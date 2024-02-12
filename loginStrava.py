import time
from playwright.sync_api import sync_playwright
from loguru import logger
from getCredential import obter_credenciais
from bs4 import BeautifulSoup
import pandas as pd


def fazer_login_strava():
    timeStart = time.time()
    

    # Chama a função para obter as credenciais
    credenciais, conexao = obter_credenciais()
    logger.debug("Starting access to the website")

    # Verifica se as credenciais foram obtidas com sucesso
    if credenciais:
        email, password = credenciais[0]
        logger.info("Validated email and password")  # Acesse o primeiro elemento da lista de credenciais
    else:
        logger.error("Unable to obtain credentials.")

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
        logger.info(f"Login done at {int(finalTime - timeStart)} seconds")

        logger.info("Inicando o Scraping")
        timeInicioScrap = time.time()
        page.goto("https://www.strava.com/athlete/training")
        time.sleep(3)
        table_html = page.locator('xpath=//*[@id="search-results"]').inner_html()
        logger.debug("Table located on the page")

        soup = BeautifulSoup(table_html, 'html.parser')

        activitys = soup.find_all('tr', attrs={'class': 'training-activity-row'})
        logger.debug("Captured table")

        lista_activitys = []

        for activity in activitys:
            typeActivity = activity.find('td', attrs={'class': 'view-col col-type'})
            dateActivity = activity.find('td', attrs={'class': 'view-col col-date'})
            titleActivity = activity.find('td', attrs={'class': 'view-col col-title'})
            timeActivity = activity.find('td', attrs={'class': 'view-col col-time'})
            distActivity = activity.find('td', attrs={'class': 'view-col col-dist'})
            elevActivity = activity.find('td', attrs={'class': 'view-col col-elev'})
            
            lista_activitys.append([typeActivity.text, dateActivity.text, titleActivity.text, timeActivity.text, distActivity.text, elevActivity.text])

        sport = pd.DataFrame(lista_activitys, columns=['Tipo', 'Data', 'Title', 'Tempo', 'Distancia', 'Elevacao'])
        logger.debug("Add array in Data Frame send to excel")
        sport.to_excel('Activitys.xlsx', index=False)
        timeFinalScrap = time.time()
        logger.info(f'Scraping done in {int(timeFinalScrap - timeInicioScrap)} seconds')
