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
        logger.info("Conexão bem sucedida!")
        return conexao

    except pyodbc.Error as e:
        logger.error(f'Erro ao conectar ao banco de dados: {e}')
        return None

if __name__ == "__main__":
    timeStart = time.time()
    conexao = BancoDados()
    finalTime = time.time()
    logger.info(f"Conexão feita ao DB em {int(finalTime - timeStart)} segundos")
    