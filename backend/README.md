---

##  📊 SmartFinance Analyzer – Backend API

**SmartFinance Analyzer** is an intelligent backend system built with **FastAPI**. It powers a financial analysis platform that allows users to upload PDF reports, extract key financial insights, generate executive summaries, and query the document using natural language.

---

### 🚀 Features

- Upload financial PDF reports
- Extract full text and structured financial data
- Summarize content with LLM (LangChain + Groq)
- Ask questions about the document with source references
- Generate CSV/JSON exports for ETL and dashboards
- CORS-enabled and ready for frontend integration

---

### 🛠️ Tech Stack

- Python 3.10+
- FastAPI
- LangChain
- Groq API
- Uvicorn
- Python-dotenv

---

### 📁 Project Structure

```bash
backend/
│
├── main.py                 # Main FastAPI application
├── init_db.py              # Database initialization script
├── groq_config.py          # Groq API configuration
├── chat_history.db         # Local SQLite database
├── requirements.txt        # Python dependencies
├── README.md               # Backend documentation
│
├── core/                   # Middleware, configuration, CORS, settings
│   ├── config.py
│   ├── cors.py
│   └── __init__.py
│
├── routers/                # API route modules
│   ├── pdf.py              # PDF upload, extraction, summarization, QA
│   ├── financial_extract.py # RAG + financial info extraction
│   ├── benchmark.py
│   ├── news.py
│   └── __init__.py
│
├── services/               # Business logic (RAG, summarization, QA, parsing, etc.)
│   ├── summarizer.py
│   ├── rag_qa.py
│   ├── rag_financial_service.py
│   ├── pdf_parser.py
│   ├── news_scraper.py
│   ├── grog_client.py
│   ├── benchmark_logic.py
│   └── __init__.py
│
├── db/                     # Database, models, and schemas
│   ├── database.py
│   ├── __init__.py
│   ├── models/
│   │   ├── chat_history.py
│   │   └── __init__.py
│   └── schemas/
│       ├── extract_schemas.py
│       ├── pdf.py
│       └── __init__.py
│
├── utils/                  # Utilities (langchain, prompts, etc.)
│   ├── langchain_loader.py
│   ├── langchain_prompt.py
│   ├── langchain_rag.py
│   └── __init__.py
│
├── uploaded_files/         # User-uploaded PDF files
├── downloads/              # Extracted/exported files (CSV, etc.)
└── venv/                   # Python virtual environment (should be ignored)
```

---

### ⚙️ Setup Instructions

1. **Clone the repository**

```bash
git clone https://github.com/YAMINA-2109/SmartFinance.git
cd backend
```

2. **Create a virtual environment**

```bash
python -m venv venv
source venv/bin/activate  # or .\venv\Scripts\activate on Windows
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Set up environment variables**

Create a `.env` file in the root of your backend:

```env
PORT=8000
GROQ_API_KEY=your_groq_key
LANGCHAIN_TRACING_V2=true
LANGCHAIN_API_KEY=your_langchain_key
ALLOWED_ORIGINS=your_frontend_url
```

5. **Run the app**

```bash
uvicorn main:app --reload
```

---

### 📬 API Routes

| Method | Endpoint                                               | Description                        |
| ------ | ------------------------------------------------------ | ---------------------------------- |
| POST   | `/pdf/pdf/upload`                                      | Upload a PDF file                  |
| POST   | `/pdf/pdf/extract`                                     | Extract text from PDF              |
| POST   | `/pdf/pdf/summarize`                                   | Generate executive summary         |
| POST   | `/pdf/pdf/qa`                                          | Ask questions based on PDF content |
| POST   | `/api/finance/finance/extract-financial-info-from-pdf` | Extract financial KPIs (RAG)       |
| GET    | `/api/finance/finance/export-csv`                      | Download CSV of financial data     |

---

### 📤 Export Example

Exports can include:

- `summary`
- `revenue`, `net income`, `free cash flow`…
- `segment revenue` breakdown
- `guidance`, `key events`, etc.

---

### 👨‍💼 Maintained by

**Yamina ATMAOUI**
