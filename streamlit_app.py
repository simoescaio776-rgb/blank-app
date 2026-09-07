import streamlit as st
import google.generativeai as genai

API_KEY = "AQ.Ab8RN6J7dZSMvWw572f-M58o9JSnywLYcEUfvuabpRdt1S1xTQ"

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

st.set_page_config(page_title="Gauss & Badeco", page_icon="🤖")
st.title("Gauss & Badeco - Tutores")

if "chat" not in st.session_state:
    st.session_state.chat = []

for m in st.session_state.chat:
    with st.chat_message(m["role"]):
        st.write(m["text"])

pergunta = st.chat_input("Pergunte algo pro Gauss...")

if pergunta:
    st.session_state.chat.append({"role": "user", "text": pergunta})
    with st.chat_message("user"):
        st.write(pergunta)
    
    prompt = f"Voce e o Gauss e o Badeco, tutores. Responda: {pergunta}"
    resposta = model.generate_content(prompt)
    
    with st.chat_message("assistant"):
        st.write(resposta.text)
    
    st.session_state.chat.append({"role": "assistant", "text": resposta.text})
