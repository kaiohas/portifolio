import streamlit as st
import yaml
from components.ui import inject_css, section_title

st.set_page_config(page_title="Portfólio | Power BI", page_icon="📊", layout="wide", initial_sidebar_state="collapsed")
inject_css()

st.page_link("pages/1_🏠_Home.py", label="← Voltar para Home", icon="🏠")

st.title("📊 Projetos Power BI")
st.caption("Clique em um painel para expandir e visualizar o relatório interativo.")

st.divider()

with open("data/powerbi.yaml", "r", encoding="utf-8") as f:
    data = yaml.safe_load(f) or {}
relatorios = data.get("relatorios", [])

if not relatorios:
    st.info("Nenhum relatório cadastrado em `data/powerbi.yaml`.")
else:
    for i, r in enumerate(relatorios):
        titulo = r.get("titulo", "Sem título")
        descricao = r.get("descricao", "")
        url_iframe = r.get("url_iframe")

        with st.expander(f"📊 {titulo}", expanded=(i == 0)):
            if descricao:
                st.markdown(f"_{descricao}_")
                st.write("")
            if url_iframe:
                st.components.v1.iframe(url_iframe, height=600, scrolling=True)
            else:
                st.warning("URL do relatório não configurada.")
