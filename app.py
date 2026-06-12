import streamlit as st
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
import tempfile
import os

# ---------------------------------------
# Page Config & Branding
# ---------------------------------------

st.set_page_config(
    page_title="AskKrish AI",
    page_icon="🧠",
    layout="wide"
)

#Header

st.title("🧠 AskKrish AI")
st.markdown("#### *Chat with any document, instantly*")
st.markdown("Built by **Krishna Kumar** · [GitHub](https://github.com/Krish00i7) · [LinkedIn](https://www.linkedin.com/in/krishnakumar-m-073027312)")
st.divider()

# ---------------------------------------
# Load API Key from Streamlit Secrets
# ---------------------------------------

groq_api_key = st.secrets["GROQ_API_KEY"]
os.environ["GROQ_API_KEY"] = groq_api_key


# ---------------------------------------
# LOAD LLM (CACHE)
# ---------------------------------------

@st.cache_resource
def load_llm():
    return ChatGroq(
        model="llama-3.1-8b-instant",
        temperature=0.5,
        max_tokens=1024
    )

llm = load_llm()


# ---------------------------------------
# SIDEBAR
# ---------------------------------------

with st.sidebar:
    st.header("📂 Upload Documents")
    uploaded_files = st.file_uploader(
        "Upload PDF files",
        type=["pdf"],
        accept_multiple_files=True
    )
    
    process_btn = st.button("🚀 Process Documents", use_container_width=True)
    
    st.divider()
    st.markdown("**How it works:**")
    st.markdown("1. Upload one or more PDFs")
    st.markdown("2. Click Process Documents")
    st.markdown("3. Ask anything!")
    st.divider()
    st.markdown("Built by **Krishna Kumar**")
    
# ─────────────────────────────────────────
# SESSION STATE
# ─────────────────────────────────────────
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "vectorstore" not in st.session_state:
    st.session_state.vectorstore = None

if "processed" not in st.session_state:
    st.session_state.processed = False
    
# ─────────────────────────────────────────
# PROCESS DOCUMENTS
# ─────────────────────────────────────────
if process_btn:
    if not uploaded_files:
        st.error("⚠️ Please upload at least one PDF!")
    else:
        with st.spinner("Processing your documents..."):

            all_chunks = []
            
            for uploaded_file in uploaded_files:
                with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
                    tmp.write(uploaded_file.read())
                    tmp_path = tmp.name
                    
                loader = PyPDFLoader(tmp_path)
                pages = loader.load()
                
                splitter = RecursiveCharacterTextSplitter(
                    chunk_size = 1000,
                    chunk_overlap = 200
                )
                
                chunks = splitter.split_documents(pages)
                all_chunks.extend(chunks)
                os.unlink(tmp_path)
                
            embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
            )
            st.session_state.vectorstore = FAISS.from_documents(all_chunks,embeddings)
            st.session_state.processed = True
            st.success(f"✅ Processed {len(uploaded_files)} PDF(s) → {len(all_chunks)} chunks ready!")



# ─────────────────────────────────────────
# CHAT INTERFACE
# ─────────────────────────────────────────
if st.session_state.processed:

    for msg in st.session_state.chat_history:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    if question := st.chat_input("Ask anything about your documents..."):

        with st.chat_message("user"):
            st.markdown(question)
        st.session_state.chat_history.append({"role": "user", "content": question})

        with st.chat_message("assistant"):
            
            retriever = st.session_state.vectorstore.as_retriever(
                search_kwargs={"k": 3}
            )

            prompt = PromptTemplate.from_template("""
You are a helpful document assistant.

Answer the question using only the provided context.

If the answer is not present in the context, reply:
"I don't know based on the provided documents."

Context:
{context}

Question:
{question}

Answer:
""")

            def format_docs(docs):
                return "\n\n".join(doc.page_content for doc in docs)

            chain = (
                {"context": retriever | format_docs, "question": RunnablePassthrough()}
                | prompt
                | llm
                | StrOutputParser()
            )

            response = st.write_stream(chain.stream(question))

            source_docs = retriever.invoke(question)
            with st.expander("📄 View Sources"):
                for i, doc in enumerate(source_docs):
                    st.markdown(f"**Source {i+1}** — Page {doc.metadata.get('page', 0) + 1}")
                    st.markdown(f"> {doc.page_content[:200]}...")
                    st.divider()

            st.session_state.chat_history.append({
                "role": "assistant",
                "content": response
            })

else:
    st.info("👈 Upload your PDFs in the sidebar and click **Process Documents** to start chatting!")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("### 📄 Any PDF")
        st.markdown("Upload resumes, reports, books, policies — anything")
    with col2:
        st.markdown("### ⚡ Instant Answers")
        st.markdown("Get answers in seconds with source references")
    with col3:
        st.markdown("### 🧠 AI Powered")
        st.markdown("Powered by LLaMA 3 + FAISS + HuggingFace")
                
                
                    
                    