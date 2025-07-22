import React from "react";

const FinancialCard = ({ title, data }) => {
  return (
    <div className="bg-white p-4 rounded-2xl shadow-md mb-6">
      <h2 className="text-xl font-bold mb-3 text-gray-800">{title}</h2>
      <ul className="space-y-2">
        {Object.entries(data).map(([key, value]) => (
          <li key={key} className="flex justify-between border-b pb-1">
            <span className="font-medium text-gray-600">
              {key.replace(/_/g, " ").toUpperCase()}
            </span>
            <span className="text-gray-900 font-semibold">
              {value !== null ? value : "N/A"}
            </span>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default FinancialCard;
