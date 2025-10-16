from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import logging

from pages.Steampowered.base_page import BasePage


class TopSellersPage(BasePage):


    @staticmethod
    def choose_country_locator(value):
        return (By.XPATH, f"//button[contains(@type,'button')]//div[text()='{value}']")


    def select_country(self, value):
        element = TopSellersPage.choose_country_locator(value)
        country = WebDriverWait(self.driver, self.timeout).until(EC.element_to_be_clickable(element))
        country_name = country.text
        if country_name.strip() == value.strip():
            logging.info(f"Option {value} has already selected, skipping click")
        else:
            country.click()
            logging.info(f"Select the following country: {country_name}")


    @staticmethod
    def choose_game_locator(value):
        return f"//tr[@class='_2-RN6nWOY56sNmcDHu069P'][{value}]"

    def get_game_titles(self, indices):

        if isinstance(indices, int):
            indices = [indices]

        titles = []
        for index in indices:
            base_xpath = TopSellersPage.choose_game_locator(index)
            full_xpath = base_xpath + "//div[@class='_1n_4-zvf0n4aqGEksbgW9N']"
            locator = (By.XPATH, full_xpath)
            element = WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(locator))
            titles.append(element.text)

        logging.info(f"Return the following game titles listed on the main page: {titles}")
        return titles


    def get_game_prices(self, indices):

        if isinstance(indices, int):
            indices = [indices]

        prices = []
        for index in indices:
            base_xpath = TopSellersPage.choose_game_locator(index)
            full_xpath = base_xpath + "//div[@class='_3j4dI1yA7cRfCvK8h406OB']"
            locator = (By.XPATH, full_xpath)
            element = WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(locator))
            prices.append(element.text)

        logging.info(f"Return the following game prices listed on the main page: {prices}")
        return prices


    def select_game(self, value):
        xpath = TopSellersPage.choose_game_locator(value)
        locator = (By.XPATH, xpath)
        game = WebDriverWait(self.driver, self.timeout).until(EC.element_to_be_clickable(locator))
        game.click()
        logging.info(f"Select the game number {value} from the list of games")