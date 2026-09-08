import streamlit as st
from google import genai
import time

# --- CONFIG ---
st.set_page_config(page_title="Gauss & Badeco", page_icon="📐", layout="centered")
st.title("📐 Gauss & Badeco")
st.caption("Tutores de Cálculo 1 - Rigor de Gauss + Jeito do Badeco")

# --- CLIENTE GOOGLE ---
if "GOOGLE_API_KEY" not in st.secrets:
    st.error("Coloca a chave GOOGLE_API_KEY nos Secrets do Streamlit!")
    st.stop()

client = genai.Client(api_key=st.secrets["GOOGLE_API_KEY"])
MODELO = "gemini-3.6-flash"

# --- SIDEBAR ---
with st.sidebar:
    st.header("⚙️ Config")
    estilo = st.radio("Quem responde?", ["Gauss (Rigoroso e Formal)", "Badeco (Descontraído e Direto)", "Dupla - Gauss & Badeco juntos"])
    if st.button("🗑️ Limpar conversa"):
        st.session_state.messages = []
        st.rerun()

# --- PROMPT BASE ---
def get_system_prompt(estilo):
    base = "Você é tutor de Cálculo 1. Explique limite, derivada e integral passo a passo, sem pular etapas. Use exemplos simples. Responda em PT-BR."
    if "Gauss" in estilo and "Badeco" not in estilo:
        return f"{base} Você é Carl Friedrich Gauss. Formal, elegante, rigoroso. Chame o aluno de 'meu caro'."
    elif "Badeco" in estilo and "Gauss" not in estilo:
        return f"{base} Você é o Badeco. Fala igual amigo de faculdade, gírias leves, direto ao ponto, faz analogia do dia a dia, mas a conta tem que estar 100% certa."
    else:
        return f"{base} Vocês são uma dupla: Gauss começa com a definição formal e rigorosa, depois o Badeco traduz do jeito simples e dá o macete pra prova. Se revezem."

# --- FUNÇÃO QUE CHAMA O GEMINI COM RETRY ---
def responder(pergunta, estilo):
    prompt = f"{get_system_prompt(estilo)}\n\nPergunta do aluno: {pergunta}"
    for i in range(4):
        try:
            resp = client.models.generate_content(model=MODELO, contents=prompt)
            return resp.text
        except Exception as e:
            if "503" in str(e) or "UNAVAILABLE" in str(e):
                time.sleep(2)
                continue
            return f"Erro do Google: {e}"
    return "Google lotado agora (erro 503). Tenta de novo em 30 segundos."

# --- HISTÓRICO ---
if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# --- INPUT ---
if pergunta := st.chat_input("Digite sua dúvida de Cálculo 1..."):
    st.session_state.messages.append({"role": "user", "content": pergunta})
    with st.chat_message("user"):
        st.markdown(pergunta)

    with st.chat_message("assistant"):
        with st.spinner("Gauss & Badeco pensando..."):
            resposta = responder(pergunta, estilo)
            st.markdown(resposta)

    st.session_state.messages.append({"role": "assistant", "content": resposta})
