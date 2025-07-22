from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQA
from langchain.chains.llm import LLMChain
from langchain_core.documents import Document
from langchain_groq import ChatGroq
from utils.langchain_prompt import financial_prompt_details
from core.config import settings
import json
import re


from langchain.chains.combine_documents.stuff import StuffDocumentsChain

def build_rag_chain(docs: list[Document]):
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    splits = splitter.split_documents(docs)

    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectorstore = FAISS.from_documents(splits, embeddings)
    retriever = vectorstore.as_retriever(search_type="mmr", k=6)

    llm = ChatGroq(
        api_key=settings.GROQ_API_KEY,
        model="llama3-70b-8192"
    )

    # LLM Chain
    llm_chain = LLMChain(
        llm=llm,
        prompt=financial_prompt_details
    )

    # Emballage dans StuffDocumentsChain
    stuff_chain = StuffDocumentsChain(
        llm_chain=llm_chain,
        document_variable_name="context"
    )

    # RAG
    rag_chain = RetrievalQA(
        retriever=retriever,
        combine_documents_chain=stuff_chain,
        return_source_documents=False,
        input_key="context" 
    )

    return rag_chain



def query_rag_chain_details(source_text: str):
    """
    Appelle la chaîne RAG construite à partir d’un texte source.
    Attend une réponse JSON, nettoie et extrait `summary` et `fields`.
    """

    docs = [Document(page_content=source_text)]
    rag_chain = build_rag_chain(docs)

    # Appel du modèle avec la bonne clé
    response = rag_chain.invoke({"context": source_text})
    raw_result = response["result"]

    print("=== RAW RESULT ===")
    print(raw_result)

    try:
        match = re.search(r"\{.*\}", raw_result.strip(), re.DOTALL)
        if not match:
            raise ValueError("No JSON object found.")
        json_str = match.group(0)
        output = json.loads(json_str)

        summary = output.get("summary", "")
        fields = output.get("fields", {})
    except Exception as e:
        print(f"JSON parsing failed: {e}")
        summary = raw_result
        fields = {}

    return summary, fields

