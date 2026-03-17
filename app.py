from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pickle
import pandas as pd
import numpy as np
import os

app = FastAPI()

# ✅ CORS Add Karo — React se connect hone ke liye
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React ka port
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Input Schema
class StudentData(BaseModel):
    gender: str
    race_ethnicity: str
    parental_level_of_education: str
    lunch: str
    test_preparation_course: str
    reading_score: int
    writing_score: int

# Model load karo
model        = pickle.load(open("artifact/model.pkl",        "rb"))
preprocessor = pickle.load(open("artifact/preprocessor.pkl", "rb"))

# Homepage
@app.get("/")
def index():
    return {"message": "Student Performance Prediction API"}

# Predict Route
@app.post("/predict")
def predict(data: StudentData):
    try:
        input_data   = pd.DataFrame([data.dict()])
        input_scaled = preprocessor.transform(input_data)
        prediction   = model.predict(input_scaled)

        return {
            "status":          "success",
            "predicted_score": round(float(prediction[0]), 2)
        }

    except Exception as e:
        return {
            "status": "failed",
            "error":  str(e)
        }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)