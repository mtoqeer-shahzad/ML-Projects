// src/services/api.ts
import { StudentData, PredictionResult } from "../types/index";  // ✅ path fix

export const predictScore = async (
  data: StudentData
): Promise<PredictionResult> => {
  const response = await fetch("http://localhost:8000/predict", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data),
  });
  return response.json();
};
