import streamlit as st
import joblib
import requests

#carregando modelo
modelo = joblib.load("modelo.pkl")

st.title("Conversor Temperatura ML")
temp = st.number_input("Digite a temperatura em Celsius:",value=0)

if st.button("Converter"):
  saida = modelo.predict([[temp]])
  st.write(f'{saida[0]}')
