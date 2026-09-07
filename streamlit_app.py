import streamlit as st
from google import genai

st.set_page_config(page_title="Gauss & Badeco")

# pega sua chave AQ que você já colocou
api_key = st.secrets["AQ.Ab8RN6K3ezKPNegbSIcAoqss8y5KOJ5PTqGTFt_Y33iVvvmXww"]
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
            model="gemini-2.0-flash",
            contents=f"Você é o Gauss, tutor de cálculo. Explique de forma simples: {prompt}"
        )
        st.markdown(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})

