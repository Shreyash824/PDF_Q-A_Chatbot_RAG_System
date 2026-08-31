#Create Embeddings

from langchain_openai import OpenAIEmbeddings

# Instantiating this lazily would be nicer, but the vector DB
# construction needs an embeddings object; this is cheap (no network I/O
# happens until the first call to embed_documents/embed_query).
embeddings = OpenAIEmbeddings()
