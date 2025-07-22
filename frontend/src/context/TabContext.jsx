import { createContext, useContext, useState } from "react";

const TabContext = createContext();

// useTab hook
export const useTab = () => useContext(TabContext);

// Provider
export const TabProvider = ({ children }) => {
  const [activeTab, setActiveTab] = useState("summary");

  return (
    <TabContext.Provider value={{ activeTab, setActiveTab }}>
      {children}
    </TabContext.Provider>
  );
};
