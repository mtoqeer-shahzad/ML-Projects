from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import pandas as pd
import numpy as np
import os

application = FastAPI()

# ✅ Input Schema define karo
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
@application.get("/")
def index():
    return {"message": "Student Performance Prediction API 🎓"}

# Predict Route
@application.post("/predict")
def predict(data: StudentData):  # ✅ StudentData use karo
    try:
        # Dict mein convert karo
        input_data = pd.DataFrame([data.dict()])

        # Preprocess karo
        input_scaled = preprocessor.transform(input_data)

        # Predict karo
        prediction = model.predict(input_scaled)

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
    uvicorn.run(application, host="0.0.0.0", port=8000)