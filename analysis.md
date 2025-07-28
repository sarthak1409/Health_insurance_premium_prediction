# 📊 Model Training & Analysis

## 📌 Dataset
The dataset includes features like:
- Age, Income, Number of Dependents
- Gender, Marital Status
- BMI Category, Smoking Status
- Employment Status, Region
- Insurance Plan, Genetical Risk, Medical History

## 🔧 Preprocessing
- One-hot encoding for categorical variables
- Manual mapping for insurance plans (Bronze=1, Silver=2, Gold=3)
- Normalized medical risk score based on conditions like:
  - Diabetes: 6
  - Heart Disease: 8
  - Thyroid: 5
  - etc.

## 🧠 Modeling Strategy
- Two separate models trained:
  - `model_young`: for users aged ≤ 25
  - `model_rest`: for users aged > 25
- Models used: Linear Regression / Random Forest
- Scaling: StandardScaler applied only to numeric columns

## 🏁 Output
- Trained models and scalers saved as `.joblib` files
- Integrated into a Streamlit UI for live prediction

## ✅ Notebooks
The following Jupyter notebooks were used to train and evaluate models:
- `ml_premium_prediction.ipynb`
- `ml_premium_prediction_Young.ipynb`
- `ml_premium_prediction_rest.ipynb`
- `*_with_gr.ipynb`: Variants including Genetical Risk
