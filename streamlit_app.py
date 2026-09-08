import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Gauss & Badeco", page_icon="⚡")
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

# ESSE é o modelo do 3.6 que funcionou ontem
model = genai.GenerativeModel("models/gemini-pro")

st.title("Gauss & Badeco - 3.6 TURBO ⚡")

pergunta = st.text_input("Sua dúvida de matemática/engenharia:")
escolha = st.radio("Quem responde?", ["🎓 Gauss", "😎 Badeco"], horizontal=True)

if st.button("Responder") and pergunta:
    if "Gauss" in escolha:
        prompt = f"Você é o GAUSS, professor técnico e formal de Matemática e Engenharia. Responda curto, direto e técnico: {pergunta}"
    else:
        prompt = f"Você é o BADECO, mestre de obras, fala simples, prático, com exemplo de obra. Responda curto e direto: {pergunta}"

    texto = st.empty()
    full = ""
    for chunk in model.generate_content(prompt, stream=True):
        if hasattr(chunk, 'text') and chunk.text:
            full += chunk.text
            texto.markdown(full)
