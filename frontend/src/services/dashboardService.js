import axios from "axios";

// const BASE_URL = import.meta.env.VITE_API_BASE_URL;
const BASE_URL = "http://localhost:8000";

export const fetchFinancialDataFromPDF = async (filename) => {
  const res = await axios.post(
    `${BASE_URL}/api/finance/finance/extract-financial-info-from-pdf`,
    {
      pdf_filename: filename,
    }
  );
  return res.data;
};

export const downloadCSVExportUrl = `${BASE_URL}/api/finance/finance/export-csv`;
