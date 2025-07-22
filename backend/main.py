from fastapi import FastAPI
from core.cors import add_cors_middleware
from routers import pdf, financial_extract, benchmark, news
from dotenv import load_dotenv
import os

load_dotenv()

PORT = os.getenv("PORT", 8000)


# initialize our app
app = FastAPI(
    title="Scalens Smart Insights",
    description="An intelligent financial assistant for IR teams using LangChain and Groq.",
    version="0.1.0"
)

# CORS middleware / allow access
add_cors_middleware(app)


# add our routers
app.include_router(pdf.router, prefix='/pdf', tags=["PDF"])
app.include_router(financial_extract.router, prefix="/api/finance", tags=["Finance"])

# app.include_router(benchmark.router, prefix="/benchmark", tags=["Benchmark"])
# app.include_router(news.router, prefix="/news", tags=["News"])

