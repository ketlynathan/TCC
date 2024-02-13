import time
from playwright.sync_api import sync_playwright
from loguru import logger
from getCredential import obter_credenciais
from bs4 import BeautifulSoup
import pandas as pd


def fazer_login_strava():
    # Tempo de início
    time_start = time.time()

    # Obter credenciais
    credenciais, conexao = obter_credenciais()
    logger.debug("Iniciando acesso ao site")

    if credenciais:
        email, password = credenciais[0]
        logger.info("E-mail e senha validados")
    else:
        logger.error("Não foi possível obter as credenciais.")

    # Iniciar navegador
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("https://www.strava.com/login")
        page.fill('xpath=//*[@id="email"]', email)
        page.fill('xpath=//*[@id="password"]', password)
        page.click('xpath=//*[@id="login-button"]')
        logger.info("Login realizado")

        # Scraping das atividades
        logger.info("Iniciando o scraping")
        page.goto("https://www.strava.com/athlete/training")

        # Esperar até que a tabela de atividades seja carregada
        page.wait_for_selector('xpath=//*[@id="search-results"]')

        # Extrair HTML da tabela
        table_html = page.inner_html('xpath=//*[@id="search-results"]')
        soup = BeautifulSoup(table_html, 'html.parser')

        # Extrair dados das atividades
        lista_activitys = []
        activitys = soup.find_all('tr', attrs={'class': 'training-activity-row'})
        for activity in activitys:
            typeActivity = activity.find('td', attrs={'class': 'view-col col-type'}).text
            dateActivity = activity.find('td', attrs={'class': 'view-col col-date'}).text
            titleActivity = activity.find('td', attrs={'class': 'view-col col-title'}).text
            timeActivity = activity.find('td', attrs={'class': 'view-col col-time'}).text
            distActivity = activity.find('td', attrs={'class': 'view-col col-dist'}).text
            elevActivity = activity.find('td', attrs={'class': 'view-col col-elev'}).text
            lista_activitys.append([typeActivity, dateActivity, titleActivity, timeActivity, distActivity, elevActivity])

        # Criar DataFrame
        sport = pd.DataFrame(lista_activitys, columns=['Tipo', 'Data', 'Title', 'Tempo', 'Distancia', 'Elevacao'])

        # Tempo final
        time_end = time.time()
        logger.info(f'Scraping concluído em {int(time_end - time_start)} segundos')

    return sport

