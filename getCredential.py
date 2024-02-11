import pyodbc
import time
from loguru import logger
from connectDB import BancoDados
timeStart = time.time()

conexao = BancoDados()

if conexao:
    logger.info(f"Started Get credential in {conexao} seconds")
    cursor = conexao.cursor()

    comando = """SELECT * FROM CredentialView;"""
    cursor.execute(comando)

    resultados = cursor.fetchall()

    # Listas para armazenar todas as credenciais
    credenciais = []

    for linha in resultados:
        email = linha[0]
        password = linha[1]
        logger.info(email)
        credenciais.append((email, password))

    # Não fechar a conexão aqui

    # Retorna todas as credenciais
    # return credenciais, conexao
else:
    logger.error("Erro de conexão com o banco de dados.")
if __name__ == "__main__":
    timeStart = time.time()
    finalTime = time.time()
    logger.info(f"Get credential in {int(finalTime - timeStart)} seconds")