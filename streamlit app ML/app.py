# Car Price Pridiction........

import streamlit as st
import pickle

## To load Model and Label Encoder

## rb = Run binary

reg = pickle.load(open("car_model.pk1","rb"))
le = pickle.load(open("label_encoder.pk1","rb"))

st.title("Car price prediction App")

car_model = st.selectbox("select Car Model",le.classes_)
milage = st.number_input("Enter Mileage (in mles)",min_value=0)
age= st.slider("Car Age(year)",0,15)
encoded_model = le.transform([car_model])[0]

if st.button("Prediction Price"):
    input_data = [[encoded_model,milage,age]]
    predicted_price = reg.predict(input_data)
    st.success(f"Estimated Selling Price: {predicted_price[0]}")