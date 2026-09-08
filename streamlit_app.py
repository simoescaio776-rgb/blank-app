import streamlit as st
import google.generativeai as genai
import glob

st.set_page_config(page_title="Gauss & Badeco", page_icon="📐")
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
model = genai.GenerativeModel("gemini-3.6-flash-8b")

# Carrega conhecimento
texto_conhecimento = ""
try:
    for arquivo in glob.glob("conhecimento/*.txt"):
        with open(arquivo, "r", encoding="utf-8") as f:
            texto_conhecimento += f.read()[:2000] + "\n"
except:
    pass

st.title("Gauss & Badeco")

pergunta = st.text_input("Sua dúvida de matemática / engenharia:")

escolha = st.radio("Quem vai responder?", ["🎓 Gauss (Técnico)", "😎 Badeco (Prático da Obra)"])

if st.button("Responder") and pergunta:
    if "Gauss" in escolha:
        prompt = f"Você é GAUSS, professor formal de Matemática e Engenharia. Conhecimento extra: {texto_conhecimento}. Responda diretamente: {pergunta}"
    else:
        prompt = f"Você é BADECO, mestre de obras que virou professor de Matemática e Engenharia, fala simples com exemplo de obra. Conhecimento extra: {texto_conhecimento}. Responda diretamente: {pergunta}"

    with st.spinner("Pensando..."):
        r = model.generate_content(prompt)
        st.markdown("### Resposta:")
        st.write(r.text)
