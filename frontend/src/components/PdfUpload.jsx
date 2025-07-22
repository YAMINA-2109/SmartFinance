import { useState } from "react";
import { uploadPdf, extractPdf, summarizePdf } from "../services/pdfService";
import { CheckCircle, LoaderCircle } from "lucide-react";

const PdfUpload = ({ onUploadSuccess }) => {
  const [file, setFile] = useState(null);
  const [filename, setFilename] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [success, setSuccess] = useState(false);

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
    setError(null);
    setSuccess(false);
  };

  const handleUpload = async () => {
    if (!file) {
      setError("Please select a PDF file.");
      return;
    }

    try {
      setLoading(true);
      const response = await uploadPdf(file);
      const uploadedFilename = response.filename;
      setFilename(uploadedFilename);

      const extractData = await extractPdf(uploadedFilename);
      const summaryData = await summarizePdf(uploadedFilename);

      onUploadSuccess({
        filename: uploadedFilename,
        extractedText: extractData.content,
        summary: summaryData.summary,
      });

      localStorage.setItem("uploadedPdfFilename", uploadedFilename);
      setSuccess(true);
    } catch (error) {
      const err = error.response?.data;
      setError(
        typeof err === "string" ? err : err?.msg || "Something went wrong."
      );
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="bg-white p-6 rounded-xl shadow mb-6 border border-gray-200">
      <h2 className="text-lg font-semibold text-gray-800 mb-3">
        Upload a PDF File
      </h2>

      <div className="flex items-center gap-4 flex-wrap">
        <input
          id="pdf-upload"
          type="file"
          accept=".pdf"
          onChange={handleFileChange}
          className="hidden"
        />
        <label
          htmlFor="pdf-upload"
          className="cursor-pointer inline-block px-5 py-2 bg-gray-100 text-gray-800 rounded hover:bg-blue-700 hover:text-white transition"
        >
          Upload your PDF
        </label>
        <button
          onClick={handleUpload}
          disabled={!file || loading}
          className={`px-5 py-2 rounded text-white text-sm transition-all ${
            loading
              ? "bg-gray-400 cursor-not-allowed"
              : "bg-blue-600 hover:bg-blue-700"
          }`}
        >
          {loading ? (
            <span className="flex items-center gap-2">
              <LoaderCircle className="animate-spin w-4 h-4" />
              Uploading...
            </span>
          ) : (
            "Summarize"
          )}
        </button>
      </div>

      {success && (
        <div className="mt-4 text-green-600 flex items-center gap-2 text-sm">
          <CheckCircle className="w-5 h-5" />
          PDF <strong>{filename}</strong> uploaded and processed successfully!
        </div>
      )}

      {error && <p className="mt-4 text-red-500 text-sm">{error}</p>}
    </div>
  );
};

export default PdfUpload;
