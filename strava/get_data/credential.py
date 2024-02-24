from loguru import logger
import time
from database import DataBaseConnector

class CredenciaisManager:
    def __init__(self):
        self.database_connector = DataBaseConnector()

    def obter_credenciais(self):
        conexao = self.database_connector.connect()
        timestart = time.time()

        if conexao:
            logger.info("Starting to obtain credentials...")
            cursor = conexao.cursor()
            comando = """SELECT * FROM CredentialView;"""
            cursor.execute(comando)
            resultados = cursor.fetchall()

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

#if __name__ == "__main__":
    #cred_manager = CredenciaisManager()
    #cred_manager.obter_credenciais()
