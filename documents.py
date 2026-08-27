from langchain_community.document_loaders import PyPDFLoader

loader=
PyPDFLoader("document.pdf")
documents = loader.load()


