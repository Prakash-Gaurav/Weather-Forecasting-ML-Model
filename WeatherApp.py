import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load the saved model.
model = joblib.load("weather_forecasting_model.pkl")

st.title("Weather Forecasting Dashboard")

st.markdown("### Input the current weather conditions:")

# Sidebar inputs for features.
wind_direction = st.sidebar.slider("Wind Direction", 0.0, 360.0, 180.0)
pressure = st.sidebar.slider("Pressure (hPa)", 1001.0, 1021.0, 1010.0)
precipitation = st.sidebar.slider("Precipitation (mm)", 0.0, 2.0, 0.0)
cloud_coverage = st.sidebar.slider("Cloud Coverage (%)", 0.0, 100.0, 50.0)
hour = st.sidebar.slider("Hour of Day", 0, 23, 12)
dayofweek = st.sidebar.selectbox("Day of the Week (0=Monday)", list(range(7)))
month = st.sidebar.slider("Month", 1, 12, 6)

# Compute the cyclical features.
hour_sin = np.sin(2 * np.pi * hour / 24)
hour_cos = np.cos(2 * np.pi * hour / 24)
month_sin = np.sin(2 * np.pi * month / 12)
month_cos = np.cos(2 * np.pi * month / 12)

# Create the input DataFrame for prediction.
input_features = pd.DataFrame([{
    "wind_direction": wind_direction,
    "pressure": pressure,
    "precipitation": precipitation,
    "cloud_coverage": cloud_coverage,
    "hour_sin": hour_sin,
    "hour_cos": hour_cos,
    "month_sin": month_sin,
    "month_cos": month_cos,
    "dayofweek": dayofweek
}])

st.markdown("### Forecasted Weather Metrics:")
# Get predictions from the model.
predicted = model.predict(input_features)

# The model outputs: [temperature, humidity, wind_speed]
st.write(f"**Temperature:** {predicted[0][0]:.2f} °C")
st.write(f"**Humidity:** {predicted[0][1]:.2f} %")
st.write(f"**Wind Speed:** {predicted[0][2]:.2f} m/s")