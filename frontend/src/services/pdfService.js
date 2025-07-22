import axios from "axios";

const BASE_URL = import.meta.env.VITE_API_BASE_URL;

// Upload PDF
export const uploadPdf = async (file) => {
  const formData = new FormData();
  formData.append("file", file);
  const response = await axios.post(`${BASE_URL}/pdf/pdf/upload`, formData, {
    headers: {
      "Content-Type": "multipart/form-data",
    },
  });
  return response.data;
};

// Summarize PDF
export const summarizePdf = async (filename) => {
  const response = await axios.post(`${BASE_URL}/pdf/pdf/summarize`, null, {
    params: { file_name: filename },
  });
  return response.data;
};

// extract pdf text
export const extractPdf = async (filename) => {
  const response = await axios.get(`${BASE_URL}/pdf/pdf/extract`, {
    params: { file_name: filename },
  });
  return response.data;
};
