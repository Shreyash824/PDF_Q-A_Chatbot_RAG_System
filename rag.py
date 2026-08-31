#Search Relevant Chunks and Generate Final Answer

from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from langchain_openai import ChatOpenAI

prompt_template = PromptTemplate(
    input_variables=["context", "question"],
    template="""You are a helpful assistant that answers questions strictly from the provided context.
If the answer is not present in the context, say that you don't know rather than guessing.

Context:
{context}

Question: {question}

Answer:""",
)


def build_rag_chain(retriever):
    """Build a RetrievalQA chain from a prepared retriever."""
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
    return RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        return_source_documents=True,
        chain_type_kwargs={"prompt": prompt_template},
    )
