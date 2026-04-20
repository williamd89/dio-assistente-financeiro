import streamlit as st
import json
import os
import time
from dotenv import load_dotenv
from openai import OpenAI
from datetime import datetime

# =========================
# CONFIG
# =========================
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
LOG_DIR = os.path.join(BASE_DIR, "logs")

os.makedirs(LOG_DIR, exist_ok=True)

# =========================
# LOAD DATA
# =========================
with open(os.path.join(DATA_DIR, "perfil_investidor.json"), encoding="utf-8") as f:
    perfis = json.load(f)

with open(os.path.join(DATA_DIR, "produtos_financeiros.json"), encoding="utf-8") as f:
    produtos = json.load(f)

# =========================
# IA FUNÇÕES
# =========================
def identificar_perfil(risco):
    return {
        "baixo": "🟢 Conservador",
        "medio": "🟡 Moderado",
        "alto": "🔴 Arrojado"
    }.get(risco, None)

def gerar_resposta(user_input, contexto):
    system_prompt = f"""
Você é um assistente financeiro educativo.

REGRAS:
- NÃO recomendar diretamente
- NÃO dizer "invista em"
- Explicar com clareza
- Usar bullet points
- Linguagem simples
- Sempre educativo

Perfil:
{contexto}
"""
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_input}
        ]
    )
    return response.choices[0].message.content

def gerar_titulo(pergunta):
    try:
        r = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role":"user","content":f"Título curto (máx 5 palavras): {pergunta}"}]
        )
        return r.choices[0].message.content.strip()
    except:
        return "Nova conversa"

def gerar_resumo(chat):
    try:
        texto = "\n".join([m for r,m in chat if r=="user"])
        r = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role":"user","content":f"Resumo em 1 frase:\n{texto}"}]
        )
        return r.choices[0].message.content.strip()
    except:
        return ""

# =========================
# LOGS
# =========================
def gerar_id():
    return datetime.now().strftime("chat_%Y-%m-%d_%H%M%S")

def salvar_chat(chat_id, chat, contexto, fixado=False, titulo=None):
    path = os.path.join(LOG_DIR, f"{chat_id}.json")

    if not titulo and chat:
        titulo = gerar_titulo(chat[0][1])

    resumo = gerar_resumo(chat)

    data = {
        "id": chat_id,
        "titulo": titulo,
        "resumo": resumo,
        "fixado": fixado,
        "contexto": contexto,
        "chat": [{"role":r,"msg":m} for r,m in chat]
    }

    with open(path,"w",encoding="utf-8") as f:
        json.dump(data,f,indent=4,ensure_ascii=False)

def carregar_chat(chat_id):
    path = os.path.join(LOG_DIR, f"{chat_id}.json")

    if os.path.exists(path):
        with open(path, encoding="utf-8") as f:
            d = json.load(f)

            # compatibilidade com versão antiga
            if "chat" not in d and "conversa" in d:
                d["chat"] = [
                    {"role": c["role"], "msg": c["mensagem"]}
                    for c in d["conversa"]
                ]

            return d

    return None

def listar():
    chats = []

    for f in os.listdir(LOG_DIR):
        if f.endswith(".json"):
            with open(os.path.join(LOG_DIR, f), encoding="utf-8") as file:
                d = json.load(file)

                chats.append({
                    # fallback inteligente
                    "id": d.get("id", f.replace(".json", "")),
                    "titulo": d.get("titulo", "Conversa"),
                    "fixado": d.get("fixado", False)
                })

    chats.sort(key=lambda x: (not x["fixado"], x["id"]), reverse=True)
    return chats

def deletar(chat_id):
    os.remove(os.path.join(LOG_DIR,f"{chat_id}.json"))

def renomear(chat_id,novo):
    path=os.path.join(LOG_DIR,f"{chat_id}.json")
    d=carregar_chat(chat_id)
    d["titulo"]=novo
    with open(path,"w",encoding="utf-8") as f:
        json.dump(d,f,indent=4,ensure_ascii=False)

def fixar(chat_id,status):
    path=os.path.join(LOG_DIR,f"{chat_id}.json")
    d=carregar_chat(chat_id)
    d["fixado"]=status
    with open(path,"w",encoding="utf-8") as f:
        json.dump(d,f,indent=4,ensure_ascii=False)

# =========================
# SESSION
# =========================
if "chat" not in st.session_state:
    st.session_state.chat=[]
if "chat_id" not in st.session_state:
    st.session_state.chat_id=gerar_id()

# =========================
# UI
# =========================
st.set_page_config(layout="wide")
st.title("💰 Assistente Financeiro IA")

st.markdown("""
<style>
.chat-title {
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    max-width: 180px;
}
</style>
""", unsafe_allow_html=True)

if "editando" not in st.session_state:
    st.session_state.editando = None
    
# =========================
# SIDEBAR PERFIL
# =========================
st.sidebar.header("📊 Perfil")

objetivo = st.sidebar.selectbox("Objetivo",["Selecionar...","Segurança","Equilíbrio","Retorno"])
prazo = st.sidebar.selectbox("Prazo",["Selecionar...","Curto","Médio","Longo"])
risco = st.sidebar.selectbox("Risco",["Selecionar...","baixo","medio","alto"])
experiencia = st.sidebar.selectbox("Experiência",["Selecionar...","iniciante","intermediario","avancado"])

perfil_ok = all(x!="Selecionar..." for x in [objetivo,prazo,risco,experiencia])
perfil = identificar_perfil(risco) if perfil_ok else None

st.sidebar.markdown(f"### 🧠 {perfil if perfil else 'Não definido'}")

# =========================
# HISTÓRICO
# =========================
st.sidebar.markdown("---")
st.sidebar.header("📜 Histórico")

busca = st.sidebar.text_input("🔍 Buscar")

for c in listar():
    if busca and busca.lower() not in c["titulo"].lower():
        continue

    col1, col2 = st.sidebar.columns([5,1])

    # =========================
    # MODO EDIÇÃO
    # =========================
    if st.session_state.editando == c["id"]:
        novo_nome = col1.text_input(
            "",
            value=c["titulo"],
            key=f"edit_{c['id']}"
        )

        if col1.button("Salvar", key=f"save_{c['id']}"):
            renomear(c["id"], novo_nome)
            st.session_state.editando = None
            st.rerun()

    else:
        # =========================
        # TÍTULO (CLIQUE NORMAL)
        # =========================
        if col1.button(
            ("📌 " if c["fixado"] else "") + c["titulo"],
            key=c["id"]
        ):
            dados = carregar_chat(c["id"])
            st.session_state.chat = [(i["role"], i["msg"]) for i in dados["chat"]]
            st.session_state.chat_id = c["id"]

        # =========================
        # MENU (...)
        # =========================
        if col2.button("⋯", key=f"menu_{c['id']}"):
            st.session_state.editando = c["id"]

    # =========================
    # AÇÕES EXTRAS
    # =========================
    colA, colB = st.sidebar.columns(2)

    if colA.button("📌", key=f"pin_{c['id']}"):
        fixar(c["id"], not c["fixado"])
        st.rerun()

    if colB.button("🗑️", key=f"del_{c['id']}"):
        deletar(c["id"])
        st.rerun()

# =========================
# PERGUNTAS RÁPIDAS
# =========================
st.markdown("### 💡 Perguntas rápidas")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("💬 Melhor investimento"):
        st.session_state.input = "Qual o melhor investimento?"

with col2:
    if st.button("🛡️ Investimento seguro"):
        st.session_state.input = "Quero investir com segurança"

with col3:
    if st.button("📈 Maior retorno"):
        st.session_state.input = "Quero investir buscando maior retorno"

# =========================
# CHAT
# =========================
if "input" in st.session_state:
    user_input = st.session_state.input
    del st.session_state.input
else:
    user_input = st.chat_input("Digite...")

if user_input:
    st.session_state.chat.append(("user",user_input))

    for r,m in st.session_state.chat:
        with st.chat_message("user" if r=="user" else "assistant"):
            st.markdown(m)

    with st.chat_message("assistant"):
        ph=st.empty()
        ph.markdown("⏳ Pensando...")

        if not perfil_ok:
            resp="Preencha o perfil 👈"
        else:
            resp=gerar_resposta(user_input,f"Perfil: {perfil}")

        txt=""
        for c in resp:
            txt+=c
            ph.markdown(txt)
            time.sleep(0.005)

    st.session_state.chat.append(("bot",resp))

    salvar_chat(st.session_state.chat_id,st.session_state.chat,f"Perfil:{perfil}")

else:
    for r,m in st.session_state.chat:
        with st.chat_message("user" if r=="user" else "assistant"):
            st.markdown(m)

st.caption("⚠️ Educativo — não é recomendação financeira")