import streamlit as st
pdf = st.file_uploader("Upload PDF")

Ask Questions:

question = st.text_input("Ask Question")

Generate Answers:
if question:
    answer = rag_chain.invoke(question)
    st.write(answer)
