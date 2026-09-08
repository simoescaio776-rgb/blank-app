import streamlit as st
from google import genai

st.set_page_config(page_title="Gauss & Badeco")

# Pega a chave que você já trocou
client = genai.Client(api_key=st.secrets["GEMINI_KEY"])

st.title("Gauss & Badeco - Tutores")

if "messages" not in st.session_state:
    st.session_state.messages = []

for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.markdown(m["content"])

# ESSE IF AQUI É O QUE FALTA NA SUA FOTO LINHA 24
pergunta = st.chat_input("Pergunte algo pro Gauss...")

if pergunta:
    st.session_state.messages.append({"role": "user", "content": pergunta})
    with st.chat_message("user"):
        st.markdown(pergunta)
    
    with st.chat_message("assistant"):
        resposta = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=f"Voce e o Gauss, tutor de calculo. Responda curto: {pergunta}"
        )
        st.markdown(resposta.text)
        st.session_state.messages.append({"role": "assistant", "content": resposta.text})
