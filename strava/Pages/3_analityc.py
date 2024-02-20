import streamlit as st
import pandas as pd

st.set_page_config(page_title="Minhas Atividades")
with st.container():
    st.subheader(" Movimente-se")
    st.title("Dashboard de Atividades Fisicas")
    st.write("Informações de distacias e tipos de atividades")

with st.container():
    st.write("---")
    file = 'sports.xlsx'
    dados = pd.read_excel(file)

    st.area_chart(dados, x="Date", y="Distance")