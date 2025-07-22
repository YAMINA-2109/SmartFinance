import { Bar } from "react-chartjs-2";

const BarChartCard = ({ data }) => (
  <div className="bg-white p-6 rounded-xl shadow border mb-6">
    <h3 className="text-lg font-semibold text-gray-800 mb-4">
      Key Financial Metrics
    </h3>
    <Bar data={data} />
  </div>
);

export default BarChartCard;
