import time
import pyodbc
from dotenv import load_dotenv
import os
from loguru import logger

load_dotenv()

class DataBaseConnector:
    def __init__(self):
        self.db_host = os.getenv("DB_HOST")
        self.db_user = os.getenv("DB_USER")
        self.db_password = os.getenv("DB_PASSWORD")

    def connect(self):
        time_start = time.time()
        connection_string = (
            f"Driver={{SQL Server}};"
            f"Server={self.db_host};"
            f"Database=ManagerActivity;"
            f"UID={self.db_user};"
            f"PWD={self.db_password};"
            f"Trusted_Connection=yes;"
        )

        try:
            connection = pyodbc.connect(connection_string)
            logger.info("Successful connection!")
            final_time = time.time()
            logger.info(f"Connection made in database {int(final_time - time_start)} seconds")
            return connection
        except pyodbc.Error as e:
            logger.error(f'Error connecting to database: {e}')
            return None

# Exemplo de uso da classe
#if __name__ == "__main__":
    #database_connector = DataBaseConnector()
    #conexao = database_connector.connect()
