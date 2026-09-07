import streamlit as st
from google import genai

st.set_page_config(page_title="Gauss & Badeco")
api_key = st.secrets["GEMINI_KEY"]
client = genai.Client(api_key=api_key)

st.title("Gauss & Badeco - Tutores")

if "messages" not in st.session_state:
    st.session_state.messages = []

for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.markdown(m["content"])

prompt = st.chat_input("Pergunte algo pro Gauss...")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    with st.chat_message("assistant"):
        response = client.models.generate_content(
            model="gemini-1.5-flash",
            contents=f"Voce e o Gauss, tutor de calculo. Explique: {prompt}"
        )
        st.markdown(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})
