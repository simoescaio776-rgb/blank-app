import streamlit as st
import google.generativeai as genai
import glob

st.set_page_config(page_title="Gauss & Badeco", page_icon="📐")
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
model = genai.GenerativeModel("gemini-3.6-flash")

# Carrega conhecimento (se tiver)
texto_conhecimento = ""
try:
    for arquivo in glob.glob("conhecimento/*.txt"):
        with open(arquivo, "r", encoding="utf-8") as f:
            texto_conhecimento += f.read()[:2000] + "\n"
except:
    texto_conhecimento = ""

st.title("Gauss & Badeco - Matemática + Engenharia")

pergunta = st.text_input("Faça sua pergunta:")

if pergunta:
    prompt_gauss = f"""
    Você é o GAUSS, especialista em Matemática e Engenharia.
    CONHECIMENTO EXTRA: {texto_conhecimento}
    REGRA MAIS IMPORTANTE: Responda DIRETAMENTE a pergunta do usuário: {pergunta}
    Seja técnico e formal.
    """
    prompt_badeco = f"""
    Você é o BADECO, mestre de obras que virou professor de Matemática e Engenharia.
    CONHECIMENTO EXTRA: {texto_conhecimento}
    REGRA MAIS IMPORTANTE: Responda DIRETAMENTE a pergunta do usuário: {pergunta}
    Seja prático, simples, com exemplo de obra.
    """

    r1 = model.generate_content(prompt_gauss)
    r2 = model.generate_content(prompt_badeco)

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("🎓 Gauss")
        st.write(r1.text)
    with col2:
        st.subheader("😎 Badeco")
        st.write(r2.text)
