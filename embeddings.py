#Split Into Chunks

from langchain.text_splitter import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)
chunks = splitter.split_documents(documents)

#Create Embeddings

from langchain.embedding
import OpenAIEmbeddings
embeddings = OpenAIEmbeddings()


#Store in Vector Database

from langchain.vectorstores 
import Chromadb = Chroma.from_documents(chunks, embeddings)
