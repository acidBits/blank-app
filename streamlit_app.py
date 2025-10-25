import streamlit as st
import joblib
import requests

#carregando modelo
url = "https://github.com/acidBits/blank-app/blob/main/modelo.pkl"
#r = requests.get(url)
modelo = joblib.load(url)


st.title("Conversor Temperatura ML")
temp = st.text.input("Digite a temperatura em Celsius:")
saida = modelo.predict([[temp]])
st.write(saida[0])
