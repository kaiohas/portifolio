# Portfólio em Streamlit

Um app simples de portfólio para exibir **Home**, **projetos Power BI**, **apps** e **estudos/análises**.

## Como rodar
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

pip install -r requirements.txt
streamlit run app.py
```

## Onde editar
- **Home:** edite `pages/1_🏠_Home.py` (foto, contatos, sobre).
- **Power BI:** adicione/edite relatórios em `data/powerbi.yaml`.
- **Apps:** ajuste os cartões em `data/apps.yaml` e coloque imagens em `assets/`.
- **Estudos/Análises:** descreva itens em `data/estudos.yaml` com links e imagens.

## Deploy (opcionais)
- **Streamlit Community Cloud:** subir este repositório no GitHub e conectar em https://streamlit.io/cloud
- **Railway/Fly.io/Render:** usar `streamlit run app.py` como comando de start.
