from utils import db_connect
engine = db_connect()

# your code here
import streamlit as st
import numpy as np
import joblib

# Cargar el modelo entrenado
model = joblib.load('./models/model_reducido.pkl')

# Título
st.title("✈️ Predicción del Precio de Vuelo")

# Inputs del usuario
airline = st.selectbox("Aerolínea", [
    "Vistara", "Air_India", "Indigo", "GO_FIRST", "AirAsia"
])
source_city = st.selectbox("Ciudad de origen", [
    "Delhi", "Mumbai", "Bangalore", "Kolkata", "Hyderabad"
])
destination_city = st.selectbox("Ciudad de destino", [
    "Delhi", "Mumbai", "Bangalore", "Kolkata", "Hyderabad"
])
flight_class = st.selectbox("Clase del vuelo", ["Economy", "Business"])
duration = st.slider("Duración del vuelo (horas)", 0.83, 49.8, 1.0)

# Mapping de valores al LabelEncoder original (esto depende de tu encoding)
airline_dict = {
    "Vistara": 0,
    "Air_India": 1,
    "Indigo": 2,
    "GO_FIRST": 3,
    "AirAsia": 4
}

city_dict = {
    "Delhi": 0,
    "Mumbai": 1,
    "Bangalore": 2,
    "Kolkata": 3,
    "Hyderabad": 4
}

class_dict = {
    "Economy": 0,
    "Business": 1
}

# Botón para predecir
if st.button("Predecir precio"):
    features = np.array([[ 
        airline_dict[airline], 
        city_dict[source_city], 
        city_dict[destination_city], 
        class_dict[flight_class], 
        duration
    ]])
    prediction = model.predict(features)[0]
    st.success(f"💰 Precio estimado del vuelo: ${round(prediction, 2)}")

