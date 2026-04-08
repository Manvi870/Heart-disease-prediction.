import streamlit as st
import pickle
import numpy as np

# load model + scaler
model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

# Title
st.markdown("<h1 style='text-align: center; color: red;'> Heart Disease Prediction</h1>", unsafe_allow_html=True)
st.markdown("### Enter patient details to check risk")

st.markdown("---")
st.sidebar.title("ℹ️ About")
st.sidebar.write("This app predicts heart disease risk using Machine Learning.")
st.sidebar.write("Developed by You ")

# Layout (2 columns)
col1, col2 = st.columns(2)

# numeric inputs
age = st.number_input("Age")
bp = st.number_input("Resting BP")
chol = st.number_input("Cholesterol")
fbs = st.number_input("Fasting BS")
maxhr = st.number_input("Max HR")
oldpeak = st.number_input("Oldpeak")

# categorical inputs
sex = st.selectbox("Sex", ["F", "M"])
cp = st.selectbox("Chest Pain Type", ["ATA","NAP","TA"])
ecg = st.selectbox("Resting ECG", ["Normal","ST"])
angina = st.selectbox("Exercise Angina", ["N","Y"])
slope = st.selectbox("ST Slope", ["Flat","Up"])

if st.button("Predict"):
    
    # dummy encoding manually
    data = [age, bp, chol, fbs, maxhr, oldpeak,
            1 if sex=="M" else 0,
            1 if cp=="ATA" else 0,
            1 if cp=="NAP" else 0,
            1 if cp=="TA" else 0,
            1 if ecg=="Normal" else 0,
            1 if ecg=="ST" else 0,
            1 if angina=="Y" else 0,
            1 if slope=="Flat" else 0,
            1 if slope=="Up" else 0]

 #scaling..
    data = scaler.transform([data])   

    result = model.predict(data)

    if result[0] == 1:
        st.write("High risk of Heart Disease")
    else:
        st.write("Low risk")