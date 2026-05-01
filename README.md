# 📄 RAG-based PDF Question Answering System

This project demonstrates two implementations of Retrieval-Augmented Generation (RAG) using LangChain, Ollama, and ChromaDB.

## 🔹 Implementations

- **RAG_PDF.py** → Step-by-step (static pipeline)
- **RAG_dynamic.py** → Interactive chatbot-style Q&A

---

## 🧠 What is RAG?

RAG (Retrieval-Augmented Generation) improves LLM responses by retrieving relevant context from external data (PDF) before generating answers.

---

## ⚙️ Tech Stack

- Python
- LangChain
- Ollama (LLM + Embeddings)
- PyMuPDF (PDF Loader)
- RecursiveCharacterTextSplitter
- ChromaDB

---

## 📂 Project Structure

```
├── VectorStore/
│   └── enterprise_sales_report.pdf
├── RAG_PDF.py
├── RAG_dynamic.py
└── README.md
```

---

## 🚀 Setup

### 1. Install dependencies

```bash
pip install langchain langchain-community langchain-openai langchain-ollama chromadb pymupdf
```

### 2. Install and run Ollama

```bash
ollama pull llama3
ollama pull nomic-embed-text
ollama run llama3
```

(Optional)
```bash
ollama serve
```

---

## 🔹 RAG_PDF.py (Static Pipeline)

### Steps:
1. Load PDF
2. Split into chunks
3. Generate embeddings
4. Store in vector DB
5. Retrieve relevant chunks
6. Query LLM

### Run:

```bash
python RAG_PDF.py
```

---

## 🔹 RAG_dynamic.py (Interactive)

### Features:
- Continuous question-answer loop
- Dynamic retrieval
- Context-aware answers

### Run:

```bash
python RAG_dynamic.py
```

---

## 🔄 Workflow

```
User Query
   ↓
Vector Search (Chroma)
   ↓
Top-K Chunks
   ↓
LLM (llama3 via Ollama)
   ↓
Answer
```

---

## ⚠️ Notes

- Chroma no longer requires `.persist()` in newer versions
- Ensure Ollama models are downloaded before running
- Modify `chunk_size`, `chunk_overlap`, and `k` for better accuracy

---

## 🔧 Future Improvements

- Add Streamlit UI
- Multi-PDF support
- Chat history (memory)
- Metadata filtering
- Temperature control

---

## 👨‍💻 Author

Arsath Mohamed

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!