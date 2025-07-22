import React, { useEffect, useState } from "react";
import {
  Chart as ChartJS,
  BarElement,
  CategoryScale,
  LinearScale,
  ArcElement,
  Tooltip,
  Legend,
} from "chart.js";

import FinancialSummary from "../components/FinancialSummary";
import ExtractedFinancialData from "../components/ExtractedFinancialData";
import BarChartCard from "../components/BarChartCard";
import PieChartCard from "../components/PieChartCard";
import {
  fetchFinancialDataFromPDF,
  downloadCSVExportUrl,
} from "../services/dashboardService";

ChartJS.register(
  BarElement,
  CategoryScale,
  LinearScale,
  ArcElement,
  Tooltip,
  Legend
);

const Dashboard = () => {
  const [data, setData] = useState(null);
  const [summary, setSummary] = useState("");
  const [loading, setLoading] = useState(true);
  const filename = localStorage.getItem("uploadedPdfFilename");
  useEffect(() => {
    const load = async () => {
      try {
        const res = await fetchFinancialDataFromPDF(filename);
        setData(res.extracted_data);
        setSummary(res.summary);
      } catch (err) {
        console.error("Error fetching financial data:", err);
      } finally {
        setLoading(false);
      }
    };
    load();
  }, []);

  const getBarChartData = () => {
    if (!data) return null;
    const labels = [
      "Revenue",
      "Net Income",
      "Gross Margin",
      "Operating Cash Flow",
      "Free Cash Flow",
      "CAPEX",
    ];
    const values = labels.map((label) => {
      const key = label.toLowerCase().replace(/ /g, "_");
      const value = data[key];
      return typeof value === "string" && value.includes("$")
        ? parseFloat(value.replace(/[$M]/g, "")) || 0
        : parseFloat(value) || 0;
    });

    return {
      labels,
      datasets: [
        {
          label: "Financial Values (in M)",
          data: values,
          backgroundColor: "#2563eb",
        },
      ],
    };
  };

  const getPieChartData = () => {
    if (!data?.segment_revenue) return null;
    const labels = Object.keys(data.segment_revenue);
    const values = labels.map((key) => {
      const value = data.segment_revenue[key];
      return typeof value === "string" && value.includes("$")
        ? parseFloat(value.replace(/[$M]/g, "")) || 0
        : parseFloat(value) || 0;
    });

    return {
      labels,
      datasets: [
        {
          label: "Segment Revenue",
          data: values,
          backgroundColor: ["#3b82f6", "#10b981", "#f59e0b", "#ef4444"],
        },
      ],
    };
  };

  return (
    <main className="flex-1 p-8 overflow-y-auto bg-gray-100 min-h-screen">
      <div className="p-8">
        <h2 className="text-2xl font-bold mb-4">Financial Dashboard</h2>

        {loading ? (
          <p className="text-gray-500">Loading data...</p>
        ) : (
          <>
            <FinancialSummary summary={summary} />
            <ExtractedFinancialData data={data} />
            {getBarChartData() && <BarChartCard data={getBarChartData()} />}
            {getPieChartData() && <PieChartCard data={getPieChartData()} />}
            <a
              href={downloadCSVExportUrl}
              download
              className="inline-block mt-6 px-4 py-2 bg-green-600 text-white text-sm rounded hover:bg-green-700 transition"
            >
              Download CSV
            </a>
          </>
        )}
      </div>
    </main>
  );
};

export default Dashboard;
