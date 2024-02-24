from playwright.sync_api import sync_playwright
from credential import CredenciaisManager
from bs4 import BeautifulSoup
from loguru import logger
import pandas as pd
import time


class StravaScraper:

    def __init__(self):
        cred_manager = CredenciaisManager()
        self.credentials, _ = cred_manager.obter_credenciais()

    def strava_activities(self):
        time_start = time.time()

        logger.debug("Starting website access")

        if self.credentials:
            email, password = self.credentials[0]
            logger.info("Email and password validated")
        else:
            logger.error("Unable to obtain credentials.")

        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            page.goto("https://www.strava.com/login")
            page.fill('xpath=//*[@id="email"]', email)
            page.fill('xpath=//*[@id="password"]', password)
            page.click('xpath=//*[@id="login-button"]')
            logger.info("Login successful")

            logger.info("Starting scraping")
            page.goto("https://www.strava.com/athlete/training")
            page.wait_for_selector('xpath=//*[@id="search-results"]')

            table_html = page.inner_html('xpath=//*[@id="search-results"]')
            soup = BeautifulSoup(table_html, 'html.parser')

            activities_list = []
            activities = soup.find_all('tr', attrs={'class': 'training-activity-row'})
            for activity in activities:
                type_activity = activity.find('td', attrs={'class': 'view-col col-type'}).text
                date_activity = activity.find('td', attrs={'class': 'view-col col-date'}).text
                title_activity = activity.find('td', attrs={'class': 'view-col col-title'}).text
                time_activity = activity.find('td', attrs={'class': 'view-col col-time'}).text
                dist_activity = activity.find('td', attrs={'class': 'view-col col-dist'}).text
                elev_activity = activity.find('td', attrs={'class': 'view-col col-elev'}).text
                activities_list.append([type_activity, date_activity, title_activity, time_activity, dist_activity, elev_activity])

            sport = pd.DataFrame(activities_list, columns=['Type', 'Date', 'Title', 'Time', 'Distance', 'Elevation'])
            time_end = time.time()
            logger.info(f'Scraping completed in {int(time_end - time_start)} seconds')

        return sport

if __name__ == "__main__":
    scraper = StravaScraper()
    activities = scraper.strava_activities()
