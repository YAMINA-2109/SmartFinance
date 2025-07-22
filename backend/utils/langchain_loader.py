from langchain_community.document_loaders import PyPDFLoader, WebBaseLoader
from langchain_core.documents import Document
from typing import List

def load_pdf(file_path: str) -> str:
    """
    Charge le texte d’un fichier PDF à partir d’un chemin donné.
    Retourne tout le contenu concaténé en un seul string.
    """
    loader = PyPDFLoader(file_path)
    docs: List[Document] = loader.load()
    full_text = "\n".join([doc.page_content for doc in docs])
    return full_text


def load_web(url: str) -> str:
    """
    Charge le texte d’une page web à partir d’une URL.
    Retourne le contenu complet de la page sous forme de string.
    """
    loader = WebBaseLoader(url)
    docs: List[Document] = loader.load()
    full_text = "\n".join([doc.page_content for doc in docs])
    return full_text
