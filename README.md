# 🌫️ Air Quality Index (AQI) Prediction System 

An end-to-end **Machine Learning project** that predicts the **Air Quality Index (AQI)** category using real-world pollutant data.  
This project walks through the **complete ML pipeline** — from data preprocessing and model building to web app deployment using **Streamlit Cloud**.  

---

## 🚀 Project Overview  

The AQI Prediction System analyzes key pollutant levels and environmental factors to estimate overall air quality.  
Users can input pollutant values through a simple web form, and the trained model instantly predicts the **AQI category** (Good, Moderate, Poor, etc.).  

---

## 🎯 Key Objectives  

1. **Data Gathering:** Used open-source air pollution datasets (e.g., CPCB / Kaggle).  
2. **Exploratory Data Analysis (EDA):** Found patterns and correlations among pollutants.  
3. **Visualization:** Showed pollutant impact on AQI using heatmaps & scatterplots.  
4. **Data Preprocessing:** Cleaned missing values, scaled data, and encoded targets.  
5. **Modeling:** Built ML models (Linear Regression, Random Forest, XGBoost).  
6. **Evaluation:** Checked performance using **RMSE** and **R² score**.  
7. **Deployment:** Developed and hosted web app using **Streamlit Cloud**.  

---

## ⚙️ Tech Stack  

**Language:** Python  
**Libraries:**  
- pandas  
- numpy  
- matplotlib  
- seaborn  
- scikit-learn  
- streamlit

**Deployment:** Streamlit Cloud  

---

## 🌍 Input Features  

| Feature | Description |
|----------|-------------|
| PM2.5 | Fine particulate matter (µg/m³) |
| PM10 | Coarse particulate matter (µg/m³) |
| NO₂ | Nitrogen Dioxide concentration |
| SO₂ | Sulphur Dioxide concentration |
| CO | Carbon Monoxide level |
| O₃ | Ozone level |

**Output:**  
> AQI Level → Good / Satisfactory / Moderate / Poor / Very Poor / Severe  

---


## 🖥️ Web Application  

**Framework:** Streamlit  
**Hosting:** Streamlit Cloud  

**Features:**  
- Input pollutants via web form  
- Real-time AQI prediction  
- Color-coded AQI result card  
- About & Info section  

---

## 🧩 How to Run Locally  

### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/AnshulKumar001/AQI_Prediction-.git
cd AQI_Prediction-

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the streamlit run:
   ```bash
   python app.py

4. Open your browser and go to `http://localhost:5000` to access the web app.

it Cloud:
   ```bash
   git push Streamlit Cloud m### Deployment on Streamlit Cloud

To deploy the app on Streamlit Cloud, follow these steps:

1. Login to Streamlit Cloud:
   ```bash
   Streamlit Cloud login
   ```

2. Create a new Streamlit Cloud app:
   ```bash
   Streamlit Cloud create your-app-name
   ```

3. Push your code to Streamlit
   ```

4. Open the app in your browser:
   ```bash
   Streamlit Cloud open
   ```

## 💡 Future Scope

- Integrate live AQI APIs for real-time predictions.
- Add city-wise AQI dashboard with historical trends
- Deploy mobile-friendly UI.
- Experiment with deep learning (LSTM for time-series AQI prediction).
   

![dia](https://w.ndtvimg.com/sites/3/2024/01/09155352/660-1.jpg)
