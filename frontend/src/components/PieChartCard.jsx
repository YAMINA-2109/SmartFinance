import { Pie } from "react-chartjs-2";

const PieChartCard = ({ data }) => (
  <div className="bg-white p-6 rounded-xl shadow border mb-6">
    <h3 className="text-lg font-semibold text-gray-800 mb-4">
      Segment Revenue Breakdown
    </h3>
    <div className="w-[500px] mx-auto">
      <Pie data={data} />
    </div>
  </div>
);

export default PieChartCard;
