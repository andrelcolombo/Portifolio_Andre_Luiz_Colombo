# =========================
# IMPORTS
# =========================

import streamlit as st
import requests
import base64
import os
# =========================
# CONFIG DA PÁGINA
# =========================

st.set_page_config(
    page_title="André Colombo | Data Engineer",
    layout="wide"
)

# =========================
# CONFIG GITHUB
# =========================

GITHUB_USERNAME = "andrelcolombo"  # Seu user real

# =========================
# FUNÇÃO API GITHUB
# =========================

def carregar_repos():
    url = f"https://api.github.com/users/{GITHUB_USERNAME}/repos"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        return []

# =========================
# CAMINHO DA IMAGEM
# =========================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
caminho_imagem = os.path.join(BASE_DIR, "imagens", "minha_foto.jpeg")

# =========================
# FUNÇÃO PARA CONVERTER IMAGEM
# =========================

def carregar_imagem_base64(caminho):
    with open(caminho, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

img_base64 = carregar_imagem_base64(caminho_imagem)

# =========================
# CSS PARA FOTO REDONDA NO SIDEBAR
# =========================

st.sidebar.markdown(
    f"""
    <div style="
        width:170px;
        height:170px;
        border-radius:50%;
        overflow:hidden;
        margin-left:auto;
        margin-right:auto;
    ">
        <img src="data:image/jpeg;base64,{img_base64}" 
             style="
                width:100%;
                height:100%;
                object-fit:cover;
                object-position:30% 45%;
                transform:scale(1.3);
             ">
    </div>
    """,
    unsafe_allow_html=True
)


# =========================
# MENU
# =========================

menu = st.sidebar.radio(
    "Menu",
    ["🏠 Sobre mim", "ℹ️ Informações", "📊 Projetos", "📞 Contato"]
)

if menu == "🏠 Sobre mim":

    

    # =========================
    # HEADER
    # =========================

    st.title("André Luiz Colombo")
    st.subheader("Data Engineer | ETL & Data Pipelines | Analytics")

    # =========================
    # RESUMO PROFISSIONAL (FORTE)
    # =========================

    st.write("""
    Profissional de Dados com atuação em Engenharia e Análise de Dados, 
    especializado na construção de pipelines, modelagem de dados e geração de insights estratégicos.

    Atuo no desenvolvimento de soluções end-to-end, desde a ingestão e transformação de dados 
    até a disponibilização em camadas analíticas para consumo em BI e suporte à tomada de decisão.

    Tenho experiência com grandes volumes de dados utilizando Python, SQL e Spark, 
    além de atuação em ambientes cloud.

    Meu diferencial está na capacidade de conectar engenharia de dados com analytics, 
    garantindo não apenas dados confiáveis, mas também geração de valor para o negócio.
    """)

    st.divider()

    # =========================
    # IMPACTO / ESPECIALIDADES
    # =========================

    st.header("🎯 Especialidades")

    st.write("""
    - Construção de pipelines de dados end-to-end  
    - Processos de ETL e ELT em ambientes corporativos  
    - Integração de dados (APIs, ERP, bancos relacionais)  
    - Modelagem dimensional (Star Schema)  
    - Data Quality e governança de dados  
    - Automação de processos e otimização de rotinas  
    - Preparação de dados para BI e Machine Learning  
    """)

    st.divider()

    # =========================
    # EXPERIÊNCIA (REESCRITA PROFISSIONAL)
    # =========================

    st.header("💼 Experiência Profissional")

    st.subheader("🏦 Data Engineer | Bradesco Seguros")

    st.write("""
    - Desenvolvimento e manutenção de pipelines de ingestão e transformação de dados  
    - Implementação de processos ETL/ELT com integração de múltiplas fontes (ERP, APIs, bases SQL)  
    - Aplicação de Data Quality, validação e padronização de dados  
    - Modelagem de dados e construção de datasets analíticos  
    - Automação de rotinas e otimização de processos de dados  
    - Preparação de dados para BI e projetos de machine learning  
    - Otimização de consultas SQL e melhoria de performance  
    - Governança, documentação e versionamento de dados  
    """)

    st.subheader("📊 Data Analyst | Netsupport")

    st.write("""
    - Desenvolvimento de dashboards no Looker Studio  
    - Integração de dados de múltiplas fontes  
    - Automação com Python e SQL  
    - Criação de KPIs e indicadores estratégicos  
    """)

    st.subheader("🏦 Data & Tech | Itaú Unibanco")

    st.write("""
    - Manipulação e análise de dados em larga escala  
    - Desenvolvimento e otimização de queries SQL  
    - Experiência com AWS (S3, EC2, RDS, Lambda)  
    - Automação de processos e suporte a soluções corporativas  
    - Atuação em ambiente ágil (Scrum)  
    """)

    st.divider()

    # =========================
    # STACK
    # =========================

    st.header("🚀 Stack Tecnológica")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("🧠 Data Engineering")
        st.write("""
        - Python (Pandas, PySpark)  
        - SQL Server  
        - Spark  
        - ETL / ELT  
        """)

    with col2:
        st.subheader("☁️ Cloud & Infra")
        st.write("""
        - AWS (S3, EC2, RDS, Lambda)  
        - Docker  
        - Linux  
        - Git  
        """)

    with col3:
        st.subheader("📊 Analytics")
        st.write("""
        - Power BI  
        - DAX  
        - Looker Studio  
        - Excel / VBA  
        """)

    st.divider()

    # =========================
    # POSICIONAMENTO (OURO)
    # =========================

    st.header("📌 Objetivo Profissional")

    st.write("""
    Evoluir na área de Engenharia de Dados e Arquitetura de Dados, 
    atuando na construção de soluções escaláveis, modernas e orientadas a dados, 
    com forte impacto no negócio e suporte à tomada de decisão estratégica.
    """)
    # =========================
    # FORMAÇÃO
    # =========================

    st.header("🎓 Formação Acadêmica")

    st.write("""
    🎓 Bacharelado em Engenharia de Produção  
    Universidade São Judas Tadeu  

    🎓 MBA em Data Science & Advanced Analytics  
    Impacta Tecnologia  

    🎓 Formação em Análise de Dados  
    Data Science Academy  
    """)

# =========================
# INFORMAÇÕES PROFISSIONAIS
# =========================

elif menu == "ℹ️ Informações":

    st.title("📚 Informações Profissionais")

    # =========================
    # FORMAÇÃO ACADÊMICA
    # =========================

    st.header("🎓 Formação Acadêmica")

    st.write("""
    🎓 Bacharelado em Engenharia de Produção  
    Universidade São Judas Tadeu  

    🎓 MBA em Data Science & Advanced Analytics  
    Impacta Tecnologia  
    """)

    st.divider()

    # =========================
    # CERTIFICAÇÕES (FORTES)
    # =========================

    st.header("🏅 Certificações Relevantes")

    st.write("""
    - Databricks Get Started Days (Data Engineering + SQL Analytics)  
    - Build Data Pipelines (Lakeflow / Data Engineering)  
    - Business Analytics & Machine Learning  
    - Formação Analista de Dados  
    """)

    st.divider()

    # =========================
    # CURSOS (AGRUPADOS)
    # =========================

    st.header("📚 Cursos Complementares")

    st.write("""
    Possuo diversas formações complementares voltadas para engenharia e análise de dados, incluindo:

    - Python para Análise de Dados  
    - SQL e Modelagem de Dados  
    - ETL e Pipelines de Dados  
    - Power BI e Visualização de Dados  
    - Automação de processos com Python  
    """)

    st.info("💡 Diversos cursos adicionais em plataformas como Data Science Academy e outras.")

    st.divider()

    # =========================
    # DIFERENCIAIS (OURO)
    # =========================

    st.header("🚀 Diferenciais")

    st.write("""
    - Experiência prática em ambiente corporativo (Bradesco, Itaú)  
    - Atuação end-to-end em pipelines de dados  
    - Forte integração entre Engenharia de Dados e Analytics  
    - Experiência com grandes volumes de dados  
    - Conhecimento em arquitetura de dados moderna  
    - Background em setor financeiro (alto nível de exigência)  
    """)

# =========================
# PROJETOS
# =========================

elif menu == "📊 Projetos":

    st.title("Projetos 🚀")

    st.subheader("📂 Todos os Projetos do GitHub")

    # Lista de repositórios que você NÃO quer mostrar
    repos_excluidos = [
        "aulagithub",
        "aulateste",
        "aula_csharp",
        "desafio-git",
        "desafio-merge",
        "sistema-de-cadastro"
    ]

    # Carrega os repositórios do GitHub
    repos = carregar_repos()

    # Ordena por relevância (stars)
    repos = sorted(repos, key=lambda x: x['stargazers_count'], reverse=True)

    # Loop nos repositórios
    for repo in repos:

        nome_repo = repo["name"].lower()  # normaliza para evitar erro

        # ❌ Ignora os repositórios que você não quer
        if nome_repo in repos_excluidos:
            continue

        # ❌ Ignora forks
        if repo["fork"]:
            continue

        # ❌ Ignora projetos sem descrição
        if repo["description"] is None:
            continue

        # =========================
        # EXIBE PROJETO
        # =========================

        nome = repo["name"]
        descricao = repo["description"]
        url = repo["html_url"]
        linguagem = repo["language"]

        st.markdown(f"### 🔹 {nome}")

        st.write(descricao)

        # Linguagem (importante)
        if linguagem:
            st.write(f"🛠️ {linguagem}")

        st.markdown(f"[🔗 Ver repositório]({url})")

        st.divider()
# =========================
# CONTATO
# =========================

elif menu == "📞 Contato":

    st.title("Contato 📬")

    st.markdown("""
    - 📧 andre-luiz-colombo@outlook.com  
    - 🐙 https://github.com/andrelcolombo  
    - 🔗 https://www.linkedin.com/in/andrelcolombo/  
    - 📱 (11) 96917-7343  
    - 🏢 São Paulo, SP        
    """)

    nome = st.text_input("Nome")
    msg = st.text_area("Mensagem")

    if st.button("Enviar"):
        st.success(f"Valeu, {nome}! 🚀")