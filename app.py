import pickle
import streamlit as st
import pandas as pd



# load Saved model
with open(r"Notebook\random_forest_model.pkl", "rb") as f:
    model = pickle.load(f)
    
# load saved scaler
with open(r"Notebook\scaler.pkl", "rb") as f:
    scaler = pickle.load(f)
    

# UI section
st.set_page_config(page_title="🌱 Crop Yield Predictor", page_icon="🌽", layout="centered")
st.title("🌱 Crop Yield Prediction App")
st.markdown("""
This app predicts **maize yield (kg/ha)** based on soil and weather features.
Enter the feature values below and click **Predict Yield**.
""")

# --- User input ---
st.sidebar.header("Input Features")

soil_ph = st.sidebar.slider("Soil pH", 0.0, 14.0, 6.5)
organic_matter = st.sidebar.slider("Organic Matter (%)", 0.0, 100.0, 5.0)
sand_pct = st.sidebar.slider("Sand (%)", 0.0, 100.0, 40.0)
temperature = st.sidebar.slider("Temperature (°C)", -50.0, 60.0, 25.0)
humidity = st.sidebar.slider("Humidity (%)", 0.0, 100.0, 50.0)
rainfall = st.sidebar.slider("Rainfall (mm)", 0.0, 5000.0, 200.0)
ndvi = st.sidebar.slider("NDVI", -1.0, 1.0, 0.5)

# --- Create dataframe for prediction ---
input_data = pd.DataFrame([[soil_ph, organic_matter, sand_pct, temperature, humidity, rainfall, ndvi]],
                          columns=['soil_ph','organic_matter','sand_pct','temperature','humidity','rainfall','ndvi'])

# Display input features
st.markdown("### Your Input Values")
st.dataframe(input_data)

# --- Scale features ---
input_scaled = scaler.transform(input_data)

# --- Predict ---
if st.button("Predict Yield 🌽"):
    prediction = model.predict(input_scaled)
    st.success(f"🌽 Predicted Maize Yield: {prediction[0]:.2f} kg/ha")