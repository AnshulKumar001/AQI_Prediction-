import streamlit as st
import joblib
import numpy as np
import os

# Load model (relative path so it works on Streamlit Cloud)
model = joblib.load(os.path.join(os.path.dirname(__file__), "model.pkl"))

st.title("AQI Prediction App")

year = st.number_input("Year", value=2021)
month = st.number_input("Month", value=1)
holidays_count = st.number_input("Holidays Count", value=0)
days = st.number_input("Days", value=5)
pm25 = st.number_input("PM2.5", value=408.80)
pm10 = st.number_input("PM10", value=442.42)
no2 = st.number_input("NO2", value=160.61)
so2 = st.number_input("SO2", value=12.95)
co = st.number_input("CO", value=2.77)
ozone = st.number_input("Ozone", value=43.19)

if st.button("Predict"):
    input_data = np.array([[month, year, holidays_count, days, pm25, pm10, no2, so2, co, ozone]])
    prediction = model.predict(input_data)
    st.success(f"Predicted AQI: {prediction[0]}")
