import React, { useState, useEffect } from "react";
import { getInsights, runTask } from "./services";

export default function App() {
  const [insights, setInsights] = useState([]);

  // load insights on first render
  useEffect(() => {
    loadInsights();
  }, []);

  async function loadInsights() {
    try {
      const data = await getInsights();
      setInsights(data);
    } catch (err) {
      console.error("Failed to load insights:", err);
    }
  }

  async function handleRunTask() {
    try {
      await runTask();      // call backend
      await loadInsights(); // refresh list immediately
    } catch (err) {
      console.error("Run Task failed:", err);
    }
  }

  return (
    <div style={{ padding: 20, fontFamily: "sans-serif" }}>
      <h1>AI Worker Dashboard</h1>
      <button onClick={handleRunTask} style={{ padding: "8px 16px", marginBottom: 20 }}>
        Run Task Now
      </button>

      {insights.length === 0 ? (
        <p>No insights yet. Click "Run Task Now".</p>
      ) : (
        insights.map((i) => (
          <div key={i.id} style={{ border: "1px solid #ddd", padding: 10, marginBottom: 10 }}>
            <p><b>Topics:</b> {i.topics}</p>
            <p><b>Summary:</b><br />{i.summary}</p>
            <p><b>Recommendations:</b><br />{i.recommendations}</p>
          </div>
        ))
      )}
    </div>
  );
}
