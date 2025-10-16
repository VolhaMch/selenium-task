from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import logging

from pages.Steampowered.base_page import BasePage


class PersonalGamePage(BasePage):

    GAME_TITLE = (By.XPATH, "//div[@id='appHubAppName']")
    GAME_PRICE = (By.XPATH, "//div[@class='game_purchase_price price']")
    RELEASE_DATE = (By.XPATH, "//div[@class='date']")
    DEVELOPER_NAME = (By.XPATH, "//div[@id='developers_list']//a")


    def compare_game_data(self, value1: str, value2: str):
        assert value1 == value2,  f'Expected {value1} and {value2} are equal'
        logging.info(f"Confirm {value1} is equal to {value2}")

    def get_game_title(self):
        element = WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(
            PersonalGamePage.GAME_TITLE))
        logging.info(f"Return the following game title: {element.text}")
        return element.text

    def get_game_price(self):
        element = WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(
            PersonalGamePage.GAME_PRICE))
        logging.info(f"Return the following game price: {element.text}")
        return element.text

    def get_developer_name(self):
        name = WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(
            PersonalGamePage.DEVELOPER_NAME)).text
        logging.info(f"The name of the developer of a choosen game: {name}")
        return name