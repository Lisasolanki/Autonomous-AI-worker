const API = import.meta.env.VITE_API || "http://localhost:8000";

export async function getInsights() {
  const res = await fetch(`${API}/insights`);
  return res.json();
}

export async function runTask() {
  const res = await fetch(`${API}/run`, { method: "POST" });
  return res.json();
}
