import pandas as pd
import time
from loguru import logger
from database import DataBaseConnector 
import pyodbc

# Obter as credenciais
database_connector = DataBaseConnector()
conexao = database_connector.connect()
timeStart = time.time()

def inserir_dtframe_banco(dataframe):
    if conexao:
        cursor = conexao.cursor()
        
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
            
            try:
                cursor.execute(comando)
                conexao.commit()
                logger.info("Data successfully inserted")
            except pyodbc.IntegrityError as e:
                # Capturar a exceção de violação de chave única
                logger.error(f"Error inserting data: {e}")
                # Decidir como lidar com a exceção, como registrar, pular ou interromper o processamento

        cursor.close()
        conexao.close()
        timeEnd = time.time()
        logger.info(f"Insert data in {int(timeEnd - timeStart)} seconds")
    else:
        logger.error("Unable to get connection")

# Exemplo de uso
if __name__ == "__main__":
    # Carregar DataFrame pandas com os dados a serem inseridos
    inserir_dtframe_banco(dataframe)
