import streamlit as st
from google import genai

st.title("Gauss & Badeco")

if "GOOGLE_API_KEY" not in st.secrets:
    st.error("Chave não encontrada nos Secrets")
    st.stop()

client = genai.Client(api_key=st.secrets["GOOGLE_API_KEY"])

def perguntar_gauss(pergunta):
    try:
        r = client.models.generate_content(
            model="gemini-1.5-flash",
            contents=f"Voce e o Gauss, tutor de calculo: {pergunta}"
        )
        return r.text
    except Exception as e:
        return f"ERRO REAL: {e}"

p = st.text_input("Digite sua pergunta")
if p:
    st.write(perguntar_gauss(p))
