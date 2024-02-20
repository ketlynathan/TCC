from loginStrava import StravaScraper
from formatData import limpar_converter_dataframe
from InsertData import InserirDataframeNoBanco
from loguru import logger

if __name__ == "__main__":
    logger.info("Starting to obtain credentials...")

    try:
        # Realiza o scraping das atividades do Strava
        scraper = StravaScraper()
        dataframe_sport = scraper.scrape_strava_activities()

        # Verifica se o DataFrame não está vazio
        if not dataframe_sport.empty:
            logger.info("Data obtained successfully. Starting cleaning and conversion.")
            
            # Limpa e converte os dados
            dataframe_limpo = limpar_converter_dataframe(dataframe_sport)

            # Insere os dados limpos no banco de dados
            InserirDataframeNoBanco(dataframe_limpo)
            logger.info("Data inserted into the database successfully.")

        else:
            logger.error("The DataFrame is empty.")

    except Exception as e:
        logger.error(f"An error occurred during the process: {str(e)}")
