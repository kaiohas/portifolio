import streamlit as st

# CSS global leve
def inject_css():
    st.markdown(
        """
        <style>
        .app-card {
            border-radius: 16px;
            padding: 1rem;
            background: rgba(255,255,255,0.03);
            border: 1px solid rgba(255,255,255,0.08);
            box-shadow: 0 10px 30px rgba(0,0,0,0.25);
        }
        .tag {
            display:inline-block;
            padding: 2px 10px;
            border:1px solid rgba(255,255,255,0.15);
            border-radius: 999px;
            margin-right: 6px;
            margin-bottom: 6px;
            font-size: 12px;
            opacity:.9;
        }
        .muted { opacity:.8; font-size: 0.95rem; }
        .grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
            gap: 16px;
            align-items: start;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

def _is_video(path_or_url: str) -> bool:
    # formatos suportados diretamente pelo st.video
    exts = (".mp4", ".mov", ".webm")
    p = path_or_url.lower()
    return any(p.endswith(ext) for ext in exts)

def _is_image(path_or_url: str) -> bool:
    exts = (".gif", ".png", ".jpg", ".jpeg", ".webp")
    p = path_or_url.lower()
    return any(p.endswith(ext) for ext in exts)

def card(title, subtitle=None, image=None, body=None, tags=None, links=None):
    """
    Renderiza um 'cartão' de projeto/estudo.

    Parâmetros:
      - title (str): título do card.
      - subtitle (str, opcional): subtítulo/caption.
      - image (str, opcional): caminho local (ex.: 'assets/demo.mp4' ou 'assets/img.png')
                               ou URL direta para arquivo (ex.: raw GitHub).
                               Se for vídeo (.mp4/.mov/.webm), usa st.video.
                               Se for imagem (.gif/.png/.jpg/.jpeg/.webp), usa st.image.
      - body (str, opcional): texto em Markdown.
      - tags (list[str], opcional): lista de tags.
      - links (list[tuple[str,str]], opcional): pares (label, url) para botões.
    """
    with st.container(border=False):
        st.markdown('<div class="app-card">', unsafe_allow_html=True)

        # mídia (vídeo ou imagem)
        if image:
            if _is_video(image):
                st.video(image)
            elif _is_image(image):
                # GIF entra aqui também (anima automaticamente)
                st.image(image, use_container_width=True)
            else:
                # fallback: tenta exibir como imagem; se não renderizar, ignora
                try:
                    st.image(image, use_container_width=True)
                except Exception:
                    pass

        st.subheader(title)
        if subtitle:
            st.caption(subtitle)
        if body:
            st.markdown(body)

        if tags:
            st.markdown(
                " ".join([f"<span class='tag'>{t}</span>" for t in tags]),
                unsafe_allow_html=True
            )

        if links:
            cols = st.columns(len(links))
            for i, (label, url) in enumerate(links):
                cols[i].link_button(label, url)

        st.markdown('</div>', unsafe_allow_html=True)

def section_title(title, emoji=""):
    st.markdown(f"### {emoji} {title}")
