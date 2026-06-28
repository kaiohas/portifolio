import streamlit as st
import yaml
from components.ui import inject_css

st.set_page_config(page_title="Portfólio | Apps", page_icon="🧰", layout="wide", initial_sidebar_state="collapsed")
inject_css()

st.page_link("pages/1_🏠_Home.py", label="← Voltar para Home", icon="🏠")
st.title("🧰 Apps desenvolvidos")
st.caption("Aplicações construídas do zero — da modelagem de dados à interface final.")

st.divider()

with open("data/apps.yaml", "r", encoding="utf-8") as f:
    data = yaml.safe_load(f) or {}
apps = data.get("apps", [])


def render_stack(tags: list):
    if tags:
        st.markdown(
            " ".join([f"<span class='tag'>{t}</span>" for t in tags]),
            unsafe_allow_html=True,
        )


def render_media(imagem):
    if not imagem:
        st.info("📹 Gravação em breve.", icon="🎬")
        return
    ext = imagem.lower()
    if ext.endswith((".mp4", ".mov", ".webm")):
        st.video(imagem)
    else:
        st.image(imagem, use_container_width=True)


def render_funcionalidades(items: list):
    if items:
        for f in items:
            st.markdown(f"- {f}")


if not apps:
    st.info("Nenhum app cadastrado em `data/apps.yaml`.")
else:
    for i, app in enumerate(apps):
        titulo = app.get("titulo", "Sem título")
        resumo = app.get("resumo", "")
        stack = app.get("stack", [])
        modulos = app.get("modulos")

        with st.expander(f"🧰 {titulo}", expanded=(i == 0)):
            st.markdown(f"_{resumo}_")
            st.write("")

            if modulos:
                tab_labels = [f"{m.get('icone', '')} {m.get('nome', '')}" for m in modulos]
                tabs = st.tabs(tab_labels)

                for tab, modulo in zip(tabs, modulos):
                    with tab:
                        col_media, col_info = st.columns([1.4, 1], gap="large")
                        with col_media:
                            render_media(modulo.get("imagem"))
                        with col_info:
                            st.markdown(f"**{modulo.get('descricao', '')}**")
                            st.write("")
                            render_funcionalidades(modulo.get("funcionalidades", []))
            else:
                col_media, col_info = st.columns([1.4, 1], gap="large")
                with col_media:
                    render_media(app.get("imagem"))
                with col_info:
                    render_funcionalidades(app.get("funcionalidades", []))

            st.write("")
            render_stack(stack)
