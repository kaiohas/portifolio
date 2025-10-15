import streamlit as st

# A função `section_title` e `inject_css` não são padrão do Streamlit.
# Para que o código funcione de forma independente, criei uma função similar aqui.
# Você pode substituir pela sua implementação original.
def section_title(title, icon):
    st.header(f"{icon} {title}", divider="rainbow")

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="Portfólio | Kaio Siqueira",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Se você tiver um arquivo CSS customizado, pode injetá-lo.
# with open("style.css") as f:
#     st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# --- CABEÇALHO ---
col1, col2 = st.columns([1, 2.5], gap="large")

with col1:
    # Use um caminho para uma imagem acessível ou faça upload dela
    st.image("assets/profile.jpg", caption="Kaio Henrique Alves Siqueira", use_container_width=True)

with col2:
    st.title("Olá, eu sou o Kaio Henrique 👋")
    st.subheader("Especialista de Dados | Python & Cloud Developer")
    st.write(
        "Desenvolvo soluções de dados de ponta a ponta, "
        "desde a criação de pipelines e dashboards até o desenvolvimento de aplicações web interativas."
    )
    st.write("📍 Baseado em Uberlândia, MG (Brasil)")

    # --- CONTATOS E LINKS ---
    st.write(
        "**Celular**: [11 91069-0905](tel:+5511910690905) | "
        "**Email**: [kaio.alves123@gmail.com](mailto:kaio.alves123@gmail.com) | "
        "**LinkedIn**: [kaiohalves](https://www.linkedin.com/in/kaiohalves/) | "
        "**GitHub**: [kaiohas](https://github.com/kaiohas)"
    )

st.divider()

# --- SOBRE MIM ---
section_title("Sobre Mim", "👤")
st.markdown(
    """
    Sou um especialista de dados apaixonado por transformar problemas de negócio em soluções eficientes e orientadas a dados. 
    Com uma base sólida em Engenharia de Dados e Business Intelligence, meu objetivo é criar ferramentas que não apenas informem, mas também capacitem as equipes a tomarem as melhores decisões.
    Tenho um perfil proativo e busco constantemente aprender e aplicar novas tecnologias para otimizar processos e gerar valor real.
    """
)

st.divider()

# --- PRINCIPAIS COMPETÊNCIAS ---
section_title("Principais Competências", "🛠️")
col_skills_1, col_skills_2, col_skills_3 = st.columns(3)

with col_skills_1:
    st.subheader("Cloud & Dados")
    st.markdown("""
    - **Cloud:** Azure, AWS
    - **Plataformas:** Databricks
    - **Bancos de Dados:** SQL (SQL Server, MySQL), NoSQL
    - **Ferramentas ETL:** Pipelines em Python e SQL
    """)

with col_skills_2:
    st.subheader("BI & Visualização")
    st.markdown("""
    - **BI:** Power BI, DAX, Power Query
    - **Analytics:** Google Analytics
    - **CRM/ERP:** Salesforce, SAP
    - **Marketing:** Oracle Responsys, Ad Manager
    """)

with col_skills_3:
    st.subheader("Desenvolvimento")
    st.markdown("""
    - **Linguagens:** Python, SQL
    - **Frameworks Web:** Streamlit, Flask, Django
    - **Ambientes:** Colab, Jupyter Notebooks
    - **Idiomas:** Inglês (Avançado - Influx)
    """)

st.divider()

# --- EXPERIÊNCIA EM DESTAQUE ---
section_title("Experiência em Destaque", "🚀")
st.markdown(
    """
    - **Desenvolvimento de Soluções de Dados:** Criação de aplicações e sites interativos com Streamlit, Flask e Django para visualização e manipulação de dados.
    - **Business Intelligence:** Construção de dashboards e relatórios gerenciais em Power BI, com foco na definição e acompanhamento de KPIs estratégicos.
    - **Engenharia de Dados:** Desenvolvimento e orquestração de pipelines de dados robustos (ETL/ELT) utilizando Python, SQL, e Databricks para processar grandes volumes de informação.
    - **Análise Multissetorial:** Experiência na análise e construção de indicadores para diversos segmentos, incluindo **Agronegócio, Bancário, Marketing, Pesquisa Clínica, Varejo, Programas de Fidelidade e Contact Centers**.
    """
)


# --- NAVEGAÇÃO RÁPIDA (Exemplo) ---

st.divider()
section_title("Navegue", "🧭")
colA, colB, colC = st.columns(3)
with colA:
    st.page_link("pages/2_📊_PowerBI.py", label="Projetos Power BI", icon="📊")
with colB:
    st.page_link("pages/3_🧰_Apps.py", label="Apps", icon="🧰")
with colC:
    st.page_link("pages/4_📝_Estudos.py", label="Estudos & Análises", icon="📝")
