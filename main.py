from loginStrava import fazer_login_strava
from formatData import limpar_e_converter_dataframe
from InsertData import inserir_dataframe_no_banco
from loguru import logger

if __name__ == "__main__":
    logger.info("Started call Login")
    
    try:
        # Realiza o login e o scraping das atividades
        dataframe_sport = fazer_login_strava()
        

        # Verifica se o DataFrame não está vazio
        if not dataframe_sport.empty:
            dataframe_limpo = limpar_e_converter_dataframe(dataframe_sport)
            logger.debug("Yes content, data transform")
           
            # Insere o DataFrame limpo no banco de dados
            inserir_dataframe_no_banco(dataframe_limpo)

        else:
            logger.error("The DataFrame is empty.")

    except Exception as e:
        logger.error(f"An error occurred during the process: {str(e)}")