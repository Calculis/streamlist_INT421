import streamlit as st
import pickle
import numpy as np

def preprocess(bmi,age,stroke):

    return np.array([[bmi,age,stroke]])

with open('linear_regression_model.pkl','rb') as m:
    model = pickle.load(m)
st.title('Predict your glucose level from your BMI (for stroke individual)')
bmi = st.number_input("Enter your bmi", step=0.1, min_value=10.0, max_value=100.0, format="%.2f")
age = st.number_input("Enter your age", step=1, min_value=20, max_value=100)
stroke = st.radio('Are you have stroke disorder', [1, 0], captions=['Yes', 'No'])
button_clicked = st.button("Enter")
if button_clicked:
    prediction = model.predict(preprocess(bmi,stroke,age))
    st.write(f"Your estimate Glucose: {prediction[0][0]:.4f}")




