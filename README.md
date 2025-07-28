# 🏥 Health Insurance Premium Predictor

This project is a **machine learning-powered web app** that estimates a person's health insurance premium using personal, medical, and lifestyle features.

Built with:
- 🐍 Python
- 🧠 Scikit-learn
- 📊 Pandas & NumPy
- 🎯 Streamlit (for interactive UI)

---

## 📁 Project Structure

```
.
├── app.py                       # Streamlit web app
├── predcition_helper1.py       # Backend prediction + preprocessing
├── requirements.txt            # Python dependencies
├── README.md
├── artifacts/                  # Trained models and scalers
│   ├── model_young.joblib
│   ├── model_rest.joblib
│   ├── scaler_young.joblib
│   └── scaler_rest.joblib
├── notebooks/                  # Training and analysis notebooks
│   ├── ml_premium_prediction.ipynb
│   ├── ml_premium_prediction_rest.ipynb
│   ├── ml_premium_prediction_rest_with_gr.ipynb
│   ├── ml_premium_prediction_Young.ipynb
│   └── ml_premium_prediction_Young_with_gr.ipynb
```

---

## 🧠 Models

| Model Type | Age Group | Preprocessing |
|------------|-----------|----------------|
| Linear Regression / Random Forest | Age ≤ 25 (`model_young`) | StandardScaler |
| Linear Regression / Random Forest | Age > 25 (`model_rest`) | StandardScaler |

---

## 🚀 How to Run

### 🔧 Install dependencies

```bash
pip install -r requirements.txt
```

### ▶️ Launch the app

```bash
streamlit run app.py
```

---

## ✅ Inputs Considered

- Age
- Number of Dependents
- Income (in Lakhs)
- Insurance Plan (Bronze/Silver/Gold)
- Employment Status
- Gender, Marital Status
- BMI Category
- Smoking Habits
- Genetical Risk (0–5)
- Medical History (e.g., "Diabetes & Heart disease")
- Region

---

## 📦 Outputs
- Predicted Health Insurance Premium in ₹
- Personalized UI + prediction result with styling
