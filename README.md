# 🧠 AskKrish AI

> A RAG-powered Document Intelligence Assistant that enables users to upload PDF documents and interact with them using natural language.

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)]()
[![Streamlit](https://img.shields.io/badge/Streamlit-App-red.svg)]()
[![LangChain](https://img.shields.io/badge/LangChain-RAG-green.svg)]()
[![FAISS](https://img.shields.io/badge/FAISS-Vector%20DB-orange.svg)]()
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)]()

🌐 **Live Demo:** https://askkrishai.streamlit.app/

💻 **GitHub Repository:** https://github.com/Krish00i7/AskKrish-AI

👨‍💻 **Developer:** :contentReference[oaicite:0]{index=0}

---

## 🚀 Overview

AskKrish AI is a Retrieval-Augmented Generation (RAG) application that allows users to upload PDF documents and receive context-aware answers through a conversational interface.

Instead of relying solely on the Large Language Model's knowledge, the application retrieves relevant information directly from uploaded documents using vector embeddings and semantic search, ensuring more accurate and document-grounded responses.

---

## ✨ Features

### 📄 Multi-PDF Support
Upload and process multiple PDF documents simultaneously.

### 🧩 Intelligent Document Chunking
Splits documents into optimized chunks for efficient retrieval and context preservation.

### 🔍 Semantic Search
Uses vector embeddings and FAISS similarity search to retrieve the most relevant document sections.

### 🤖 Context-Aware Question Answering
Answers questions using only information available in uploaded documents.

### 📚 Source Citations
Displays the source chunks used to generate each answer.

### ⚡ Fast Inference
Powered by Groq's ultra-fast inference engine with Llama 3.1.

### 💬 Interactive Chat Interface
Modern Streamlit-based conversational UI.

---

## 🏗️ Architecture

```text
User Uploads PDF
         │
         ▼
 PyPDFLoader
         │
         ▼
Text Chunking
(1000 / 200)
         │
         ▼
HuggingFace Embeddings
(all-MiniLM-L6-v2)
         │
         ▼
 FAISS Vector Store
         │
         ▼
Retriever (Top-K Search)
         │
         ▼
 Prompt Template
         │
         ▼
 Groq Llama 3.1
         │
         ▼
 Context-Aware Answer
```

---

## 🛠️ Tech Stack

| Category | Technology |
|-----------|------------|
| Frontend | Streamlit |
| LLM | Llama 3.1 (Groq) |
| Framework | LangChain |
| Vector Database | FAISS |
| Embeddings | HuggingFace Embeddings |
| PDF Processing | PyPDFLoader |
| Programming Language | Python |

---

## 📂 Project Structure

```text
AskKrish-AI/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
└── .streamlit/
    └── secrets.toml
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/Krish00i7/AskKrish-AI.git

cd AskKrish-AI
```

### Create Virtual Environment

```bash
python -m venv .venv
```

### Activate Environment

#### Windows

```bash
.venv\Scripts\activate
```

#### Linux / Mac

```bash
source .venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Setup

Create:

```text
.streamlit/secrets.toml
```

Add:

```toml
GROQ_API_KEY = "your_groq_api_key"
```

---

## ▶️ Run Locally

```bash
streamlit run app.py
```

Application will be available at:

```text
http://localhost:8501
```

---

## 📸 Demo

### Upload Documents

- Upload one or more PDF files.
- Process documents using semantic embeddings.

### Ask Questions

Examples:

```text
What is this document about?

Summarize the key points.

What are the main findings?

Who is the author?
```

### View Sources

Each response includes the retrieved document chunks used for answer generation.

---

## 🧠 RAG Workflow

1. Upload PDF documents.
2. Extract text using PyPDFLoader.
3. Split documents into chunks.
4. Generate embeddings using HuggingFace.
5. Store embeddings in FAISS.
6. Convert user query into embedding.
7. Retrieve top-k relevant chunks.
8. Inject context into prompt.
9. Generate answer using Groq Llama 3.1.
10. Display answer with source references.

---

## 🎯 Skills Demonstrated

- Retrieval-Augmented Generation (RAG)
- Large Language Models (LLMs)
- Vector Databases
- Semantic Search
- Prompt Engineering
- Natural Language Processing
- Streamlit Application Development
- LangChain Pipelines
- Document Intelligence Systems
- AI Application Deployment

---

## 📈 Future Improvements

- Conversation Memory
- Hybrid Search (BM25 + Vector Search)
- Support for DOCX and TXT files
- User Authentication
- Multi-Session Chat History
- Citation Highlighting
- Docker Deployment

---

## 👨‍💻 Author

### Krishna Kumar

B.Sc Computer Science Student

🔗 LinkedIn:
https://www.linkedin.com/in/krishnakumar-m-073027312/

🔗 GitHub:
https://github.com/Krish00i7

---

## ⭐ Support

If you found this project useful:

⭐ Star the repository

🍴 Fork the project

📢 Share it with others

---

## 📄 License

This project is licensed under the MIT License.
