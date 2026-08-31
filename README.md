# 📄 PDF Q&A Chatbot RAG System

An AI chatbot that answers questions **from your uploaded PDFs** instead of
from general knowledge, using Retrieval-Augmented Generation (RAG).

RAG pipeline:

```
PDF Upload → Extract Text → Chunk → Embed → Vector DB →
User Question → Similarity Search → Relevant Chunks → LLM → Answer (with sources)
```

## Project structure

```
PDF-Q-A-Chatbot-RAG-System/
├── app.py           # Streamlit UI (entry point)
├── documents.py     # PDF → text extraction (PyPDFLoader)
├── embeddings.py    # OpenAI embeddings
├── vectordb.py      # Chunking + Chroma vector store
├── rag.py           # RetrievalQA chain (LLM + prompt)
├── requirements.txt
├── .streamlit/secrets.example.toml
└── .gitignore
```

## Quick start (local)

1. **Clone / copy** this project into a folder.

2. **Create a virtual environment and install dependencies:**

   ```bash
   python -m venv .venv
   .venv\Scripts\activate        # Windows
   # source .venv/bin/activate   # macOS / Linux
   pip install -r requirements.txt
   ```

3. **Set your OpenAI API key.** Copy the example secrets file and fill in your key:

   ```bash
   copy .streamlit\secrets.example.toml .streamlit\secrets.toml
   ```

   Then edit `.streamlit\secrets.toml` so it contains your real key:
   `OPENAI_API_KEY = "sk-..."`

4. **Run the app:**

   ```bash
   streamlit run app.py
   ```

5. Open the URL Streamlit prints (default `http://localhost:8501`), upload
   one or more PDFs, and start asking questions.

## Deploy on Streamlit Community Cloud

1. Push this folder to a GitHub repository.
2. Go to https://share.streamlit.io and click **Create app** → pick the repo
   and set **Main file path** to `app.py`.
3. In the app's **Settings → Secrets** (or `⚙ → Secrets` on the dashboard),
   add your key:
   ```toml
   OPENAI_API_KEY = "sk-..."
   ```
4. Click **Deploy**. No `.streamlit/secrets.toml` should be committed — the
   cloud injects secrets at runtime.

> Note: `OPENAI_API_KEY` is read automatically by `langchain-openai` from the
> `OPENAI_API_KEY` value in secrets. If your provider/environment differs,
> set the variable accordingly.

## Notes

- The vector store is rebuilt whenever you (re)upload PDFs, so updates are
  reflected immediately.
- Source sections are shown under each answer so responses are verifiable.
