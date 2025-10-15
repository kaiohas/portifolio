import streamlit as st
import yaml
from components.ui import inject_css, card, section_title

st.page_link("pages/1_🏠_Home.py", label="Home", icon="🏠")
st.set_page_config(page_title="Portfólio | Apps", page_icon="🧰", layout="wide",initial_sidebar_state="collapsed")
inject_css()
st.title("🧰 Apps desenvolvidos")

with open("data/apps.yaml", "r", encoding="utf-8") as f:
    data = yaml.safe_load(f) or {}
apps = data.get("apps", [])

if not apps:
    st.info("Nenhum app cadastrado em `data/apps.yaml`.")
else:
    cols = st.columns(2, gap="large")
    for i, app in enumerate(apps):
        with cols[i % 2]:
            links = [(lbl, url) for lbl, url in app.get("links", [])]
            card(
                title=app.get("titulo", "Sem título"),
                subtitle=app.get("resumo"),
                image=app.get("imagem"),
                body=app.get("detalhes"),
                tags=app.get("tags", []),
                links=links,
            )
