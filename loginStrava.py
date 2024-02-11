import time
from playwright.sync_api import sync_playwright
from loguru import logger
from getCredential import obter_credenciais

def fazer_login_strava():
    timeStart = time.time()

    # Chama a função para obter as credenciais
    credenciais, conexao = obter_credenciais()
    logger.debug("Iniciando o acesso ao site")

    # Verifica se as credenciais foram obtidas com sucesso
    if credenciais:
        email, password = credenciais[0]
        logger.info(email)  # Acesse o primeiro elemento da lista de credenciais
    else:
        logger.error("Não foi possível obter as credenciais.")

    # Verificar se as credenciais foram obtidas com sucesso
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        time.sleep(5)
        page = browser.new_page()
        page.goto("https://www.strava.com/login")
        page.locator('xpath=//*[@id="email"]').click()
        page.fill('xpath=//*[@id="email"]', email)
        time.sleep(3)
        page.locator('xpath=//*[@id="password"]').click()
        page.fill('xpath=//*[@id="password"]', password)
        time.sleep(3)
        page.locator('xpath=//*[@id="login-button"]').click()
        logger.info("Login realizado")

    finalTime = time.time()
    logger.info(f"Login feito em  {int(finalTime - timeStart)} segundos")

if __name__ == "__main__":
    fazer_login_strava()
