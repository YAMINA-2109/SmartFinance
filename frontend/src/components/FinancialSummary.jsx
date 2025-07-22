import React from "react";

const FinancialSummary = ({ summary }) => (
  <div className="bg-white p-6 rounded-xl shadow border mb-6">
    <h3 className="text-lg font-semibold text-gray-800 mb-2">Summary</h3>
    <p className="text-gray-700 whitespace-pre-wrap">
      {summary || "No summary available."}
    </p>
  </div>
);

export default FinancialSummary;
