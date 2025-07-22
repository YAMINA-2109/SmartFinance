from langchain_groq import ChatGroq
from config import settings

# Initialisation du modèle LLM via Groq
llm = ChatGroq(
    api_key=settings.GROQ_API_KEY,
    model="llama3-70b-8192"
)