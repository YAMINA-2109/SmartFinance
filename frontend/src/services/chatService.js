import axios from "axios";

const API_URL = import.meta.env.VITE_API_BASE_URL;

export const uploadPdfFile = async (file) => {
  const formData = new FormData();
  formData.append("file", file);
  const res = await axios.post(`${API_URL}/pdf/pdf/upload`, formData);
  return res.data;
};

export const askQuestionToPdf = async ({ filename, question, chatHistory }) => {
  const res = await axios.post(`${API_URL}/pdf/pdf/qa`, {
    filename,
    question,
    chat_history: chatHistory,
  });
  return res.data;
};
