from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from core.config import settings

SUMMARY_PROMPT = PromptTemplate.from_template("""
You are a professional financial analyst assistant.

Your task is to read the following financial document and generate a clean and professional executive summary in **HTML format**.

Structure the summary into the following sections, each with a proper heading (`<h3>`), and bullet points (`<ul><li>`):

1. Key Financial Metrics
2. Strategic Initiatives and Business Highlights
3. Market and Operational Performance
4. Guidance and Outlook
5. Notable Events or Announcements

Use <strong> for key figures (e.g., revenue, growth, margin). Do not use Markdown (**). Return only HTML.

Document:
{text}
""")

# SUMMARY_PROMPT = PromptTemplate.from_template("""
# You are a professional financial analyst assistant working for a company that provides intelligent financial summaries to investors and executive teams.

# Your task is to read the following financial document and generate a structured executive summary using clear bullet points.

# The summary must be structured in the following sections:
# 1. Key Financial Metrics
# 2. Strategic Initiatives and Business Highlights
# 3. Market and Operational Performance
# 4. Guidance and Outlook
# 5. Notable Events or Announcements

# Each section must contain 2 to 5 concise bullet points.
# Use professional business language.
# When relevant, highlight numerical figures (revenues, margins, growth %, CAPEX, FCF, etc.).

# Document:
# {text}
# """)

# SUMMARY_PROMPT = PromptTemplate.from_template("""
# Act as a senior financial assistant.

# Summarize the following financial document in a highly concise and professional executive summary of 5 to 7 bullet points maximum.

# Emphasize:
# - Revenue and earnings
# - Business performance highlights
# - Strategic decisions
# - Guidance and forecast

# Avoid redundancy. Use formal language.

# Document:
# {text}
# """)

# Création du LLMChain
def build_summary_chain():
    llm = ChatGroq(
        api_key=settings.GROQ_API_KEY,
        model_name="llama-3.1-8b-instant" 
    )
    return SUMMARY_PROMPT | llm | StrOutputParser()


def summarize_text(text: str) -> str:
    chain = build_summary_chain()
    return chain.invoke({"text": text})
