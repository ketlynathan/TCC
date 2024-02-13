import pandas as pd
import time
from loguru import logger
from connectDB import BancoDados 


# Obter as credenciais
conexao = BancoDados()
timeStart = time.time()

def inserir_dataframe_no_banco(dataframe):
    if conexao:
        cursor = conexao.cursor()
        logger.info(conexao)

        df= dataframe
        logger.info("reading dataframe")

        for index, row in df.iterrows():
            tipo = row['Tipo']
            titulo = row['Title']
            tempo = row['Tempo']
            distancia = row['Distancia']
            elevacao = row['Elevacao']
            data = row['Data']
        

            comando = f"""EXEC [SP_InserirStravaActivity]
                @Type = '{tipo}',
                @Date = '{data}',
                @Title = '{titulo}',
                @Time = '{tempo}',
                @Distance = '{distancia}',
                @Elevation = '{elevacao}'"""
        

            
            cursor.execute(comando)
            

        conexao.commit()

        cursor.close()
        conexao.close()
        logger.info("data successfully")
        timeEnd = time.time()
        logger.info(f"Insert data in  {int(timeEnd - timeStart)} seconds")
    else:
        logger.error("Unable to get connection")
