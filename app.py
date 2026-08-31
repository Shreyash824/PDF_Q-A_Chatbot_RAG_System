#PDF Q&A Chatbot - Streamlit UI

import os
import tempfile

import streamlit as st

from documents import load_documents
from vectordb import build_vectorstore
from rag import build_rag_chain

st.set_page_config(page_title="PDF Q&A Chatbot", page_icon="📄")
st.title("📄 PDF Q&A Chatbot (RAG)")


@st.cache_resource(show_spinner=False)
def make_rag(paths: tuple) -> object:
    """Load PDFs from disk, build the vector store, and return the RAG chain.

    Cached by the tuple of file paths, so it is only rebuilt when the set of
    uploaded files actually changes.
    """
    documents = []
    for path in paths:
        documents.extend(load_documents(path))

    vectorstore = build_vectorstore(documents)
    return build_rag_chain(vectorstore.as_retriever(search_kwargs={"k": 4}))


uploads = st.file_uploader(
    "Upload PDFs",
    type=["pdf"],
    accept_multiple_files=True,
)

rag_chain = None
if uploads:
    # Write uploads to a persistent temp dir so the cached builder can read
    # them across Streamlit re-runs.
    temp_dir = tempfile.mkdtemp(prefix="pdf_qa_")
    paths = []
    for upload in uploads:
        path = os.path.join(temp_dir, upload.name)
        with open(path, "wb") as f:
            f.write(upload.getbuffer())
        paths.append(path)

    with st.spinner("Indexing PDFs..."):
        rag_chain = make_rag(tuple(paths))
    st.success(f"Indexed {len(uploads)} PDF(s). You can now ask questions.")

question = st.text_input("Ask a question about your PDFs")

if question and rag_chain is not None:
    with st.spinner("Searching and generating an answer..."):
        result = rag_chain.invoke({"query": question})
    st.write(result["result"])

    with st.expander("📚 Source sections"):
        for i, doc in enumerate(result["source_documents"], start=1):
            st.markdown(f"**Source {i}** — page {doc.metadata.get('page', '?')}")
            st.write(doc.page_content)
elif question and rag_chain is None:
    st.warning("Please upload at least one PDF before asking a question.")
