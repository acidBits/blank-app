import streamlit as st
import joblib

#carregando modelo
url = "https://github.com/acidBits/blank-app/blob/main/modelo.pkl"
r = requests.get(url)
modelo = joblib.load("modelo.pkl")


st.title("Conversor Temperatura ML")
temp = st.text.input("Digite a temperatura em Celsius:")
saida = modelo.predict([[temp]])
st.write(saida[0])
