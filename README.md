# PDF_Q-A_Chatbot_RAG_System

*📚 AI Project #9: PDF Q&A Chatbot RAG System*

This is the type of project used by:  
*OpenAI* assistants  
*Microsoft Copilot*  
*Google Gemini Apps*  

Enterprise knowledge management systems

Instead of answering from general knowledge, the chatbot answers questions from uploaded documents.  
This technology is called:  
*🧠 RAG Retrieval-Augmented Generation*

*🎯 Project Goal*  
Build an AI chatbot that can:  
✅ Upload PDFs  
✅ Read documents  
✅ Understand content  
✅ Answer questions from documents  
✅ Cite relevant sections  
✅ Support multiple PDFs

📌 RAG Architecture
PDF Upload → Text Extraction → Chunking → Embeddings → Vector Database → User Question → Similarity Search → Relevant Chunks → LLM → Final Answer

📂 Project Structure
pdf-qa-chatbot/
├── documents/
├── vectordb/
├── app.py
├── rag.py
├── embeddings.py
├── requirements.txt
├── README.md
└── screenshots/
