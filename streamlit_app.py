import streamlit as st
import joblib
import requests

#carregando modelo
modelo = joblib.load("modelo.pkl")

st.title("Conversor Temperatura ML")
#temp = st.text.input("Digite a temperatura em Celsius:")
saida = modelo.predict([[temp]])
st.write(saida[0])
