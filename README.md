![Python](https://img.shields.io/badge/Python-Data%20Science-blue)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Supervised%20Learning-green)
![Scikit‑Learn](https://img.shields.io/badge/Scikit--Learn-Modeling-yellow)
![XGBoost](https://img.shields.io/badge/XGBoost‑Boosting‑Model-orange)
![EDA](https://img.shields.io/badge/EDA‑Exploratory%20Data%20Analysis-lightgrey)
![Data Visualization](https://img.shields.io/badge/Data‑Visualization-red)
![Model Serialization](https://img.shields.io/badge/Serialization‑Pickle-blueviolet)
![Portfolio Project](https://img.shields.io/badge/Type‑Portfolio%20Project-important)


# 📊 Customer Churn Prediction Using Machine Learning

This project predicts customer churn for a telecommunications company using machine learning.  
The goal is to build a model that identifies which customers are most likely to **churn (leave)** based on their characteristics and interaction data.

---

## 🧠 Project Summary

Customer churn is when a customer stops using a company’s service. Reducing churn is critical for businesses to retain revenue and grow. This project uses supervised machine learning to analyze historical customer data and build a predictive model.

---

## 📁 Repository Contents

```
├── WA_Fn-UseC_-Telco-Customer-Churn.csv # Dataset
├── customer_churn_model.pkl # Trained Machine Learning Model
├── encoders.pkl # Encoders for categorical features
├── app.py # Streamlit application
├── requirements.txt # Required Python packages
└── README.md # Project documentation

```
---
## 📌 Dataset

The dataset contains customer information and churn labels.  
It includes features such as:

| Feature | Description |
|---------|-------------|
| customerID | Unique customer identifier |
| gender | Male or Female |
| SeniorCitizen | 0 = No, 1 = Yes |
| Partner | Whether customer has a partner |
| Dependents | Whether customer has dependents |
| tenure | Number of months with the company |
| PhoneService | Whether customer has phone service |
| InternetService | Type of internet service |
| MonthlyCharges | Monthly bill amount |
| TotalCharges | Total bill amount to date |
| Churn | Target column (Yes = churn, No = stay) |

---

## 🛠 Used Technologies

- Python  
- pandas, numpy  
- scikit‑learn  
- joblib  
- Streamlit  

---

## 🚀 How to Run the App

### 🔹 Step 1 — Install Requirements

```bash
pip install -r requirements.txt

```

### 🔹 Step 2 — Run Streamlit App
```
streamlit run app.py

```
Then open your browser at:

```
Then open your browser at:
```

---


