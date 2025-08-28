# Crop_Yield_Prediction_from_soil_and_weather
# 🌱 Crop_Yield_Predictor

Crop_Yield_Predictor is a machine learning–powered application that predicts maize yield (kg/ha) based on soil and weather conditions. The app is built using Random Forest Regressor and deployed with Streamlit for an interactive interface.

## 🚀 Features

- 📊 Predict maize yield from soil & weather features
- 🧮 Uses Random Forest Regressor (best-performing model)
- 📈 Scales input data for accurate prediction
- 🖥️ Interactive Streamlit UI for manual input

## Setup

1. **Clone the repository:**
	```powershell
	git clone https://github.com/Sujan122321/Crop_yield_prediction_from_soil_and_weather.git
	cd Crop_yield_prediction_from_soil_and_weather
	```

2. **Create and activate a Conda environment:**
	```powershell
	conda create --name agriculture python=3.12.5
	conda activate agriculture
	```

3. **Install dependencies:**
	```powershell
	pip install -r requirements.txt
	```

## Usage

Run the main application (update with your main script name if different):
```powershell
streamlit run app.py
```

## Input Options
- Enter soil pH, organic matter, sand %, temperature, humidity, rainfall, and NDVI values.
- Preview inputs before prediction.
- Get maize yield prediction instantly.

## 📌 Project Workflow
- 1. Data preprocessing (scaling, cleaning)
- 2. Data Analysis(EDA, Feature Engineering, Hypothesis testing)
- 3. Hyperparameter tuning & evaluation
- 4. Model training using Random Forest
- 5. Saving model & scaler with pickle
- 6. Building Streamlit app for predictions

## 🛠️ Utilizations
- scikit-learn → model training & evaluation
- xgboost, gradient boosting (tested but Random Forest performed best)
- pickle → save & load trained model + scaler
- Streamlit → user-friendly web app

## Contributing

Contributions are welcome! Please open issues or submit pull requests for improvements.

## License

This project is licensed under the MIT License.


## contact
 gmail: suzanstha203@gmail.com