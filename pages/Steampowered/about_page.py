import re

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from typing import Union
import logging

from pages.Steampowered.base_page import BasePage


class AboutPage(BasePage):
    ONLINE = (By.XPATH, "//div[@class='online_stat'][div[@class='online_stat_label gamers_online']]")
    PLAYING_NOW = (By.XPATH, "//div[@class='online_stat'][div[@class='online_stat_label gamers_in_game']]")

    def __init__(self, driver):
        super().__init__(driver)


    def _extract_numbers(self, locator, label) -> Union[int, None]:
        try:
            logging.info(f"Extract the number of {label} players")
            element = WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(locator)
                                                                     )
            cleaned_element = re.findall(r"\d[\d,]*", element.text)
            cleaned_element_str = "".join(map(str, cleaned_element)).replace(",", "")
            number = int(cleaned_element_str)
            return number
        except TimeoutError:
            logging.warning("No element found")
            return None

    def get_online_players(self):
        return self._extract_numbers(self.ONLINE, 'online')

    def get_playing_now_players(self):
        return self._extract_numbers(self.PLAYING_NOW, 'playing now')

    def validate_players_number(self, online: int, playing_now: int) -> bool:
        logging.info(f"Validate the number of online players is greater than playing_now")
        if online > playing_now:
            logging.info("Online players exceed in-game players.")
            return True
        else:
            logging.error("Invalid state: more players in-game than online.")
            raise ValueError("Playing now cannot exceed online players.")
