import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Gauss & Badeco", page_icon="📐")
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

# Deixa o modelo carregado na memória (fica mais rápido)
@st.cache_resource
def get_model():
    return genai.GenerativeModel("gemini-pro")

model = get_model()

st.title("Gauss & Badeco")

pergunta = st.text_input("Sua dúvida de matemática / engenharia:")

col1, col2 = st.columns(2)
with col1:
    gauss = st.button("🎓 Gauss", use_container_width=True)
with col2:
    badeco = st.button("😎 Badeco", use_container_width=True)

if pergunta and (gauss or badeco):
    # Prompt CURTO = resposta RÁPIDA
    if gauss:
        prompt = f"Você é Gauss, professor técnico de Engenharia. Seja objetivo e técnico. Pergunta: {pergunta}"
        titulo = "### 🎓 Gauss:"
    else:
        prompt = f"Você é Badeco, mestre de obras. Explique simples com exemplo de obra. Pergunta: {pergunta}"
        titulo = "### 😎 Badeco:"

    with st.spinner("..."):
        resposta = model.generate_content(prompt)
        st.markdown(titulo)
        st.write(resposta.text)
