import streamlit as st
import pandas as pd
import pickle

# Load trained model
with open("best_model (1).pkl", "rb") as file:
    model = pickle.load(file)

# App title
st.title("🏥 Insurance Charges Prediction App")
st.write("Enter the details below to predict insurance charges.")

# Sidebar or input form
st.sidebar.header("Input Features")

# Input fields
age = st.sidebar.number_input("Age", min_value=18, max_value=100, value=30)
sex = st.sidebar.selectbox("Sex", ["male", "female"])
bmi = st.sidebar.number_input("BMI", min_value=10.0, max_value=50.0, value=25.0)
children = st.sidebar.number_input("Children", min_value=0, max_value=10, value=0)
smoker = st.sidebar.selectbox("Smoker", ["yes", "no"])
region = st.sidebar.selectbox("Region", ["southeast", "southwest", "northeast", "northwest"])

# Prepare input data
input_data = pd.DataFrame({
    "age": [age],
    "sex": [sex],
    "bmi": [bmi],
    "children": [children],
    "smoker": [smoker],
    "region": [region]
})

# Prediction button
if st.button("Predict Charges"):
    try:
        prediction = model.predict(input_data)
        st.success(f"💰 Predicted Insurance Charge: **${prediction[0]:,.2f}**")
    except Exception as e:
        st.error(f"An error occurred while predicting: {e}")

# Footer
st.markdown("---")
st.markdown("Made with ❤️ using Streamlit")
