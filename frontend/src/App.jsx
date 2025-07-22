import { Routes, Route } from "react-router-dom";
import Home from "./pages/Home";
import { TabProvider } from "./context/TabContext";
import "./App.css";
import Dashboard from "./pages/Dashboard";
import Layout from "./components/Layout";
import ChatPage from "./pages/ChatPage";

function App() {
  return (
    <TabProvider>
      <Routes>
        <Route element={<Layout />}>
          <Route path="/" element={<Home />} />
          <Route path="/dashboard" element={<Dashboard />} />
          <Route path="/chat" element={<ChatPage />} />
        </Route>
      </Routes>
    </TabProvider>
  );
}

export default App;
