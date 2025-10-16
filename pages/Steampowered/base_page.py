from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import logging


class BasePage:

    ABOUT_MENU_LINK = (By.XPATH, "//a[contains(@class,'menuitem')][normalize-space()='About']")
    BROWSE_BUTTON = (By.XPATH, "//div[text()='Browse']")
    TOP_SELLER_BUTTON = (By.XPATH, "//span[contains(@class, '_1ELX9bTITFJpYsMBCh_y7F') and text()='Top Sellers']")
    COUNTRY_BUTTON = (By.XPATH, "//button[starts-with(@class, 'DialogDropDown')]")


    def __init__(self, driver, timeout=5):
        self.driver = driver
        self.timeout = timeout

    def open_page(self, link):
        self.driver.get(link)
        logging.info(f"Open page to the link: {link}")


    def click_element(self, locator):
        WebDriverWait(self.driver, self.timeout).until(EC.element_to_be_clickable(locator)).click()
        logging.info(f"Click to the element using locator: {locator}")


    def check_page(self, page_url):
        WebDriverWait(self.driver, self.timeout).until(EC.url_to_be(page_url))
        assert self.driver.current_url == page_url, f'Expected {page_url}'
        logging.info(f"Check the following page is opened: {page_url}")


    def click_link_about(self):
        about_links = self.driver.find_elements(*BasePage.ABOUT_MENU_LINK)
        for link in about_links:
            try:
                WebDriverWait(self.driver, self.timeout).until(EC.element_to_be_clickable(link))
                link.click()
                break
            except:
                continue
        logging.info(f"Go to the page About")
