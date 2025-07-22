from langchain_groq import ChatGroq
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from core.config import settings
from pathlib import Path
from db.database import SessionLocal
from db.models.chat_history import ChatHistory

# Dossier des pdf de user
UPLOAD_DIR = Path("uploaded_files")

# Split PDF
splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)

# Embeddings
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

def get_llm():
    return ChatGroq(
        api_key=settings.GROQ_API_KEY,
        model_name="llama3-70b-8192"
    )

def ask_question(filename: str, question: str, chat_history: list[tuple[str, str]]) -> dict:
    # Charge our PDF
    filepath = UPLOAD_DIR / filename
    if not filepath.exists():
        raise FileNotFoundError("PDF file not found.")
    
    loader = PyPDFLoader(str(filepath))
    pages = loader.load_and_split()

    # Vector store
    vectorstore = FAISS.from_documents(pages, embedding_model)
    retriever = vectorstore.as_retriever()

    # set Memory
    memory = ConversationBufferMemory(
        memory_key="chat_history",
        return_messages=True,
        output_key="answer"
    )

    # Injecte l’historique
    for user, bot in chat_history:
        memory.chat_memory.add_user_message(user)
        memory.chat_memory.add_ai_message(bot)

    chain = ConversationalRetrievalChain.from_llm(
        llm=get_llm(),
        retriever=retriever,
        memory=memory,
        return_source_documents=True
    )

    result = chain.invoke({"question": question})
    answer = result["answer"]
    sources = [
        {
            "page": doc.metadata.get("page", None),
            "content": doc.page_content
        }
        for doc in result["source_documents"]
    ]
    db = SessionLocal()
    chat = ChatHistory(
        filename=filename,
        question=question,
        answer=result["answer"]
    )
    db.add(chat)
    db.commit()
    db.close()
    return {"answer": answer, "sources": sources}
