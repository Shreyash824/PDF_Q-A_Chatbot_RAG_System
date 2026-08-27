#Search Relevant Chunks and Generate Final Answer

from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from langchain_openai import ChatOpenAI

# Initialize LLM
llm = ChatOpenAI(model="gpt-3.5-turbo")

# Create prompt template
prompt_template = PromptTemplate(
    input_variables=["context", "question"],
    template="""Context: {context}
Question: {question}
Answer:"""
)

# Create RAG chain
rag_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=db.as_retriever(),
    return_source_documents=True
)
