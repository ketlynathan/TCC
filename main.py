from loginStrava import fazer_login_strava
from loguru import logger

logger.info("Started call Login")
if __name__ == "__main__":
    # Realiza o login e o scraping das atividades
    fazer_login_strava()
