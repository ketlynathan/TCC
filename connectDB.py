import time
import pyodbc
from loguru import logger
timeStart = time.time()

def BancoDados():
    dadosConexao = (
        r"Driver={SQL Server};"
        r"Server=GIGANTE_SEGURO\SQLKEH;"
        r"Database=ManagerActivity;"
        r"Trusted_Connection=yes;"
    )

    try:
        conexao = pyodbc.connect(dadosConexao)
        logger.info("successful connection!")
        return conexao

    except pyodbc.Error as e:
        logger.error(f'Error connecting to database: {e}')
        return None
finalTime = time.time()
logger.info(f"Connection made in database  {int(finalTime - timeStart)} seconds")