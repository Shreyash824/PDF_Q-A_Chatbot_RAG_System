#Search Relevant Chunks

docs = db.similarity_search(question, k=3)

#Generate Final Answer

Context: {retrieved_chunks}  
Question: {user_question}
response = llm.invoke(prompt)
