import streamlit as st
import altair as alt
import numpy as np
import datetime
import plotly.express as px
import pandas as pd

st.set_page_config(page_title="Minhas Atividades")
with st.container():
    st.subheader(" Movimente-se")
    st.title("Dashboard de Atividades Fisicas")
    st.write("Informações de distacias e tipos de atividades")

with st.container():
    st.write("---")
    file = 'sports.xlsx'
    df = pd.read_excel(file)
    atividades = df['Type']
    distancia = df['Distance'].sum()

    col = st.columns((1.5, 4.5, 2), gap='medium')
    
    with col[0]:
        st.markdown('#### Atividades')
        #treino= df.query("Type == 'Run'")
        #fig = px.bar(df, x='Date', y='Distance')
        #fig.show()
    
        
    with col[1]:
        st.markdown('#### Total Treino')
        st.area_chart(df, x="Type", y="Distance")
        st.write("---")
        
    
    with col[2]:
        st.markdown('#### Dias Treinado')
        st.line_chart(df, x='Distance', y= 'Date')

        
    
    
    

   

    