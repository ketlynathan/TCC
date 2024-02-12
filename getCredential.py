import time
from loguru import logger
from connectDB import BancoDados
timestart = time.time()

def obter_credenciais():
    conexao = BancoDados()
    

    if conexao:
        
        logger.info("Starting to obtain credentials...")
        cursor = conexao.cursor()
        comando = """SELECT * FROM CredentialView;"""
        cursor.execute(comando)
        resultados = cursor.fetchall()

        # Listas para armazenar todas as credenciais
        credenciais = []

        for linha in resultados:
            email = linha[0]
            password = linha[1]
            logger.info(f"E-mail encontrado: {email}")
            credenciais.append((email, password))
        
        return credenciais, conexao
    else:
        logger.error("Database connection error.")
        return None, None
finalTime = time.time()
logger.info(f"Get credential in  {int(finalTime - timestart)} seconds")