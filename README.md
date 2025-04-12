
# 🌦️ Weather Forecasting Using Machine Learning
![Image](https://github.com/user-attachments/assets/55d6313d-6a9c-4fe2-9b2c-ccfaa11418b1)
This project builds a machine learning model to forecast weather metrics such as temperature, humidity, and wind speed using historical data. It also includes a real-time interactive dashboard built with Streamlit.

---

## 📌 Overview

- 🔄 Historical data scraped from [Open-Meteo API](https://open-meteo.com/)
- 📊 35 years of hourly weather records analyzed
- 🤖 Random Forest model trained with GridSearchCV
- 🚀 Real-time predictions via a Streamlit dashboard
- 🔧 Ready for automation and deployment

---

## 📂 Project Structure

```
weather-forecasting-ml/
├── data/                           # Raw and processed datasets
├── notebooks/
│   ├── Scraping Weather Data.ipynb
│   ├── 35 Years Weather_Data EDA.ipynb
│   └── Weather_Predicting ML Model.ipynb
├── WeatherAppXGB.py                   # Streamlit application
├── xgb_weather_model.pkl  # Trained ML model
├── README.md
└── requirements.txt
```

---

## 🧠 Machine Learning

- **Model**: XGBRegressor 
- **Target Variables**: 
  - Temperature (°C)
  - Humidity (%)
  - Wind Speed (m/s)
- **Features Used**:
  - Wind direction, pressure, cloud coverage, precipitation
  - Time-based cyclical features (hour, month)
- **Evaluation Metrics**: R^2 Scores, MAE, RMSE
![Image](https://github.com/user-attachments/assets/303b0d4e-9d0b-4197-827f-1a088ea35789)
---

## 📈 Exploratory Data Analysis (EDA)

- Examined trends over time (seasonality, climate shift)
- Derived insights for feature engineering
- Created plots of temperature, precipitation, wind speed over years

---

## 💡 Streamlit App

**Run the app:** https://weather-forecasting-ml-model-prakashdineshrafi.streamlit.app/
![Image](https://github.com/user-attachments/assets/b625591f-f09a-4bd5-a64d-7607d2b67204)

```bash
streamlit run WeatherAppXGB.py
```

**Features:**

- Interactive sidebar to input current weather
- Model predicts key metrics for selected conditions
- Clean and responsive UI

---

## 🛠 Setup Instructions

1. Clone the repository:

```bash
git clone https://github.com/Prakash-Gaurav/weather-forecasting-ml.git
cd weather-forecasting-ml
```

2. Create a virtual environment and activate it:

```bash
python -m venv venv
source venv/bin/activate  # on Windows: venv\Scripts\activate
```

3. Install required packages:

```bash
pip install -r requirements.txt
```

4. Run the Streamlit app:

```bash
streamlit run WeatherAppXGB.py
```

---

## 📌 Future Enhancements

- Add weather condition (categorical) prediction
- Integrate Open-Meteo real-time API for automatic data pull
- Push predictions to a **Streamlit-powered Streamlit** dashboard

---

## 👨‍💻 Team Members

This project was developed as a group effort by:

- **Prakash Gaurav** – [LinkedIn](https://www.linkedin.com/in/prakash-gaurav-519164268/)
- **Dinesh Sharma** – [LinkedIn](https://www.linkedin.com/in/zarddinesh/)
- **Rafi Qamar** – [LinkedIn](https://www.linkedin.com/in/rafi-qamar/)

---

## 🙌 Acknowledgments

- [Open-Meteo](https://open-meteo.com) for weather data API
- Scikit-learn **Xgboost** for machine learning modeling
- Streamlit for interactive app development

---


