import streamlit as st
import yaml
from components.ui import inject_css

st.set_page_config(page_title="Portfólio | Estudos & Análises", page_icon="📝", layout="wide", initial_sidebar_state="collapsed")
inject_css()

st.page_link("pages/1_🏠_Home.py", label="← Voltar para Home", icon="🏠")
st.title("📝 Análises e Estudos")
st.markdown("Entregáveis reais de projetos de dados — do problema de negócio ao resultado mensurável.")

st.divider()

with open("data/estudos.yaml", "r", encoding="utf-8") as f:
    data = yaml.safe_load(f) or {}
estudos = data.get("estudos", [])


def badge_status(status: str) -> str:
    s = status.lower()
    if "produção" in s:
        cor = "#22c55e"
    elif "desenvolvimento" in s:
        cor = "#f59e0b"
    else:
        cor = "#60a5fa"
    return (
        f"<span style='background:{cor}18; color:{cor}; border:1px solid {cor}55; "
        f"border-radius:999px; padding:2px 12px; font-size:12px; font-weight:600'>{status}</span>"
    )


def badge_tipo(tipo: str) -> str:
    return (
        f"<span style='background:rgba(255,255,255,0.06); color:inherit; "
        f"border:1px solid rgba(255,255,255,0.18); border-radius:999px; "
        f"padding:2px 12px; font-size:12px'>{tipo}</span>"
    )


def render_stack(stack: dict):
    linhas = []
    labels = {
        "fontes": "Fontes",
        "janela": "Janela",
        "volume": "Volume",
        "processamento": "Processamento",
        "entregavel": "Entregável",
    }
    for key, label in labels.items():
        if stack.get(key):
            linhas.append(f"**{label}:** {stack[key]}")
    st.markdown("\n\n".join(linhas))


def render_card(estudo: dict):
    with st.container(border=True):
        st.markdown(badge_tipo(estudo.get("tipo", "")), unsafe_allow_html=True)
        st.markdown(f"### {estudo.get('titulo', '')}")
        st.markdown(estudo.get("resumo", ""))

        with st.expander("Ver detalhes"):
            st.markdown("#### 🔍 O problema")
            st.markdown(estudo.get("problema", ""))

            st.markdown("#### 🔧 Como foi resolvido")
            st.markdown(estudo.get("solucao", ""))

            st.markdown("#### 💡 Achados / valor gerado")
            st.markdown(estudo.get("achados", ""))

            st.markdown("#### 📋 Ficha técnica")
            render_stack(estudo.get("stack", {}))


if not estudos:
    st.info("Nenhum estudo cadastrado em `data/estudos.yaml`.")
else:
    tipos_ordenados = ["Segmentação", "Score Composto", "Estudo", "Produtificação"]
    tab_labels = ["Todos"] + tipos_ordenados
    tabs = st.tabs(tab_labels)

    for tab, filtro in zip(tabs, tab_labels):
        with tab:
            lista = estudos if filtro == "Todos" else [e for e in estudos if e.get("tipo") == filtro]
            for estudo in lista:
                render_card(estudo)
                st.write("")

st.divider()
st.caption(
    "⚠️ Os dados apresentados foram generalizados para preservar confidencialidade contratual. "
    "Valores absolutos, nomes de clientes e identificadores foram omitidos ou aproximados."
)
