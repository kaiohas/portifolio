import streamlit as st

def section_title(title, icon):
    st.header(f"{icon} {title}", divider="rainbow")

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="Portfólio | Kaio Alves",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- CABEÇALHO ---
col1, col2 = st.columns([1, 2.5], gap="large")

with col1:
    st.image("assets/profile.jpg", caption="Kaio Alves", use_container_width=True)

with col2:
    st.title("Olá, eu sou o Kaio Alves 👋")
    st.subheader("Especialista de Dados | Engenharia, BI e Aplicações end-to-end")
    st.write(
        "Desenvolvo soluções de dados de ponta a ponta, "
        "desde a criação de pipelines e dashboards até o desenvolvimento de aplicações web interativas."
    )
    st.write("📍 Baseado em Uberlândia, MG (Brasil)")

    # --- CONTATOS E LINKS ---
    st.write(
        "**Celular**: [11 91069-0905](tel:+5511910690905) | "
        "**Email**: [kaiohas@hotmail.com](mailto:kaiohas@hotmail.com) | "
        "**LinkedIn**: [kaiohalves](https://www.linkedin.com/in/kaiohalves/) | "
        "**GitHub**: [kaiohas](https://github.com/kaiohas)"
    )

st.divider()

# --- SOBRE MIM ---
section_title("Sobre Mim", "👤")
st.markdown(
    """
    Especialista de Dados com 13+ anos de experiência, atuando do contact center ao agronegócio — sempre na ponte entre dados brutos e decisão de negócio.
    Hoje na Vertem, lidero soluções de dados para o segmento Agro, do pipeline de ingestão (Databricks, Spark) até o dashboard que o board usa pra decidir.
    Tenho perfil end-to-end: penso a arquitetura, construo o ETL, modelo no Power BI e ainda escrevo a aplicação que entrega isso pro usuário final.
    Como prestador de serviço, também sou a referência de relacionamento com o cliente contratante. Manter uma boa experiência pra quem está do outro lado da mesa não é um extra — é parte de como eu trabalho.
    """
)

st.divider()

# --- NAVEGAÇÃO RÁPIDA ---
section_title("Navegue", "🧭")

nav_items = [
    ("pages/2_📊_PowerBI.py", "📊", "Projetos Power BI", "Dashboards e relatórios interativos desenvolvidos no Power BI"),
    ("pages/3_🧰_Apps.py", "🧰", "Apps", "Aplicações web e mobile construídas do zero"),
    ("pages/4_📝_Estudos.py", "📝", "Estudos & Análises", "Análises exploratórias e estudos de dados"),
]

for col, (page, icon, label, desc) in zip(st.columns(3, gap="large"), nav_items):
    with col:
        with st.container(border=True):
            st.markdown(f"<div style='font-size:2.5rem; text-align:center; padding:0.5rem 0'>{icon}</div>", unsafe_allow_html=True)
            st.markdown(f"<p style='text-align:center; font-weight:700; font-size:1.05rem; margin-bottom:0.25rem'>{label}</p>", unsafe_allow_html=True)
            st.markdown(f"<p style='text-align:center; font-size:0.85rem; opacity:0.7; margin-bottom:0.5rem'>{desc}</p>", unsafe_allow_html=True)
            st.page_link(page, label="Acessar →", icon=icon)

st.divider()

# --- PRINCIPAIS COMPETÊNCIAS ---
section_title("Principais Competências", "🛠️")
col_skills_1, col_skills_2, col_skills_3 = st.columns(3)

with col_skills_1:
    st.subheader("Cloud & Engenharia de Dados")
    st.markdown("""
    - **Cloud:** Azure, AWS
    - **Plataformas:** Databricks (AWS + Azure), Apache Spark
    - **Bancos de Dados:** SQL Server, MySQL, NoSQL
    - **Orquestração:** Azure Data Factory, pipelines ETL/ELT em Python e SQL
    """)

with col_skills_2:
    st.subheader("BI & Analytics")
    st.markdown("""
    - **BI:** Power BI (DAX, Power Query), Metabase
    - **Analytics:** Google Analytics
    - **CRM/ERP:** Salesforce, SAP
    """)

with col_skills_3:
    st.subheader("Desenvolvimento")
    st.markdown("""
    - **Linguagens:** Python, SQL
    - **Frameworks Web:** Streamlit, Flask, Django
    - **Ambientes:** Jupyter, Google Colab
    - **Idiomas:** Inglês Avançado (Influx)
    """)

st.divider()

# --- CERTIFICAÇÕES ---
section_title("Certificações", "🎓")
st.markdown(
    """
    - Databricks Certified Data Analyst Associate
    - Databricks Platform Administrator
    - Databricks Generative AI Fundamentals
    - Formação Engenharia de Dados — Alura
    - Apache Spark — Alura
    """
)

st.divider()

# --- EXPERIÊNCIA EM DESTAQUE ---
section_title("Experiência em Destaque", "🚀")
st.markdown(
    """
    - **Engenharia de Dados:** Construção e orquestração de pipelines ETL/ELT em Databricks/Spark processando dados de múltiplos segmentos de negócio para o cliente Agro.
    - **Business Intelligence:** Definição e acompanhamento de KPIs estratégicos via dashboards em Power BI, usados na tomada de decisão executiva.
    - **Soluções Full-Stack de Dados:** Criação de aplicações internas com Streamlit, Flask e Django — do dado bruto à interface de uso.
    - **13 anos, 7 segmentos:** Trajetória passando por Contact Center, Cadeia de Suprimentos, Royalties, E-commerce, Fidelidade, Bancário e Agronegócio — visão ampla de como dados resolvem problemas diferentes.
    """
)
