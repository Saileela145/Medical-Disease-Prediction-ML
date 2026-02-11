import streamlit as st
import pickle
import numpy as np

st.set_page_config(page_title="Medical Disease Prediction")

st.title("🩺 Medical Disease Prediction")
st.write("Enter patient data to predict disease")

# Example input fields (adjust later to your dataset)
age = st.number_input("Age", min_value=0, max_value=120)
bp = st.number_input("Blood Pressure")
chol = st.number_input("Cholesterol Level")

# Dummy model logic for now
if st.button("Predict"):
    st.success("Prediction: Disease NOT Detected (demo)")
