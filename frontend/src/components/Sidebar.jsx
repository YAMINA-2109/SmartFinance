import React from "react";
import { useLocation, useNavigate } from "react-router-dom";
import { Home, BarChart3, MessageCircle } from "lucide-react";

const Sidebar = () => {
  const location = useLocation();
  const navigate = useNavigate();

  const tabs = [
    { id: "/", label: "Home", icon: <Home size={14} className="mr-2" /> },
    {
      id: "/dashboard",
      label: "Dashboard",
      icon: <BarChart3 size={18} className="mr-2" />,
    },
    {
      id: "/chat",
      label: "Chat",
      icon: <MessageCircle size={18} className="mr-2" />,
    },
  ];

  return (
    <aside className="w-1/5 bg-white border-r border-gray-200 p-6 h-screen shadow-sm">
      <h1 className="text-xl font-bold text-gray-800 mb-8">
        SmartFinance Analyzer
      </h1>
      <nav className="space-y-3">
        {tabs.map((tab) => (
          <button
            key={tab.id}
            onClick={() => navigate(tab.id)}
            className={`w-full flex items-center gap-2 px-4 py-2 rounded-lg text-sm font-medium transition-all duration-200 ${
              location.pathname === tab.id
                ? "bg-blue-600 text-white shadow"
                : "text-gray-700 hover:bg-gray-100"
            }`}
          >
            {tab.icon}
            <span>{tab.label}</span>
          </button>
        ))}
      </nav>
    </aside>
  );
};

export default Sidebar;
