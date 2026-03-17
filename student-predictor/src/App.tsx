import React, { useState } from "react";
import { StudentData, PredictionResult } from "./types/index";
import { predictScore } from "./services/api";
import "./App.css";

const App: React.FC = () => {

  const [formData, setFormData] = useState<StudentData>({
    gender: "",
    race_ethnicity: "",
    parental_level_of_education: "",
    lunch: "",
    test_preparation_course: "",
    reading_score: 0,
    writing_score: 0,
  });

  const [result, setResult]   = useState<PredictionResult | null>(null);
  const [loading, setLoading] = useState<boolean>(false);
  const [error, setError]     = useState<string>("");

  const handleChange = (
    e: React.ChangeEvent<HTMLSelectElement | HTMLInputElement>
  ) => {
    const { name, value } = e.target;
    setFormData((prev: StudentData) => ({  // ✅ type add kiya
      ...prev,
      [name]: name.includes("score") ? Number(value) : value,
    }));
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError("");
    setResult(null);
    setLoading(true);
    try {
      const data = await predictScore(formData);
      setResult(data);
    } catch (err) {
      setError("FastAPI se connect nahi hua!");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app">
      <div className="container">
        <h1>Student Score Predictor</h1>
        <form onSubmit={handleSubmit}>

          <div className="field">
            <label>Gender</label>
            <select name="gender" value={formData.gender} onChange={handleChange}>
              <option value="">Select</option>
              <option value="female">Female</option>
              <option value="male">Male</option>
            </select>
          </div>

          <div className="field">
            <label>Race / Ethnicity</label>
            <select name="race_ethnicity" value={formData.race_ethnicity} onChange={handleChange}>
              <option value="">Select</option>
              <option value="group A">Group A</option>
              <option value="group B">Group B</option>
              <option value="group C">Group C</option>
              <option value="group D">Group D</option>
              <option value="group E">Group E</option>
            </select>
          </div>

          <div className="field">
            <label>Parental Education</label>
            <select name="parental_level_of_education"
              value={formData.parental_level_of_education}
              onChange={handleChange}>
              <option value="">Select</option>
              <option value="some high school">Some High School</option>
              <option value="high school">High School</option>
              <option value="some college">Some College</option>
              <option value="associate's degree">Associate's Degree</option>
              <option value="bachelor's degree">Bachelor's Degree</option>
              <option value="master's degree">Master's Degree</option>
            </select>
          </div>

          <div className="field">
            <label>Lunch</label>
            <select name="lunch" value={formData.lunch} onChange={handleChange}>
              <option value="">Select</option>
              <option value="standard">Standard</option>
              <option value="free/reduced">Free / Reduced</option>
            </select>
          </div>

          <div className="field">
            <label>Test Preparation</label>
            <select name="test_preparation_course"
              value={formData.test_preparation_course}
              onChange={handleChange}>
              <option value="">Select</option>
              <option value="none">None</option>
              <option value="completed">Completed</option>
            </select>
          </div>

          <div className="field">
            <label>Reading Score</label>
            <input type="number" name="reading_score"
              min={0} max={100} placeholder="0-100"
              value={formData.reading_score || ""}
              onChange={handleChange}
            />
          </div>

          <div className="field">
            <label>Writing Score</label>
            <input type="number" name="writing_score"
              min={0} max={100} placeholder="0-100"
              value={formData.writing_score || ""}
              onChange={handleChange}
            />
          </div>

          {error && <p className="error">{error}</p>}

          <button type="submit" disabled={loading}>
            {loading ? "Predicting..." : "Predict Score"}
          </button>

        </form>

        {result?.status === "success" && (
          <div className="result">
            <h2>Predicted Math Score</h2>
            <h1>{result.predicted_score}</h1>
          </div>
        )}

      </div>
    </div>
  );
};

export default App;