import streamlit as st
import yaml
from components.ui import inject_css, card

st.page_link("pages/1_🏠_Home.py", label="Home", icon="🏠")
st.set_page_config(page_title="Portfólio | Estudos", page_icon="📝", layout="wide",initial_sidebar_state="collapsed")
inject_css()
st.title("📝 Estudos & Análises")

with open("data/estudos.yaml", "r", encoding="utf-8") as f:
    data = yaml.safe_load(f) or {}
itens = data.get("itens", [])

if not itens:
    st.info("Nenhum estudo cadastrado em `data/estudos.yaml`.")
else:
    for item in itens:
        links = [(lbl, url) for lbl, url in item.get("links", [])]
        card(
            title=item.get("titulo", "Sem título"),
            subtitle=item.get("resumo"),
            image=item.get("imagem"),
            body=item.get("texto_md"),
            tags=item.get("tags", []),
            links=links,
        )
        st.divider()
