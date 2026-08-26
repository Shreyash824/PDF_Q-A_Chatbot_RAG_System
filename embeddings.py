#Create Embeddings

from langchain.embedding
import OpenAIEmbeddings
embeddings = OpenAIEmbeddings()


#Store in Vector Database

from langchain.vectorstores 
import Chromadb = Chroma.from_documents(chunks, embeddings)
