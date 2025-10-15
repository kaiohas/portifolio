import streamlit as st
import yaml
from components.ui import inject_css, section_title


st.page_link("pages/1_🏠_Home.py", label="Home", icon="🏠")
st.set_page_config(page_title="Portfólio | Power BI", page_icon="📊", layout="wide",initial_sidebar_state="collapsed")
inject_css()

st.title("📊 Projetos Power BI")
st.caption("Espaço para apresentação de projetos desenvolvidos com Power BI.")

# Ajuda rápida
# with st.expander("Como adicionar um novo relatório?"):
#     st.markdown("""
#     1. No Power BI Service, use **Arquivo → Inserir relatório → Publicar na Web** e copie o **iframe** ou a URL pública.
#     2. Edite o arquivo `data/powerbi.yaml` e inclua um item com `titulo`, `descricao` e `url_iframe`.
#     3. Recarregue esta página.
#     """)

# Carrega lista
with open("data/powerbi.yaml", "r", encoding="utf-8") as f:
    data = yaml.safe_load(f) or {}
relatorios = data.get("relatorios", [])

if not relatorios:
    st.info("Nenhum relatório cadastrado em `data/powerbi.yaml`.")
else:
    for r in relatorios:
        st.subheader(r.get("titulo", "Sem título"))
        if r.get("descricao"):
            st.caption(r["descricao"])
        url_iframe = r.get("url_iframe")
        if url_iframe:
            st.components.v1.iframe(url_iframe, height=600)
        st.divider()


