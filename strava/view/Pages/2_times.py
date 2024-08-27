import streamlit as st
import plotly.express as px
import altair as alt
import pandas as pd

df_dados = st.session_state["data"]

sports = df_dados["Type"].value_counts().index
sport = st.sidebar.selectbox("Type", sports)

df_sport = df_dados[df_dados["Type"] == sport]

# Definindo o título da atividade
st.title(df_sport['Type'].iloc[0])

# Exibindo a imagem da atividade
col_img, col_text = st.columns([0.1, 1])  # Define a proporção das colunas

if sport == "Run":
    col_img.image("./img/corrida.png", width=100)
elif sport == "Walk":
    col_img.image("./img/andando.png", width=100)
elif sport == "Ride":
    col_img.image("./img/ciclismo.png", width=100)

total_distancia = df_sport["Distance"].sum()
total_distancia_formatado = "{:.2f}".format(total_distancia)

df_sport['Time'] = pd.to_datetime(df_dados['Time'], format='%H:%M:%S').dt.time

max_value = 100

# Calcula a porcentagem de conclusão com base na distância total
porcentagem_conclusao = (total_distancia / max_value)
total_dias = df_sport["Date"].nunique()
total_elevacao = df_sport["Elevation"].sum()

menor_tempo = df_sport['Time'].min()
maior_tempo = df_sport['Time'].max()
menor_Distancia = df_sport['Distance'].min()
maior_Distancia = df_sport['Distance'].max()

# Exibindo métricas e barra de progresso
col1, col2, col3, col4 = st.columns(4)
col1.markdown(f"**Kms Treinados:** {total_distancia_formatado}")
col2.markdown(f"**Dias Treinados:** {total_dias} dias")
col3.markdown(f"**Total de Elevação:** {total_elevacao} ")

st.divider()
st.subheader(f"**Treino:** {porcentagem_conclusao * 100:.2f}%")
st.progress(porcentagem_conclusao)

col1, col2, col3, col4 = st.columns(4)
col1.metric(label="Menor Distancia:", value=f"{menor_Distancia}")
col2.metric(label="Menor tempo:", value=f"{menor_tempo}")
col3.metric(label="Maior tempo:", value=f"{maior_tempo}")
col4.metric(label="Maior Distancia:", value=f"{maior_Distancia}")
