"""Initial Streamlit landing page for Customer Churn Intelligence.

The application is a scaffold. It deliberately does not claim that planned
modelling, evaluation, or deployment features are implemented.
"""
import streamlit as st

st.set_page_config(page_title="Customer Churn Intelligence", page_icon="🧪", layout="wide")
st.title("Customer Churn Intelligence")
st.caption("Explainable and uncertainty-aware customer churn prediction")
st.warning("Development scaffold: core workflows are being implemented.")

st.subheader("Research question")
st.write("How do churn models compare when evaluated not only by ranking performance, but also by probability calibration and the practical costs of false-positive and false-negative decisions?")

st.subheader("Planned methodology")
for item in ["Dataset inspection, missing-value analysis, and leakage checks", "Stratified train/validation/test split and cross-validation where appropriate", "Logistic Regression baseline", "Random Forest and XGBoost comparison", "Class-imbalance-aware evaluation", "Probability calibration and uncertainty-aware reporting", "SHAP-based global and individual explanations", "Transparent rule-based retention suggestions"]:
    st.write("• " + item)

st.subheader("Project status")
st.write("Scope defined · Implementation in progress · Evaluation pending · Deployment pending")
