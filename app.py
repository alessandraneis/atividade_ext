import streamlit as st
import pandas as pd
import sys

# ==========================================================
# CONFIGURAÇÃO DA PÁGINA
# ==========================================================
st.set_page_config(
    page_title="Cadastro Estudos Clínicos - Brasil",
    page_icon="🏥",
    layout="wide"
)

# ==========================================================
# CSS PERSONALIZADO
# ==========================================================
st.markdown("""
<style>
.main-header {
    font-size: 2.5rem;
    color: #1f77b4;
    text-align: center;
    margin-bottom: 2rem;
    font-weight: bold;
}

.success-box {
    padding: 20px;
    background-color: #d4edda;
    border-radius: 10px;
    border: 1px solid #c3e6cb;
    margin: 10px 0;
}

.info-box {
    padding: 15px;
    background-color: #e8f4fd;
    border-radius: 8px;
    border: 1px solid #b8daff;
    margin: 10px 0;
}
</style>
""", unsafe_allow_html=True)

# ==========================================================
# HEADER
# ==========================================================
st.markdown(
    '<div class="main-header">🏥 Sistema de Cadastro para Estudos Clínicos - Brasil</div>',
    unsafe_allow_html=True
)

# ==========================================================
# MENU LATERAL
# ==========================================================
with st.sidebar:
    st.title("Menu de Navegação")

    menu_option = st.radio(
        "Selecione uma seção:",
        [
            "Estudos Disponíveis",
            "Cadastro de Voluntários",
            "Sobre o Projeto"
        ]
    )

    st.markdown("---")
    st.write("### Tecnologias")
    st.caption("Python + Streamlit")
    st.caption("Projeto de Extensão")

# ==========================================================
# DADOS DE EXEMPLO
# ==========================================================
estudos_data = {
    "Estudo": [
        "Eficácia de Nova Medicação para Hipertensão Arterial",
        "Estudo sobre Diabetes Mellitus Tipo 2",
        "Pesquisa em Tratamento Oncológico Inovador",
        "Estudo de Vacina para Influenza Sazonal",
        "Pesquisa sobre Doenças Autoimunes"
    ],
    "Área": [
        "Cardiologia",
        "Endocrinologia",
        "Oncologia",
        "Imunologia",
        "Reumatologia"
    ],
    "Local": [
        "São Paulo - SP",
        "Rio de Janeiro - RJ",
        "Belo Horizonte - MG",
        "Porto Alegre - RS",
        "Brasília - DF"
    ],
    "Requisitos": [
        "18-65 anos, hipertensos",
        "30-70 anos, diabéticos",
        "18+ anos, diagnóstico recente",
        "18-50 anos, saudáveis",
        "18-60 anos, doença autoimune"
    ],
    "Status": [
        "🔵 Recrutando",
        "🔵 Recrutando",
        "🟡 Em andamento",
        "🔵 Recrutando",
        "🟡 Em andamento"
    ],
    "Previsão": [
        "Dez/2026",
        "Mar/2027",
        "Jun/2027",
        "Ago/2026",
        "Nov/2026"
    ]
}

estudos_df = pd.DataFrame(estudos_data)

# ==========================================================
# ESTUDOS DISPONÍVEIS
# ==========================================================
if menu_option == "Estudos Disponíveis":

    st.header("Estudos Clínicos em Andamento")

    col1, col2, col3 = st.columns(3)

    with col1:
        filtro_area = st.multiselect(
            "Filtrar por área",
            estudos_df["Área"].unique()
        )

    with col2:
        filtro_local = st.multiselect(
            "Filtrar por local",
            estudos_df["Local"].unique()
        )

    with col3:
        filtro_status = st.multiselect(
            "Filtrar por status",
            estudos_df["Status"].unique()
        )

    estudos_filtrados = estudos_df.copy()

    if filtro_area:
        estudos_filtrados = estudos_filtrados[
            estudos_filtrados["Área"].isin(filtro_area)
        ]

    if filtro_local:
        estudos_filtrados = estudos_filtrados[
            estudos_filtrados["Local"].isin(filtro_local)
        ]

    if filtro_status:
        estudos_filtrados = estudos_filtrados[
            estudos_filtrados["Status"].isin(filtro_status)
        ]

    st.subheader("Estudos Encontrados")

    if not estudos_filtrados.empty:
        st.dataframe(
            estudos_filtrados,
            use_container_width=True,
            hide_index=True
        )
    else:
        st.warning("Nenhum estudo encontrado para os filtros selecionados.")

    st.markdown("---")

    st.subheader("Detalhes do Estudo")

    estudo_selecionado = st.selectbox(
        "Selecione um estudo",
        estudos_df["Estudo"]
    )

    estudo_info = estudos_df[
        estudos_df["Estudo"] == estudo_selecionado
    ].iloc[0]

    st.info(
        f"""
**Estudo:** {estudo_info['Estudo']}

**Área:** {estudo_info['Área']}

**Local:** {estudo_info['Local']}

**Requisitos:** {estudo_info['Requisitos']}

**Status:** {estudo_info['Status']}

**Previsão de término:** {estudo_info['Previsão']}

**Descrição:** Estudo clínico randomizado controlado para avaliação de eficácia e segurança.

**Duração estimada:** 6 a 12 meses.

**Compensação:** Conforme regulamentação vigente.

**Critérios adicionais:** Avaliação médica prévia obrigatória.
"""
    )

# ==========================================================
# CADASTRO DE VOLUNTÁRIOS
# ==========================================================
st.header("📝 Cadastro de Voluntários")

with st.form("formulario_voluntario"):

    st.subheader("Dados Pessoais")

    nome = st.text_input("Nome Completo*")

    email = st.text_input("E-mail*")

    telefone = st.text_input("Telefone")

    idade = st.number_input(
        "Idade*",
        min_value=18,
        max_value=120,
        value=18
    )

    sexo = st.selectbox(
        "Sexo",
        [
            "Feminino",
            "Masculino",
            "Outro",
            "Prefiro não informar"
        ]
    )

    tipo_sanguineo = st.selectbox(
        "Tipo Sanguíneo",
        [
            "Não sei",
            "A+",
            "A-",
            "B+",
            "B-",
            "AB+",
            "AB-",
            "O+",
            "O-"
        ]
    )

    st.divider()

    st.subheader("Informações de Saúde")

    possui_doenca_cronica = st.radio(
        "Possui alguma doença crônica?",
        ["Não", "Sim"]
    )

    doenca_cronica = ""

    if possui_doenca_cronica == "Sim":
        doenca_cronica = st.text_area(
            "Informe a(s) doença(s) crônica(s)"
        )

    usa_medicamentos = st.radio(
        "Faz uso contínuo de medicamentos?",
        ["Não", "Sim"]
    )

    medicamentos = ""

    if usa_medicamentos == "Sim":
        medicamentos = st.text_area(
            "Informe os medicamentos utilizados"
        )

    st.divider()

    st.subheader("Hábitos de Vida")

    fumante = st.radio(
        "É fumante?",
        [
            "Não",
            "Sim",
            "Ex-fumante"
        ]
    )

    consumo_alcool = st.selectbox(
        "Consome bebida alcoólica?",
        [
            "Não",
            "Raramente",
            "1 a 2 vezes por semana",
            "3 ou mais vezes por semana"
        ]
    )

    atividade_fisica = st.selectbox(
        "Pratica atividade física?",
        [
            "Não",
            "1 a 2 vezes por semana",
            "3 a 5 vezes por semana",
            "Mais de 5 vezes por semana"
        ]
    )

    st.divider()

    observacoes = st.text_area(
        "Observações adicionais (opcional)"
    )

    enviar = st.form_submit_button(
        "Cadastrar Voluntário"
    )

if enviar:

    if not nome or not email:
        st.error(
            "Preencha os campos obrigatórios (Nome e E-mail)."
        )

    else:

        st.success(
            "Cadastro realizado com sucesso!"
        )

        st.subheader("Resumo do Cadastro")

        st.write(f"**Nome:** {nome}")
        st.write(f"**E-mail:** {email}")
        st.write(f"**Telefone:** {telefone}")
        st.write(f"**Idade:** {idade}")
        st.write(f"**Sexo:** {sexo}")
        st.write(f"**Tipo Sanguíneo:** {tipo_sanguineo}")

        st.write(
            f"**Possui doença crônica:** {possui_doenca_cronica}"
        )

        if doenca_cronica:
            st.write(
                f"**Doença(s) informada(s):** {doenca_cronica}"
            )

        st.write(
            f"**Uso contínuo de medicamentos:** {usa_medicamentos}"
        )

        if medicamentos:
            st.write(
                f"**Medicamentos informados:** {medicamentos}"
            )

        st.write(f"**Fumante:** {fumante}")
        st.write(f"**Consumo de álcool:** {consumo_alcool}")
        st.write(f"**Atividade física:** {atividade_fisica}")

        if observacoes:
            st.write(
                f"**Observações:** {observacoes}"
            )

# ==========================================================
# SOBRE O PROJETO
# ==========================================================
elif menu_option == "Sobre o Projeto":

    st.header("ℹ️ Sobre o Projeto")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Objetivo")

        st.write("""
Conectar voluntários a estudos clínicos em todo o Brasil,
facilitando o recrutamento para pesquisas científicas e
ampliando o acesso a tratamentos inovadores.
""")

        st.subheader("Benefícios ao Participante")

        st.write("""
- Acesso a tratamentos inovadores
- Contribuição para o avanço da ciência
- Acompanhamento médico especializado
- Exames gratuitos
- Medicamentos gratuitos quando aplicável
- Possível compensação financeira
""")

    with col2:
        st.subheader("🛡️ Aspectos Éticos")

        st.write("""
- Aprovação por Comitê de Ética em Pesquisa
- Sigilo absoluto dos dados
- Consentimento Livre e Esclarecido
- Participação voluntária
- Direito de desistência a qualquer momento
""")

# ==========================================================
# RODAPÉ
# ==========================================================
st.markdown("---")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("**Contato:** contato@estudosclinicos.org.br")

with col2:
    st.markdown("**Site:** www.estudosclinicos.org.br")
    st.caption(f"Python {sys.version.split()[0]}")

with col3:
    st.markdown("**Projeto de Extensão Universitária**")