import time
import pyodbc
from loguru import logger
timeStart = time.time()


def obter_credenciais_e_usuarios():
    dadosConexao = (
        r"Driver={SQL Server};"
        r"Server=GIGANTE_SEGURO\SQLKEH;"
        r"Database=ManagerActivity;"
        r"Trusted_Connection=yes;"
    )

    try:
        conexao = pyodbc.connect(dadosConexao)
        print("Conexão bem sucedida!")
        return  conexao

    except pyodbc.Error as e:
        print(f'Erro ao conectar ao banco de dados: {e}')
        return None, None, None

finalTime= time.time()
logger.info(f"Canexão feita ao DB\n{int(timeStart - finalTime)}-segundos")
