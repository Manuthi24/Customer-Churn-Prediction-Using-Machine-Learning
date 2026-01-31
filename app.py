import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load trained model and encoders
model = joblib.load("models/customer_churn_model.pkl")
encoders = joblib.load("models/encoders.pkl")

st.title("Customer Churn Prediction App")

st.write("""
Upload a CSV file of customer data with the same columns as the training dataset
to predict which customers will churn.
""")

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("### Uploaded Data", df.head())

    # ----- Manual encoding for Gender (avoid LabelEncoder issues) -----
    if "Gender" in df.columns:
        df["Gender"] = df["Gender"].map({
            "Male": 1,
            "Female": 0
        })

    # ----- Encode other categorical columns safely -----
    for col, encoder in encoders.items():
        if col in df.columns and col != "Gender":
            df[col] = df[col].apply(
                lambda x: encoder.transform([x])[0]
                if x in encoder.classes_
                else -1  # unseen category
            )

    # Fill missing values
    df = df.fillna(0)

    # ----- Predictions -----
    predictions = model.predict(df)
    df["Churn Prediction"] = predictions

    probabilities = model.predict_proba(df)[:, 1]
    df["Churn Probability"] = np.round(probabilities, 2)

    st.write("### Prediction Results", df)
