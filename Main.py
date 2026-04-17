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

GITHUB_USERNAME = "andrelcolombo"  

# =========================
# FUNÇÃO API GITHUB
# =========================

@st.cache_data(ttl=3600)
def carregar_repos():
    url = f"https://api.github.com/users/{GITHUB_USERNAME}/repos"

    token = st.secrets.get("GITHUB_TOKEN")
    
    headers = {
        "Authorization": f"token {token}",
        "User-Agent": GITHUB_USERNAME  # Adicionado para evitar bloqueios extras
    } if token else {"User-Agent": GITHUB_USERNAME}

    try:
        # Passamos os headers com o token aqui
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            return response.json()
        else:
            return [] 
    except:
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
        margin-bottom: 50px; 
        border: 2px solid #31333F; /* Cinza escuro discreto, quase imperceptível */
        box-shadow: 0px 8px 20px rgba(0,0,0,0.4); /* Sombra mais suave e elegante */
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

with st.sidebar:
    st.title("Menu")

    menu = st.sidebar.radio(
        "Opções",
        ["🏠 Sobre mim", "ℹ️ Informações", "📊 Projetos", "📞 Contato"]
    )

    st.markdown("<br><br>", unsafe_allow_html=True)
    
    st.divider()

if menu == "🏠 Sobre mim":

    # =========================
    # HEADER
    # =========================

    st.title("André Luiz Colombo")
    st.subheader("Data Engineer | ETL & Data Pipelines | Analytics")

    # =========================
    # RESUMO PROFISSIONAL
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

    # Criando duas colunas para organizar melhor o espaço
    col_esp1, col_esp2 = st.columns(2)

    estilo_box = "background-color: #262730; padding: 20px; border-radius: 10px; border-left: 5px solid #FF4B4B; margin-bottom: 20px; min-height: 160px;"

    with col_esp1:
        st.markdown(f"""
        <div style="{estilo_box}">
            <h4 style="margin: 0;">🏗️ Arquitetura de Dados</h4>
            <p style="font-size: 0.9rem; color: #FAFAFA;">
                Construção de pipelines <b>End-to-End</b>, processos de <b>ETL/ELT</b> e estruturação de <b>Data Warehousing</b> robustos para suporte à decisão.
            </p>
        </div>
        <div style="{estilo_box}">
            <h4 style="margin: 0;">🔗 Integração</h4>
            <p style="font-size: 0.9rem; color: #FAFAFA;">
                Conexão de dados complexos entre <b>APIs, ERPs</b> e bancos de dados relacionais, garantindo fluidez e integridade.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col_esp2:
        st.markdown(f"""
        <div style="{estilo_box}">
            <h4 style="margin: 0;">📐 Modelagem de Data Warehousing</h4>
            <p style="font-size: 0.9rem; color: #FAFAFA;">
                Expertise em <b>Star Schema</b> e modelagem voltada para performance em ferramentas de BI e Analytics.
            </p>
        </div>
        <div style="{estilo_box}">
            <h4 style="margin: 0;">🛡️ Qualidade & Automação</h4>
            <p style="font-size: 0.9rem; color: #FAFAFA;">
                Foco em <b>Data Quality</b>, governança e automação de rotinas para otimizar o tempo de resposta do negócio.
            </p>
        </div>
        """, unsafe_allow_html=True)

    st.divider()

    # =========================
    # LINHA DO TEMPO (EXPERIÊNCIA PROFISSIONAL)
    # =========================

    st.header("⏳ Trajetória Profissional")

    def timeline_item(periodo, cargo, empresa, detalhes):
        detalhes_html = "".join([f"<li style='margin-bottom: 5px;'>{item}</li>" for item in detalhes])
        
        st.markdown(f"""
            <div style="margin-left: 20px; padding-left: 20px; border-left: 2px solid #FF4B4B; position: relative; margin-bottom: 30px;">
                <div style="position: absolute; width: 12px; height: 12px; background-color: #FF4B4B; border-radius: 50%; left: -7px; top: 5px;"></div>
                <span style="font-size: 0.85rem; color: #888;">{periodo}</span>
                <h4 style="margin: 0; color: #FAFAFA;">{cargo}</h4>
                <h5 style="margin: 0; color: #FF4B4B; font-weight: normal;">{empresa}</h5>
                <ul style="font-size: 0.9rem; color: #FAFAFA; margin-top: 10px; line-height: 1.4; padding-left: 20px;">
                    {detalhes_html}
                </ul>
            </div>
        """, unsafe_allow_html=True)

    # =========================
    # EXECUÇÃO DA TIMELINE 
    # =========================

    timeline_item(
        "11/2024 - Atual", 
        "Engenheiro de Dados", 
        "Bradesco Seguros", 
        [
            "Construção e manutenção de pipelines de dados utilizando Python e SQL",
            "Tratamento e transformação de dados corporativos para análises estratégicas",
            "Desenvolvimento de dashboards executivos em Power BI e modelagem de indicadores",
            "Apoio direto às áreas de negócio na interpretação de dados estratégicos"
        ]
    )

    timeline_item(
        "08/2024 - 11/2024", 
        "Analista de Dados", 
        "Netsupport", 
        [
            "Criação de relatórios e dashboards operacionais para acompanhamento de KPIs",
            "Automação de rotinas utilizando Python e SQL",
            "Integração de dados provenientes de múltiplas fontes corporativas"
        ]
    )

    timeline_item(
        "06/2023 - 06/2024", 
        "Analista Engenharia de TI", 
        "Itaú Unibanco", 
        [
            "Análise e manipulação de dados em bases relacionais com consultas SQL avançadas",
            "Utilização de serviços AWS (S3, EC2, RDS e Lambda) para soluções escaláveis",
            "Desenvolvimento de automações para processos internos e relatórios",
            "Entrega de incrementos de software funcionais seguindo a metodologia ágil (Scrum)"
        ]
    )

    timeline_item(
        "04/2021 - 06/2023", 
        "Analista de Operações Corretora", 
        "Itaú Unibanco", 
        [
            "Análise de dados operacionais e geração de indicadores de performance",
            "Criação de dashboards em Excel e Power BI para visualização de resultados",
            "Desenvolvimento de automações de relatórios utilizando VBA"
        ]
    )

    timeline_item(
        "11/2019 - 04/2021", 
        "Estagiário de Engenharia/TI", 
        "Itaú Unibanco", 
        [
            "Suporte técnico e apoio no desenvolvimento de soluções de dados",
            "Início da trajetória em análise de processos e automação dentro do setor bancário"
        ]
    )

    st.divider()
    # =========================
    # STACK
    # =========================

    st.header("🚀 Stack Tecnológica")


    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("🧠 Data Engineering")
        st.markdown("""
            <div style="display: flex; flex-direction: column; gap: 10px;">
                <div style="display: flex; align-items: center;"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="30"/><span style="margin-left: 10px;"><b>Python:</b> ETL e Automação</span></div>
                <div style="display: flex; align-items: center;"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/pandas/pandas-original.svg" width="30"/><span style="margin-left: 10px;"><b>Pandas:</b> Manipulação de Dados</span></div>
                <div style="display: flex; align-items: center;"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/microsoftsqlserver/microsoftsqlserver-plain.svg" width="30"/><span style="margin-left: 10px;"><b>SQL Server:</b> Bancos Relacionais</span></div>
                <div style="display: flex; align-items: center;"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/postgresql/postgresql-original.svg" width="30"/><span style="margin-left: 10px;"><b>PostgreSQL:</b> Queries Avançadas</span></div>
                <div style="display: flex; align-items: center;"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/mysql/mysql-original.svg" width="30"/><span style="margin-left: 10px;"><b>MySQL:</b> Gestão de Dados</span></div>
                <div style="display: flex; align-items: center;"><img src="https://cdn.simpleicons.org/googlebigquery" width="30"/><span style="margin-left: 10px;"><b>BigQuery:</b> Data Warehousing</span></div>
                <div style="display: flex; align-items: center;"><img src="https://cdn.simpleicons.org/databricks" width="30"/><span style="margin-left: 10px;"><b>Databricks:</b> Spark e Big Data</span></div>
            </div>
        """, unsafe_allow_html=True)

    with col2:
        st.subheader("☁️ Cloud & Infra")
        st.markdown("""
            <div style="display: flex; flex-direction: column; gap: 10px;">
                <div style="display: flex; align-items: center;"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/amazonwebservices/amazonwebservices-original-wordmark.svg" width="30"/><span style="margin-left: 10px;"><b>AWS:</b> S3, EC2 e Lambda</span></div>
                <div style="display: flex; align-items: center;"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/docker/docker-original.svg" width="30"/><span style="margin-left: 10px;"><b>Docker:</b> Containerização</span></div>
                <div style="display: flex; align-items: center;"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/linux/linux-original.svg" width="30"/><span style="margin-left: 10px;"><b>Linux:</b> Adm. de Servidores</span></div>
                <div style="display: flex; align-items: center;"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/git/git-original.svg" width="30"/><span style="margin-left: 10px;"><b>Git:</b> Versionamento</span></div>
            </div>
        """, unsafe_allow_html=True)

    with col3:
        st.subheader("📊 Analytics")
        st.markdown("""
            <div style="display: flex; flex-direction: column; gap: 10px;">
                <div style="display: flex; align-items: center;"><img src="https://upload.wikimedia.org/wikipedia/commons/c/cf/New_Power_BI_Logo.svg" width="30"/><span style="margin-left: 10px;"><b>Power BI:</b> Dashboards e DAX</span></div>
                <div style="display: flex; align-items: center;"><img src="https://cdn.simpleicons.org/looker" width="30"/><span style="margin-left: 10px;"><b>Looker:</b> Visualização Cloud</span></div>
                <div style="display: flex; align-items: center;"><img src="https://upload.wikimedia.org/wikipedia/commons/4/4b/Tableau_Logo.png" width="90"/><span style="margin-left: 10px;"><b>Tableau:</b> Business Intelligence</span></div>
                <div style="display: flex; align-items: center;"><img src="https://upload.wikimedia.org/wikipedia/commons/7/73/Microsoft_Excel_2013-2019_logo.svg" width="30"/><span style="margin-left: 10px;"><b>Excel:</b> VBA e Planilhas</span></div>
            </div>
        """, unsafe_allow_html=True)



    st.divider()

    # =========================
    # POSICIONAMENTO
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

    st.header("👤 Entre Códigos e Cafés: Conheça o André")

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

    st.markdown(
    """
    <div style="text-align: center; color: #888; font-size: 0.8rem; margin-top: 10px;">
        André Luiz Colombo | Engenharia & Análise de Dados
    </div>
    """, 
    unsafe_allow_html=True
)

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
    # CERTIFICAÇÕES
    # =========================
   
    caminho_badge_fcd = os.path.join(BASE_DIR, "imagens", "Badge - FCD 4.0 - André Luiz Colombo.png")
    caminho_badge_fada = os.path.join(BASE_DIR, "imagens", "Badge - FADA 4.0 - André Luiz Colombo.png")

    st.header("🏅 Especializações e Certificações")
    st.info("Clique nos grupos para expandir ou recolher as informações.")

    with st.expander("🏆 Formações Principais (Master)", expanded=False):
        st.markdown("""
        - **Formação Cientista de Dados 4.0** - *Data Science Academy* 
        - **Formação Analista de Dados 4.0** - *Data Science Academy*
        """)

        col_badge1, col_badge2 = st.columns(2, gap="large")

        vazia_esq, col_badge1, col_badge2, vazia_dir = st.columns([1, 2, 2, 1])


        # Lógica para Badge FCD (PNG)

        if os.path.exists(caminho_badge_fcd):
            badge_fcd_base64 = carregar_imagem_base64(caminho_badge_fcd)
            with col_badge1: # Usa a segunda coluna
                st.markdown(f"""
                    <div style="text-align: center;">
                        <img src="data:image/png;base64,{badge_fcd_base64}" width="80%" style="border-radius: 10px; border: 1px solid #31333F;">
                        <p style="font-size: 0.8rem; color: #888; margin-top: 5px;">Cientista de Dados 4.0</p>
                    </div>
                """, unsafe_allow_html=True)

        # Lógica para Badge FADA (PNG)
        if os.path.exists(caminho_badge_fada):
            badge_fada_base64 = carregar_imagem_base64(caminho_badge_fada)
            with col_badge2: # Usa a terceira coluna
                st.markdown(f"""
                    <div style="text-align: center;">
                        <img src="data:image/png;base64,{badge_fada_base64}" width="80%" style="border-radius: 10px; border: 1px solid #31333F;">
                        <p style="font-size: 0.8rem; color: #888; margin-top: 5px;">Analista de Dados 4.0</p>
                    </div>
                """, unsafe_allow_html=True)
        else:
            col_badge2.warning("Arquivo FADA (.png) não encontrado.")

    with st.expander("⚙️ Engenharia de Dados, Cloud & Automação", expanded=False):
        st.markdown("""
        - **IA Generativa e Agentes de IA Para Fluxos de Automação com Langflow e n8n**
        - **SQL Server Integration Services (SSIS) - ETL Avançado** 
        - **Build Data Pipelines** (Lakeflow / Data Engineering)
        - **Pipelines de Dados com Google BigQuery**
        - **Fundamentos de Engenharia de Dados**
        - **Databricks Get Started Days** (Data Engineering + SQL Analytics)
        - **Cloud Computing & Data Science** (Amazon SageMaker e Microsoft Fabric)
        """)

    with st.expander("📊 Business Intelligence & Analytics", expanded=False):
        st.markdown("""
        - **AI/BI for Data Analysts** (Databricks)
        - **Power BI: DAX contextos e iteração**
        - **Modelagem e Análise de Dados com Power BI**
        - **Looker Studio: Visualização de Dados**
        - **Microsoft Power BI para Business Intelligence e Data Science**
        - **SQL Para Análise de Dados e Data Science**
        - **Projetos de Análise de Dados com Linguagem Python**
        - **Storytelling e Dashboards de Alto Impacto**
        - **Tableau: Visualização de Dados**
        """)

    with st.expander("🧠 Data Science, Estatística & ML", expanded=False):
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
        <img src="https://upload.wikimedia.org/wikipedia/commons/4/4b/Tableau_Logo.png" width="90"/><span style="margin-left: 10px;"/>
    """, unsafe_allow_html=True)

    # Rodapé informativo
    st.info("💡 Para detalhes sobre projetos específicos, navegue pelo menu lateral.")

    st.markdown(
    """
    <div style="text-align: center; color: #888; font-size: 0.8rem; margin-top: 10px;">
        André Luiz Colombo | Engenharia & Análise de Dados
    </div>
    """, 
    unsafe_allow_html=True
)

# =========================
# PROJETOS
# =========================

elif menu == "📊 Projetos":

    # st.title("Projetos 🚀")

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

    col_tit, col_btn = st.columns([2, 1])
    
    with col_tit:
        st.subheader("📂 Repositórios em Destaque")
        st.write("Abaixo estão os projetos que desenvolvi. Eles são carregados em tempo real do meu GitHub.")

    with col_btn:
        st.write("") # Espaçador para alinhar com o título
        st.link_button("🌐 Ver Perfil Completo no GitHub", f"https://github.com/{GITHUB_USERNAME}", type="secondary")
    
    st.divider()
   

    repos_excluidos = ["aulagithub", "aulateste", "aula_csharp", "desafio-git", "desafio-merge", "sistema-de-cadastro"]
    
    repos = carregar_repos()

    if repos:
        # Filtragem e Limpeza
        repos_filtrados = [
            repo for repo in repos 
            if repo["name"].lower() not in repos_excluidos 
            and not repo["fork"] 
            and repo["description"] is not None
        ]

        # Ordenar pelos mais recentes ou com mais estrelas
        repos_filtrados = sorted(repos_filtrados, key=lambda x: x['stargazers_count'], reverse=True)

        for repo in repos_filtrados:
           
            margem_esq, centro, margem_dir = st.columns([1, 6, 1])

            with centro:
                with st.container(border=True):
                    # Título
                    nome = repo['name'].replace('-', ' ').title()
                    st.markdown(f"### 📁 {nome}")
                    
                    # Badge
                    lang = repo.get("language")
                    if lang:
                        color = "#FF4B4B" if lang == "Python" else "#0083B0"
                        st.markdown(f"<span style='background-color:{color}; padding:2px 8px; border-radius:10px; color:white; font-size:12px;'>{lang}</span>", unsafe_allow_html=True)
                    
                    # Descrição com corte (Garanta que a classe 'repo-desc-box' esteja no seu CSS lá no topo)
                    desc = repo.get('description') or "Sem descrição."
                    st.markdown(f'<div class="repo-desc-box"><i>{desc}</i></div>', unsafe_allow_html=True)
                    
                    # Rodapé
                    st.caption(f"⭐ {repo.get('stargazers_count', 0)} | 🍴 {repo.get('forks_count', 0)}")
                    st.link_button("🌐 Acessar Repositório", repo["html_url"], use_container_width=True)
    else:
        st.warning("Não foi possível carregar os projetos. Verifique sua conexão ou limite da API.")

    st.markdown(
    """
    <div style="text-align: center; color: #888; font-size: 0.8rem; margin-top: 10px;">
        André Luiz Colombo | Engenharia & Análise de Dados
    </div>
    """, 
    unsafe_allow_html=True
)    
    
# =========================
# CONTATO
# =========================

elif menu == "📞 Contato":
    st.title("Vamos conversar? 📞")
    st.write("Estou aberto a novas conexões, projetos e oportunidades na área de dados.")

    # =========================
    # CARDS DE AÇÃO RÁPIDA
    # =========================
    
    estilo_card = """
        background-color: #262730; 
        padding: 25px 10px; 
        border-radius: 12px; 
        border-top: 4px solid #FF4B4B; 
        margin-bottom: 10px;
        min-height: 200px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
    """

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(f"""
            <div style="{estilo_card}">
                <img src="https://cdn.simpleicons.org/gmail/EA4335" width="45" style="margin-bottom:15px;">
                <span style="color: white; font-size: 1.25rem; font-weight: bold; display: block; width: 100%;">E-mail</span>
                <span style="color: #888; font-size: 0.85rem; display: block; width: 100%; margin-top: 5px;">Propostas formais</span>
            </div>
        """, unsafe_allow_html=True)
        st.link_button("Enviar E-mail", "mailto:andre-luiz-colombo@outlook.com", use_container_width=True)

    with col2:
        st.markdown(f"""
            <div style="{estilo_card}">
                <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/linkedin/linkedin-original.svg" width="45" style="margin-bottom:15px;">
                <span style="color: white; font-size: 1.25rem; font-weight: bold; display: block; width: 100%;">LinkedIn</span>
                <span style="color: #888; font-size: 0.85rem; display: block; width: 100%; margin-top: 5px;">Rede Profissional</span>
            </div>
        """, unsafe_allow_html=True)
        st.link_button("Ver Perfil", "https://www.linkedin.com/in/andr%C3%A9-luiz-colombo-729755111/", use_container_width=True)

    with col3:
        st.markdown(f"""
            <div style="{estilo_card}">
                <img src="https://cdn.simpleicons.org/whatsapp/25D366" width="45" style="margin-bottom:15px;">
                <span style="color: white; font-size: 1.25rem; font-weight: bold; display: block; width: 100%;">WhatsApp</span>
                <span style="color: #888; font-size: 0.85rem; display: block; width: 100%; margin-top: 5px;">Contato Direto</span>
            </div>
        """, unsafe_allow_html=True)
        st.link_button("Chamar agora", "https://wa.me/5511969177343", use_container_width=True)

    st.divider()

    # =========================
    # INFORMAÇÕES DETALHADAS
    # =========================
    
    c_info, c_status = st.columns([2, 1])

    with c_info:
        st.header("📍 Detalhes de Contato")
        with st.container(border=True):
     
            st.markdown(f"""
            <div style="display: flex; flex-direction: column; gap: 12px; padding: 10px;">
                <div style="display: flex; align-items: center; gap: 12px;">
                    <img src="https://cdn.simpleicons.org/googlemaps/4285F4" width="20">
                    <span><b>Localização:</b> São Paulo, SP</span>
                </div>
                <div style="display: flex; align-items: center; gap: 12px;">
                    <img src="https://cdn.simpleicons.org/gmail/EA4335" width="20">
                    <span><b>E-mail:</b> <a href="mailto:andre-luiz-colombo@outlook.com" style="color: #FF4B4B; text-decoration: none;">andre-luiz-colombo@outlook.com</a></span>
                </div>
                <div style="display: flex; align-items: center; gap: 12px;">
                    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/linkedin/linkedin-original.svg" width="20">
                    <span><b>LinkedIn:</b> <a href="https://www.linkedin.com/in/andr%C3%A9-luiz-colombo-729755111/" style="color: #FF4B4B; text-decoration: none;">linkedin.com/in/andre-luiz-colombo</a></span>
                </div>
                <div style="display: flex; align-items: center; gap: 12px;">
                    <img src="https://cdn.simpleicons.org/whatsapp/25D366" width="20">
                    <span><b>Telefone:</b> <a href="https://wa.me/5511969177343" style="color: #FF4B4B; text-decoration: none;">(11) 96917-7343</a></span>
                </div>
                <div style="display: flex; align-items: center; gap: 12px;">
                    <img src="https://cdn.simpleicons.org/github/FFFFFF" width="20">
                    <span><b>GitHub:</b> <a href="https://github.com/andrelcolombo" style="color: #FF4B4B; text-decoration: none;">github.com/andrelcolombo</a></span>
                </div>
                <div style="display: flex; align-items: center; gap: 12px;">
                    <img src="https://cdn.simpleicons.org/databricks/FF3621" width="20">
                    <span><b>Foco Atual:</b> Data Engineering & Analytics Engineering</span>
                </div>
                <div style="display: flex; align-items: center; gap: 12px;">
                    <img src="https://cdn.simpleicons.org/python/3776AB" width="20">
                    <span><b>Stack Principal:</b> Python, SQL, Spark, ETL/ELT, Analytics & Cloud</span>
                </div>
            </div>
        """, unsafe_allow_html=True)
            
            st.write("")
            st.caption("🚀 Atuando na construção de arquiteturas de dados modernas e escaláveis.")

    with c_status:
        st.header("🕒 Disponibilidade")
        with st.container(border=True):
            st.success("**Disponível para novos projetos**")
            st.markdown("""
            **Horário Comercial:** Segunda a Sexta  
            09:00 — 18:00
            """)

    # Rodapé final
    st.markdown(
    """
    <div style="text-align: center; color: #888; font-size: 0.8rem; margin-top: 10px;">
        André Luiz Colombo | Engenharia & Análise de Dados
    </div>
    """, 
    unsafe_allow_html=True
)