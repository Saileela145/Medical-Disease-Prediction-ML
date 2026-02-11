import streamlit as st
import pickle
import numpy as np

# Load trained model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

st.set_page_config(page_title="Medical Disease Prediction")

st.title("🩺 Medical Disease Prediction")
st.write("Enter patient details to predict diabetes")

# Input fields (based on diabetes dataset)
pregnancies = st.number_input("Pregnancies", min_value=0)
glucose = st.number_input("Glucose Level")
blood_pressure = st.number_input("Blood Pressure")
skin_thickness = st.number_input("Skin Thickness")
insulin = st.number_input("Insulin Level")
bmi = st.number_input("BMI")
dpf = st.number_input("Diabetes Pedigree Function")
age = st.number_input("Age", min_value=0)

if st.button("Predict"):

    input_data = np.array([[pregnancies, glucose, blood_pressure,
                            skin_thickness, insulin, bmi, dpf, age]])

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("Prediction: Diabetes Detected")
    else:
        st.success("Prediction: No Diabetes Detected")
