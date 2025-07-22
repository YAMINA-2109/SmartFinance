from langchain_core.prompts import PromptTemplate

financial_prompt_details = PromptTemplate.from_template("""
You are a financial analyst. Analyze the following financial document and extract key financial data.

Your response must ONLY be a valid JSON object in the following format:

{{
  "summary": "...",
  "fields": {{
    "revenue": "...",
    "net_income": "...",
    "gross_margin": "...",
    "operating_cash_flow": "...",
    "free_cash_flow": "...",
    "EPS": "...",
    "non_GAAP_EPS": "...",
    "EBITDA": "...",
    "EBITDA_margin": "...",
    "CAPEX": "...",
    "cash_and_equivalents": "...",
    "R&D_expenses": "...",
    "guidance": {{
      "revenue_next_quarter": "...",
      "EPS_next_quarter": "..."
    }},
    "segment_revenue": {{
      "Product": "...",
      "Services": "..."
    }},
    "geographic_breakdown": {{
      "USA": "...",
      "EMEA": "...",
      "APAC": "..."
    }}
  }}
}}



DO NOT return any explanation, comment, markdown or text outside the JSON.

Document:
{context}
""")



# first prompt not realy valid for json
# financial_prompt_details = PromptTemplate.from_template("""
# You are a financial analyst. Analyze the provided content and extract all relevant financial data such as:
# - Revenue (by product, geography, quarterly trends)
# - Gross Margin
# - EPS (Earnings Per Share)
# - Operating Cash Flow
# - CAPEX
# - Any other key financial KPIs

# Give your answer in clean, structured, human-readable English.
# Context:
# {context}
# """)