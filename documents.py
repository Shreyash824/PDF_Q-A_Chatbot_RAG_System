
#Load PDF*
from langchain.document_loaders import PyPDFLoader

loader=
PyPDFLoader("document.pdf")
documents = loader.load()
