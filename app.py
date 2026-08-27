#Upload PDFs:

import streamlit as st
from documents import documents
from embeddings import embeddings
from vectordb import db
from rag import rag_chain

pdf = st.file_uploader("Upload PDF")

#Ask Questions:

question = st.text_input("Ask Question")

#Generate Answers:
if question:
    answer = rag_chain.invoke({"query": question})
    st.write(answer["result"])
