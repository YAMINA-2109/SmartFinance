import React, { useState } from "react";
import PdfUpload from "../components/PdfUpload";
import PdfViewer from "../components/PdfViewer";
import { useTab } from "../context/TabContext";

const Home = () => {
  const { activeTab } = useTab();
  const [uploadData, setUploadData] = useState(null);

  return (
    <div className="space-y-6">
      <PdfUpload onUploadSuccess={setUploadData} />
      {uploadData && (
        <PdfViewer
          extractedText={uploadData.extractedText}
          summary={uploadData.summary}
          activeTab={activeTab}
        />
      )}
    </div>
  );
};

export default Home;
