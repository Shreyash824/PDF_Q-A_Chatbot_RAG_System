#Store in Vector Database

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from embeddings import embeddings

CHROMA_DIR = "./chroma_db"


def build_vectorstore(documents):
    """Split documents into chunks, embed them, and persist to Chroma.

    Rebuilds the vector store each time it is called so that newly
    uploaded PDFs are actually searchable.
    """
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
    )
    chunks = text_splitter.split_documents(documents)

    if not chunks:
        raise ValueError("No text could be extracted from the uploaded PDF.")

    return Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=CHROMA_DIR,
    )
