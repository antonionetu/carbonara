"use client";

import { useState } from "react";
import { Rnd } from "react-rnd";
import { useDropzone } from "react-dropzone";
import axios from "axios";

interface ChartWindow {
  id: number;
  question: string;
  answer: string;
  chart: string;
}

export default function ChartGenerator() {
  const [files, setFiles] = useState<File[]>([]);
  const [question, setQuestion] = useState("");
  const [kindOfChart, setKindOfChart] = useState("");
  const [windows, setWindows] = useState<ChartWindow[]>([]);
  const [loading, setLoading] = useState(false);

  const { getRootProps, getInputProps } = useDropzone({
    onDrop: (acceptedFiles) => setFiles(acceptedFiles),
  });

  const handleSubmit = async () => {
    if (!question || !kindOfChart || files.length === 0) {
      alert("Please fill all fields and upload files.");
      return;
    }

    const formData = new FormData();
    files.forEach(file => formData.append("files", file));
    formData.append("question", question);
    formData.append("kind_of_chart", kindOfChart);

    try {
      setLoading(true);
      const response = await axios.post("http://localhost:8000/generate-chart", formData, {
        headers: { "Content-Type": "multipart/form-data" },
      });

      const { question: q, answer, chart } = response.data;

      setWindows(prev => [
        ...prev,
        { id: Date.now(), question: q, answer, chart }
      ]);
    } catch (error) {
      console.error(error);
      alert("Failed to generate chart.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="p-4">
      <div className="space-y-4">
        <div {...getRootProps()} className="border-2 border-dashed p-4 rounded cursor-pointer">
          <input {...getInputProps()} />
          <p>Drop files here or click to select</p>
        </div>

        <input
          type="text"
          placeholder="Enter your question"
          className="border p-2 w-full rounded"
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
        />
        <input
          type="text"
          placeholder="Type of chart (e.g., bar, line)"
          className="border p-2 w-full rounded"
          value={kindOfChart}
          onChange={(e) => setKindOfChart(e.target.value)}
        />

        <button
          onClick={handleSubmit}
          disabled={loading}
          className="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600"
        >
          {loading ? "Generating..." : "Generate Chart"}
        </button>
      </div>

      <div className="relative w-full h-screen mt-8">
        {windows.map((win) => (
          <Rnd
            key={win.id}
            default={{
              x: 20,
              y: 20,
              width: 500,
              height: 400,
            }}
            bounds="parent"
            minWidth={300}
            minHeight={200}
          >
            <div className="bg-white border shadow-lg w-full h-full p-2 overflow-auto rounded">
              <div className="font-bold mb-2">{win.question}</div>
              <div className="mb-2">{win.answer}</div>
              <div dangerouslySetInnerHTML={{ __html: win.chart }} />
            </div>
          </Rnd>
        ))}
      </div>
    </div>
  );
}
