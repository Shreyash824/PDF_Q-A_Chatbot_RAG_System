#Upload PDFs:

import streamlit as st
from documents import load_documents
from embeddings import embeddings
from vectordb import db
from rag import rag_chain

pdf = st.file_uploader("Upload PDF")

if pdf:
    # Save the uploaded file temporarily and load it
    with open("temp_document.pdf", "wb") as f:
        f.write(pdf.getbuffer())
    documents = load_documents("temp_document.pdf")

question = st.text_input("Ask Question")

if question:
    answer = rag_chain.invoke({"query": question})
    st.write(answer["result"])
