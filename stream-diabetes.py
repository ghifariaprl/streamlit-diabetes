import pickle
import streamlit as st

diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))

st.title('Diabetes Prediction App')

Pregnancies = st.text_input ('Input nilai Pregnancies')
Glucose = st.text_input ('Input nilai Glucose')
Bloodpressure = st.text_input ('Input nilai Blood Pressure')
Skinthickness = st.text_input ('Input nilai Skinthick')
Insulin = st.text_input ('Input nilai Insulin')
BMI = st.text_input ('Input nilai BMI')
DiabetesPedigreeFunction = st.text_input ('Input nilai Diabetes Pedigree Function')
Age = st.text_input ('Input nilai Age')

diab_diagonosis = ''

if st.button('Predict'):
    diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, Bloodpressure, Skinthickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])

    if (diab_prediction[0] == 1):
        diab_diagonosis = 'Pasien Terkena Diabetes'
    else:
        diab_diagonosis = 'Pasien Tidak Terkena Diabetes'
    
    st.success(diab_diagonosis)