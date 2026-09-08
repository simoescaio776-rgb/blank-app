import streamlit as st
from google import genai

client = genai.Client(api_key=st.secrets["GOOGLE_API_KEY"])

def perguntar_gauss(pergunta):
    resposta = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=f"Voce e o Gauss, tutor de calculo. Responda curto: {pergunta}"
    )
    return resposta.text

st.title("Gauss & Badeco")

pergunta = st.text_input("Pergunte algo pro Gauss...")

if pergunta:
    st.write(perguntar_gauss(pergunta))
