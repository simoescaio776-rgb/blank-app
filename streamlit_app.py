import streamlit as st
import google.generativeai as genai
import glob

st.set_page_config(page_title="Gauss & Badeco", page_icon="📐")
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
model = genai.GenerativeModel("gemini-2.5-flash")

def carregar_conhecimento():
    texto = ""
    for arquivo in glob.glob("conhecimento/*.txt"):
        with open(arquivo, "r", encoding="utf-8") as f:
            texto += f.read() + "\n"
    return texto

conhecimento = carregar_conhecimento()

prompt_base = f"""
Você domina TODA A MATEMÁTICA e TODA A ENGENHARIA (civil, elétrica, mecânica, etc).
Use este conhecimento extra: {conhecimento}
"""

prompt_gauss = prompt_base + "\nVocê é o GAUSS, explique de forma formal, técnica, com fórmulas."
prompt_badeco = prompt_base + "\nVocê é o BADECO, explique de forma prática, simples, com exemplos de obra e dia a dia."

st.title("Gauss & Badeco - Matemática + Engenharia")

modo = st.radio("Quem responde?", ["Gauss", "Badeco", "Os dois juntos"])
pergunta = st.text_input("Qual sua dúvida de matemática ou engenharia?")

if pergunta:
    if modo == "Gauss":
        r = model.generate_content(prompt_gauss + f"\nPERGUNTA: {pergunta}")
        st.markdown(f"**🎓 Gauss:** {r.text}")
    elif modo == "Badeco":
        r = model.generate_content(prompt_badeco + f"\nPERGUNTA: {pergunta}")
        st.markdown(f"**😎 Badeco:** {r.text}")
    else:
        r1 = model.generate_content(prompt_gauss + f"\nPERGUNTA: {pergunta}")
        r2 = model.generate_content(prompt_badeco + f"\nPERGUNTA: {pergunta}")
        c1, c2 = st.columns(2)
        with c1: st.markdown(f"**🎓 Gauss:** {r1.text}")
        with c2: st.markdown(f"**😎 Badeco:** {r2.text}")
