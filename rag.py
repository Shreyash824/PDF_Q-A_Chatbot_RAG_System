#Load PDF*
from langchain.document_loaders import PyPDFLoader

loader=
PyPDFLoader("document.pdf")
documents = loader.load()

#Split Into Chunks

from langchain.text_splitter import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)
chunks = splitter.split_documents(documents)

#Search Relevant Chunks

docs = db.similarity_search(question, k=3)

#Generate Final Answer

Context: {retrieved_chunks}  
Question: {user_question}
response = llm.invoke(prompt)
