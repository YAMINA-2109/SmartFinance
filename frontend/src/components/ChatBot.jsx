import React, { useEffect, useRef, useState } from "react";
import { uploadPdfFile, askQuestionToPdf } from "../services/chatService";
import { MessageSquareText } from "lucide-react";

const ChatBot = () => {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const [filename, setFilename] = useState(null);
  const [chatHistory, setChatHistory] = useState([]);
  const [loading, setLoading] = useState(false);
  const bottomRef = useRef();

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

  const handleFileUpload = async (e) => {
    const file = e.target.files[0];
    if (!file || !file.name.endsWith(".pdf")) return;
    try {
      await uploadPdfFile(file);
      setFilename(file.name);
      setMessages([{ role: "system", text: `PDF "${file.name}" uploaded.` }]);
    } catch (err) {
      console.error("Upload error:", err);
      alert("Failed to upload PDF.");
    }
  };

  const handleSend = async () => {
    if (!input.trim() || !filename) return;
    setLoading(true);
    const userMessage = { role: "user", text: input };
    setMessages((prev) => [...prev, userMessage]);
    setInput("");

    try {
      const response = await askQuestionToPdf({
        filename,
        question: input,
        chatHistory,
      });
      const botMessage = {
        role: "bot",
        text: response.answer,
        sources: response.sources,
      };
      setMessages((prev) => [...prev, botMessage]);
      setChatHistory((prev) => [...prev, [input, response.answer]]);
    } catch (err) {
      console.error("QA error:", err);
      setMessages((prev) => [
        ...prev,
        { role: "bot", text: "Error fetching answer. Please try again." },
      ]);
    }
    setLoading(false);
  };

  return (
    <main className="flex-1 p-6 bg-gray-100 min-h-screen mt-10">
      <div className="max-w-3xl mx-auto bg-white p-6 rounded-2xl shadow">
        <h2 className="text-2xl font-bold mb-6 flex items-center gap-2 text-gray-800">
          <MessageSquareText className="w-6 h-6 text-blue-600" />
          Ask anything about your PDF
        </h2>

        <p className="text-gray-600 mb-2">
          Please upload a PDF file to start chatting
        </p>
        <label
          htmlFor="pdf-upload"
          className="cursor-pointer inline-block px-5 py-2 mb-2 bg-gray-100 text-gray-800 rounded hover:bg-blue-700 hover:text-white transition"
        >
          Upload your PDF
        </label>
        <input
          id="pdf-upload"
          type="file"
          accept=".pdf"
          onChange={handleFileUpload}
          className="hidden"
        />

        <div className="space-y-4 mt-4 max-h-[500px] overflow-y-auto border p-4 rounded bg-gray-50">
          {messages.map((msg, i) => (
            <div
              key={i}
              className={`${msg.role === "user" ? "text-right" : "text-left"}`}
            >
              <p
                className={`inline-block px-4 py-2 rounded-xl ${
                  msg.role === "user"
                    ? "bg-blue-500 text-white"
                    : "bg-gray-200 text-gray-800"
                }`}
              >
                {msg.text}
              </p>
              {msg.sources && (
                <div className="mt-1 text-sm text-gray-500">
                  <strong>Sources:</strong>
                  <ul className="list-disc ml-5">
                    {msg.sources.map((src, idx) => (
                      <li key={idx}>Page {src.page}</li>
                    ))}
                  </ul>
                </div>
              )}
            </div>
          ))}
          <div ref={bottomRef}></div>
        </div>

        <div className="mt-4 flex items-center gap-2">
          <input
            type="text"
            placeholder="Ask your question..."
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyDown={(e) => e.key === "Enter" && handleSend()}
            className="flex-1 border rounded px-4 py-2"
          />
          <button
            onClick={handleSend}
            disabled={loading}
            className={`px-4 py-2 rounded text-white ${
              loading
                ? "bg-gray-400 cursor-not-allowed"
                : "bg-blue-600 hover:bg-blue-700"
            }`}
          >
            {loading ? "Thinking..." : "Send"}
          </button>
        </div>
      </div>
    </main>
  );
};

export default ChatBot;
