#Store in Vector Database

from langchain.vectorstores import Chroma

db = Chroma.from_documents(chunks, embeddings)
