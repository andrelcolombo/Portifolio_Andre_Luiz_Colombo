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
    page_title="Portfólio - André Luiz Colombo",
    page_icon="⚙️",
    layout="wide",
    initial_sidebar_state="expanded"
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
caminho_logo_github = os.path.join(BASE_DIR, "imagens", "logotipo-do-github.png")

# =========================
# FUNÇÃO PARA CONVERTER IMAGEM
# =========================

def carregar_imagem_base64(caminho):
    with open(caminho, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

img_base64 = carregar_imagem_base64(caminho_imagem)
logo_github_base64 = carregar_imagem_base64(caminho_logo_github)

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

    st.divider()
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
             
    🎓 Formação em Ciência de Dados  
    Data Science Academy  
    """)

    st.divider()

    # =========================
    # QUEM É O ANDRÉ (LADO PESSOAL)
    # =========================

    st.header("👤 Além dos Pipelines: Quem é o André?")

    col_text, col_hobbies = st.columns([2, 1])

    with col_text:
        st.write("""
        Se você me perguntar por que escolhi a Engenharia, a resposta não começa com números, mas com **ronco de motores**. 🏎️ 
        
        Sou um apaixonado por carros desde cedo, o que me levou a cursar Engenharia de Produção para entender como grandes máquinas e processos complexos ganham vida. Essa curiosidade mecânica acabou migrando para o mundo digital: hoje, em vez de motores, eu projeto **arquiteturas de dados**.
        
        Fora do trabalho, você provavelmente vai me encontrar:
        - **Explorando novos setups:** Sou fascinado por eletrônicos e hardware. Se tem uma tecnologia nova saindo, eu quero entender como funciona.
        - **No mundo dos Games:** Onde exercito minha estratégia e reflexos (e claro, admiro o trabalho de engenharia por trás dos gráficos).
        - **Me atualizando:** O mundo tech não para, e minha sede por aprender coisas novas é o que me mantém em movimento.
        """)

    with col_hobbies:
        # Um pequeno card visual com ícones das suas paixões
        with st.container(border=True):
            st.markdown("### My Gear & Passions")
            st.write("🏎️ Motorsports")
            st.write("🎮 Gaming Culture")
            st.write("🔌 Gadgets & Tech")
            st.write("🚀 Continuous Learning")

    st.divider()

# =========================
# INFORMAÇÕES PROFISSIONAIS
# =========================

elif menu == "ℹ️ Informações":
    st.title("📚 Informações Profissionais")

    # =========================
    # FORMAÇÃO ACADÊMICA
    # =========================
    st.header("🎓 Formação Acadêmica")
    
    with st.expander("🎓 Graduação", expanded=True):
        st.markdown("""
        - **Bacharelado em Engenharia de Produção** - *Universidade São Judas Tadeu*
        - **MBA em Data Science & Advanced Analytics** - *Impacta Tecnologia*
        """)
    

    st.divider()

    # =========================
    # CERTIFICAÇÕES (ORGANIZADAS POR EXPANDERS)
    # =========================
    st.header("🏅 Especializações e Certificações")
    st.caption("Clique nos grupos para expandir ou recolher as informações.")

    with st.expander("🏆 Formações Principais (Master)", expanded=True):
        st.markdown("""
        - **Formação Cientista de Dados 4.0** - *Data Science Academy*
        - **Formação Analista de Dados 4.0** - *Data Science Academy*
        """)

    with st.expander("⚙️ Engenharia de Dados, Cloud & Automação", expanded=True):
        st.markdown("""
        - **IA Generativa e Agentes de IA Para Fluxos de Automação com Langflow e n8n**
        - **SQL Server Integration Services (SSIS) - ETL Avançado** 
        - **Build Data Pipelines** (Lakeflow / Data Engineering)
        - **Pipelines de Dados com Google BigQuery**
        - **Fundamentos de Engenharia de Dados**
        - **Databricks Get Started Days** (Data Engineering + SQL Analytics)
        - **Cloud Computing & Data Science** (Amazon SageMaker e Microsoft Fabric)
        """)

    with st.expander("📊 Business Intelligence & Analytics", expanded=True):
        st.markdown("""
        - **AI/BI for Data Analysts** (Databricks)
        - **Power BI: DAX contextos e iteração**
        - **Modelagem e Análise de Dados com Power BI**
        - **Looker Studio: Visualização de Dados**
        - **Microsoft Power BI para Business Intelligence e Data Science**
        - **SQL Para Análise de Dados e Data Science**
        - **Projetos de Análise de Dados com Linguagem Python**
        - **Storytelling e Dashboards de Alto Impacto**
        """)

    with st.expander("🧠 Data Science, Estatística & ML", expanded=True):
        st.markdown("""
        - **Business Analytics & Machine Learning para Projetos**
        - **Matemática e Estatística Aplicada** (Data Science, ML e IA)
        - **Data Science para Análise Multivariada de Dados**
        - **Fundamentos de Data Science e Inteligência Artificial**
        """)

    st.divider()

    # =========================
    # DIFERENCIAIS (VISUALMENTE FORTES)
    # =========================
    st.header("🚀 Diferenciais Estratégicos")
    
    # Criando 3 colunas para destacar os pontos fortes
    d1, d2, d3 = st.columns(3)
    with d1:
        st.success("**Setor Financeiro**")
        st.caption("Experiência em ambientes de alta criticidade (Bradesco, Itaú).")
    with d2:
        st.success("**Visão End-to-End**")
        st.caption("Domínio desde a ingestão (ETL) até a entrega do Insight (BI).")
    with d3:
        st.success("**IA & Automação**")
        st.caption("Implementação de agentes de IA e fluxos inteligentes.")

    st.markdown("""
        - **Escalabilidade & Big Data:** Expertise no processamento de grandes volumes de dados, aplicando técnicas de particionamento e processamento paralelo para otimizar performance e custos em nuvem.
        - **Arquitetura Moderna (Data Lakehouse):** Implementação de arquiteturas que combinam a flexibilidade dos Data Lakes com a governança e performance de Data Warehouses, utilizando tecnologias como Databricks, Delta Lake e BigQuery.
        - **Data Pipeline End-to-End:** Capacidade de atuar em todo o ciclo de vida do dado, desde a ingestão (ETL/ELT) e orquestração de fluxos complexos até a modelagem dimensional e entrega de Dashboards estratégicos.
        - **Cultura de Governança e Qualidade:** Foco em garantir a integridade e a linhagem dos dados (Data Lineage), aplicando boas práticas de segurança e documentação em conformidade com as necessidades de setores regulados.
        """)

    st.divider()
    # Centralizando o título do rodapé de habilidades
    st.markdown("<h3 style='text-align: center;'>🛠️ Stack Tecnológica</h3>", unsafe_allow_html=True)

    # Bloco de ícones HTML
    st.markdown("""
    <p align="center">
        <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="40" style="margin: 10px;"/>
        <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/pandas/pandas-original.svg" width="40" style="margin: 10px;"/>
        <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/microsoftsqlserver/microsoftsqlserver-plain.svg" width="40" style="margin: 10px;"/>
        <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/postgresql/postgresql-original.svg" width="40" style="margin: 10px;"/>
        <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/mysql/mysql-original.svg" width="40" style="margin: 10px;"/>
        <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/linux/linux-original.svg" width="40" style="margin: 10px;"/>
        <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/docker/docker-original.svg" width="40" style="margin: 10px;"/>
        <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/git/git-original.svg" width="40" style="margin: 10px;"/>
        <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/amazonwebservices/amazonwebservices-original-wordmark.svg" width="40" style="margin: 10px;"/>
        <img src="https://cdn.simpleicons.org/databricks" width="40" style="margin: 10px;"/>
        <img src="https://cdn.simpleicons.org/googlebigquery" width="40" style="margin: 10px;"/>
        <img src="https://upload.wikimedia.org/wikipedia/commons/c/cf/New_Power_BI_Logo.svg" width="40" style="margin: 10px;"/>
        <img src="https://upload.wikimedia.org/wikipedia/commons/7/73/Microsoft_Excel_2013-2019_logo.svg" width="40" style="margin: 10px;"/>
    </p>
    """, unsafe_allow_html=True)

    st.caption("<p style='text-align: center;'>André Luiz Colombo | Engenharia & Análise de Dados</p>", unsafe_allow_html=True)

    # Rodapé informativo
    st.info("💡 Para detalhes sobre projetos específicos, navegue pelo menu lateral.")

# =========================
# PROJETOS
# =========================

elif menu == "📊 Projetos":

    # st.title("Projetos 🚀")

    # Substitua: st.title("Projetos 🚀") por:

    st.markdown(
        f"""
        <div style="display: flex; align-items: center; gap: 15px;">
            <img src="data:image/png;base64,{logo_github_base64}" width="50px">
            <h1 style="margin: 0;">Projetos</h1>
        </div>
        <br>
        """,
        unsafe_allow_html=True
    )

    # --- NOVO BLOCO: Link para o Perfil ---
    col_tit, col_btn = st.columns([2, 1])
    
    with col_tit:
        st.subheader("📂 Repositórios em Destaque")
        st.write("Abaixo estão os projetos que desenvolvi. Eles são carregados em tempo real do meu GitHub.")

    with col_btn:
        st.write("") # Espaçador para alinhar com o título
        st.link_button("🌐 Ver Perfil Completo no GitHub", f"https://github.com/{GITHUB_USERNAME}", type="secondary")
    
    st.divider()
    # --------------------------------------

    # Lista de repositórios que você NÃO quer mostrar
    repos_excluidos = [
        "aulagithub",
        "aulateste",
        "aula_csharp",
        "desafio-git",
        "desafio-merge",
        "sistema-de-cadastro"
    ]
    
    # ... (restante do seu código de carregamento e loop)

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

        st.markdown(f"### 🌐 {nome}")

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

    st.title("Contato 📞")
    st.write("Escolha a melhor forma de entrar em contato comigo:")

    # Criando colunas para os botões de ação
    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("E-mail")
        st.write("Resposta em até 24h")
        # Botão que abre o app de e-mail do usuário
        st.link_button("📧 Enviar E-mail", "mailto:andre-luiz-colombo@outlook.com")

    with col2:
        st.subheader("LinkedIn")
        st.write("Rede profissional e chat")
        st.link_button("🔗 Ver Perfil", "https://www.linkedin.com/in/andr%C3%A9-luiz-colombo-729755111/")

    with col3:
        st.subheader("GitHub")
        st.write("Meus códigos e projetos")
        st.link_button("🐙 Acessar Repos", "https://github.com/andrelcolombo")

    st.divider()

    # Informações Adicionais em um card visual
    with st.expander("📍 Outras Informações", expanded=True):
        st.markdown(f"""
        - **Localização:** São Paulo, SP
        - **Telefone/WhatsApp: (11)96917-7343**  [Clique para chamar](https://wa.me/5511969177343)
        - **E-mail:** andre-luiz-colombo@outlook.com
        - **LinkedIn:** [linkedin.com/in/andrelcolombo](https://www.linkedin.com/in/andr%C3%A9-luiz-colombo-729755111/)
        - **GitHub:** [github.com/andrelcolombo](https://github.com/andrelcolombo)
        - **Horário de Disponibilidade:** Segunda a Sexta, das 09:00 às 18:00
        """)