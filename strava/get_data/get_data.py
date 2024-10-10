from scrape_data import StravaScraper
from playwright.sync_api import sync_playwright
from trans_data import limpar_converter_dataframe
from InsertData import inserir_dtframe_banco
from loguru import logger

if __name__ == "__main__":
    logger.info("Starting to obtain credentials...")

    try:
        # Criando uma instância de StravaScraper
        scraper = StravaScraper()

        # Chamando o método para fazer scraping das atividades do Strava
        dataframe_sport = scraper.strava_activities()

        # Verificando se o DataFrame não está vazio
        if not dataframe_sport.empty:
            logger.info("Data obtained successfully. Starting cleaning and conversion.")
            
            # Limpa e converte os dados
            dataframe_limpo = limpar_converter_dataframe(dataframe_sport)
            logger.info(dataframe_limpo)
            

            # Insere os dados limpos no banco de dados
            inserir_dtframe_banco(dataframe_limpo)
            logger.info("Data inserted into the database successfully.")
            logger.warning(dataframe_limpo)

        else:
            logger.error("The DataFrame is empty.")

    except Exception as e:
        logger.error(f"An error occurred during the process: {str(e)}")

