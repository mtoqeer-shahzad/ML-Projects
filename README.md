<img width="944" height="420" alt="image" src="https://github.com/user-attachments/assets/897c636e-8776-4556-a18a-8dc67cc6d8bd" />
<img width="814" height="425" alt="image" src="https://github.com/user-attachments/assets/22bc7393-9a8b-43f4-9b22-6aafd6dc1693" />




# 🎓 Student Performance Predictor

An end-to-end Machine Learning project that predicts a student's **Math Score** based on demographic and academic features — with a FastAPI backend and React TypeScript frontend.

---

## 📌 Problem Statement

Predict how a student's **math score** is affected by variables such as:
- Gender
- Race / Ethnicity
- Parental Level of Education
- Lunch Type
- Test Preparation Course
- Reading Score
- Writing Score

---

## 🏗️ Project Architecture

```
Student Performance Predictor
│
├── Backend  (FastAPI)       → REST API + ML Model
├── Frontend (React + TS)    → User Interface
└── ML Model (Scikit-learn)  → Prediction Engine
```

---

## 📁 Project Structure

```
ML-PROJECT/
├── app.py                          ← FastAPI application
├── artifact/
│   ├── model.pkl                   ← Trained ML model
│   ├── preprocessor.pkl            ← Data preprocessor
│   ├── train.csv                   ← Training data
│   └── test.csv                    ← Testing data
├── src/
│   ├── components/
│   │   ├── data_ingestion.py       ← Data loading & splitting
│   │   ├── data_transformation.py  ← Feature engineering
│   │   └── model_trainer.py        ← Model training
│   ├── custom_exception.py         ← Custom error handling
│   ├── logger.py                   ← Logging setup
│   └── utils.py                    ← Helper functions
├── notebook/
│   ├── EDA.ipynb                   ← Exploratory Data Analysis
│   ├── model_training.ipynb        ← Model training notebook
│   └── data/stud.csv               ← Raw dataset
├── student-predictor/              ← React TypeScript frontend
│   └── src/
│       ├── App.tsx
│       ├── App.css
│       ├── types/index.ts
│       └── services/api.ts
├── requirements.txt
├── setup.py
└── logs/                           ← Application logs
```

---

## 🧠 ML Pipeline

```
Raw Data (stud.csv)
      ↓
Data Ingestion     → train.csv / test.csv
      ↓
Data Transformation → OneHotEncoding + StandardScaling
      ↓
Model Training     → GridSearchCV (7 models)
      ↓
Best Model Saved   → model.pkl + preprocessor.pkl
      ↓
FastAPI Deployment → REST API
      ↓
React Frontend     → User Interface
```

---

## 🤖 Models Trained

| Model | Description |
|---|---|
| Linear Regression | Baseline model |
| Ridge | Regularized regression |
| Lasso | L1 regularization |
| K-Neighbors Regressor | Distance-based |
| Decision Tree | Tree-based model |
| Random Forest | Ensemble method |
| Gradient Boosting | Boosting method |
| XGBoost | Extreme gradient boosting |
| AdaBoost | Adaptive boosting |

> Best model is automatically selected based on **R² Score**

---

## 📊 Dataset

| Feature | Type | Values |
|---|---|---|
| gender | Categorical | male, female |
| race_ethnicity | Categorical | group A–E |
| parental_level_of_education | Categorical | some high school → master's degree |
| lunch | Categorical | standard, free/reduced |
| test_preparation_course | Categorical | none, completed |
| reading_score | Numerical | 0–100 |
| writing_score | Numerical | 0–100 |
| **math_score** | **Target** | **0–100** |

- **Rows:** 1000
- **Columns:** 8
- **Missing Values:** None

---

## 🚀 Getting Started

### Prerequisites

```bash
Python 3.8+
Node.js 16+
```

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/ML-PROJECT.git
cd ML-PROJECT
```

### 2. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 3. Train the Model

```bash
python src/components/data_ingestion.py
```

This will automatically:
- Load and split the data
- Transform features
- Train all models
- Save the best model to `artifact/`

### 4. Start FastAPI Backend

```bash
uvicorn app:application --reload
```

API will be available at: `http://localhost:8000`

### 5. Start React Frontend

```bash
cd student-predictor
npm install
npm start
```

Frontend will be available at: `http://localhost:3000`

---

## 🔌 API Endpoints

### `GET /`
Returns API status.

```json
{
  "message": "Student Performance Prediction API"
}
```

### `POST /predict`
Predicts math score.

**Request Body:**
```json
{
  "gender": "female",
  "race_ethnicity": "group B",
  "parental_level_of_education": "master's degree",
  "lunch": "standard",
  "test_preparation_course": "completed",
  "reading_score": 95,
  "writing_score": 93
}
```

**Response:**
```json
{
  "status": "success",
  "predicted_score": 91.25
}
```

> Interactive API docs available at: `http://localhost:8000/docs`

---

## 🧪 Sample Predictions

| Student Type | Reading | Writing | Predicted Math |
|---|---|---|---|
| Low Performer | 45 | 42 | ~47 |
| Average Student | 65 | 62 | ~69 |
| High Performer | 98 | 97 | ~89 |

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.8, TypeScript |
| ML Framework | Scikit-learn, XGBoost |
| Backend | FastAPI, Uvicorn |
| Frontend | React, TypeScript |
| Data Processing | Pandas, NumPy |
| Serialization | Dill, Pickle |
| Logging | Python logging |
| Version Control | Git, GitHub |

---

## 📈 Key Insights from EDA

- Female students tend to perform better than male students
- Students with **standard lunch** score higher than free/reduced lunch
- **Test preparation course** completion improves scores
- Higher **parental education** positively impacts student performance
- Reading and writing scores are strongly correlated with math scores

---

## 🔧 Environment Variables

Create a `.env` file in the root directory:

```env
GROQ_API_KEY=your_key_here
HF_TOKEN=your_token_here
```

---

## 📝 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Muhammad Toqeer**
- GitHub: [@mtoqeer-shahzad](https://github.com/mtoqeer-shahzad)

---

## ⭐ Show Your Support

If this project helped you, please give it a **star** on GitHub! ⭐
