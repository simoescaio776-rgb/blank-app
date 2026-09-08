import streamlit as st
from google import genai
import time

st.title("Gauss & Badeco")

client = genai.Client(api_key=st.secrets["GOOGLE_API_KEY"])

def perguntar_gauss(pergunta):
    modelo = "gemini-3.6-flash"
    for tentativa in range(5):
        try:
            r = client.models.generate_content(
                model=modelo,
                contents=f"Voce e o Gauss, tutor de Calculo 1: {pergunta}"
            )
            return r.text
        except Exception as e:
            if "503" in str(e):
                time.sleep(2)
                continue
            else:
                return f"ERRO REAL: {e}"
    return "Google lotado, espera 1 minuto e tenta de novo."

p = st.text_input("Digite sua pergunta")
if p:
    with st.spinner("Gauss pensando..."):
        st.write(perguntar_gauss(p))
