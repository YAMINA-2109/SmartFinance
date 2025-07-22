import React from "react";

const ExtractedFinancialData = ({ data }) => {
  if (!data) {
    return (
      <div className="bg-white p-6 rounded-xl shadow border mb-6">
        <h3 className="text-lg font-semibold text-gray-800 mb-4">
          Extracted Financial Data
        </h3>
        <p className="text-gray-500 text-sm">No data available.</p>
      </div>
    );
  }

  return (
    <div className="bg-white p-6 rounded-xl shadow border mb-6">
      <h3 className="text-lg font-semibold text-gray-800 mb-4">
        Extracted Financial Data
      </h3>
      <ul className="list-disc pl-6 text-sm text-gray-700 space-y-1">
        {Object.entries(data).map(([key, value]) => (
          <li key={key}>
            <strong>{key}:</strong>{" "}
            {typeof value === "object"
              ? JSON.stringify(value)
              : value?.toString() || "N/A"}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default ExtractedFinancialData;
