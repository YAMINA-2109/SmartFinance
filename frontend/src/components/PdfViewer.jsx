import React from "react";

const PdfViewer = ({ extractedText, summary, activeTab }) => {
  return (
    <div className="space-y-6">
      {activeTab === "summary" && (
        <div className="bg-white p-6 rounded-xl shadow border border-gray-200">
          <div
            className="prose prose-sm max-w-none text-gray-700"
            dangerouslySetInnerHTML={{
              __html: summary || "<p>No summary available.</p>",
            }}
          />
        </div>
      )}

      {activeTab === "extract" && (
        <div className="bg-white p-6 rounded-xl shadow border border-gray-200 max-h-[400px] overflow-y-auto">
          <h3 className="text-lg font-semibold text-gray-800 mb-4">
            Extracted Text
          </h3>
          <pre className="text-sm text-gray-700 whitespace-pre-wrap leading-relaxed">
            {extractedText || "No extracted text."}
          </pre>
        </div>
      )}
    </div>
  );
};

export default PdfViewer;
