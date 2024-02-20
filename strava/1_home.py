import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import calendar

# Define o título da página
st.set_page_config(page_title="Minhas Atividades")

# Define a imagem de cabeçalho
with st.container():
    st.image("./img/Movimente-se.png")
    st.title("Atividades Fisicas")
    st.write("Detalhes de progresso e evolução")


# Carrega os dados do arquivo Excel
with st.container():
    st.write("---")
    file = 'sports.xlsx'
    if "data" not in st.session_state:
        df_dados = pd.read_excel(file)
        st.session_state["data"] = df_dados
        st.write(df_dados)

    st.sidebar.markdown(
        "Desenvolvido por [Keh do Movimentese](https://www.instagram.com/kemovimentese/)")
