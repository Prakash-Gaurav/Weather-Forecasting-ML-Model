
# 🌦️ Weather Forecasting Using Machine Learning

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
├── WeatherApp.py                   # Streamlit application
├── weather_forecasting_model.pkl  # Trained ML model
├── README.md
└── requirements.txt
```

---

## 🧠 Machine Learning

- **Model**: Random Forest Regressor
- **Target Variables**: 
  - Temperature (°C)
  - Humidity (%)
  - Wind Speed (m/s)
- **Features Used**:
  - Wind direction, pressure, cloud coverage, precipitation
  - Time-based cyclical features (hour, month)
- **Evaluation Metrics**: MAE, RMSE

---

## 📈 Exploratory Data Analysis (EDA)

- Examined trends over time (seasonality, climate shift)
- Derived insights for feature engineering
- Created plots of temperature, precipitation, wind speed over years

---

## 💡 Streamlit App

**Run the app:**

```bash
streamlit run WeatherApp.py
```

**Features:**

- Interactive sidebar to input current weather
- Model predicts key metrics for selected conditions
- Clean and responsive UI

---

## 🛠 Setup Instructions

1. Clone the repository:

```bash
git clone https://github.com/yourusername/weather-forecasting-ml.git
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
streamlit run WeatherApp.py
```

---

## 📌 Future Enhancements

- Add weather condition (categorical) prediction
- Integrate Open-Meteo real-time API for automatic data pull
- Push predictions to a Supabase-powered Supaboard dashboard

---

## 👨‍💻 Team Members

This project was developed as a group effort by:

- **Prakash Gaurav** – [LinkedIn](https://www.linkedin.com/in/prakash-gaurav)
- **Dinesh Sharma** – [LinkedIn](https://www.linkedin.com/in/dinesh-sharma)
- **Rafi Qamar** – [LinkedIn](https://www.linkedin.com/in/rafi-qamar)

---

## 🙌 Acknowledgments

- [Open-Meteo](https://open-meteo.com) for weather data API
- Streamlit for interactive app development
- Scikit-learn for machine learning modeling

---

## 📜 License

This project is licensed under the MIT License.
