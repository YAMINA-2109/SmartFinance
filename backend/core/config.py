from json import load
import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    MODEL_NAME = "llama-3.1-8b-instant"
    GROQ_BASE_URL ="https://api.groq.com/openai/v1"
    UPLOAD_FOLDER = "uploaded_files"
    USER_AGENT = os.getenv("USER_AGENT")




settings = Settings()
