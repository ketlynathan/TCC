import pandas as pd
import time
from loguru import logger
from dataBase import DataBaseConnector 


# Obter as credenciais
database_connector = DataBaseConnector()
conexao = database_connector.connect()
timeStart = time.time()

def InserirDataframeNoBanco(dataframe):
    if conexao:
        cursor = conexao.cursor()
        logger.info(conexao)

        df= dataframe
        logger.info("reading dataframe")

        for index, row in df.iterrows():
            tipo = row['Type']
            titulo = row['Title']
            tempo = row['Time']
            distancia = row['Distance']
            elevacao = row['Elevation']
            data = row['Date']
        

            comando = f"""EXEC [SP_InserirStravaActivity]
                @Type = '{tipo}',
                @Date = '{data}',
                @Title = '{titulo}',
                @Time = '{tempo}',
                @Distance = '{distancia}',
                @Elevation = '{elevacao}'"""
            

        conexao.commit()

        cursor.close()
        conexao.close()
        logger.info("data successfully")
        timeEnd = time.time()
        logger.info(f"Insert data in  {int(timeEnd - timeStart)} seconds")
    else:
        logger.error("Unable to get connection")
