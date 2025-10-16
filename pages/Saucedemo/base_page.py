import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SaucedemoPage:
    USER_NAME_FIELD = (By.CSS_SELECTOR, '#user-name')
    PASSWORD_FIELD = (By.CSS_SELECTOR, '#password')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '#login-button')
    SORT = (By.XPATH, "//select[@class='product_sort_container']")
    PRICE_HIGHT_TO_LOW = (By.XPATH, "//option[@value='hilo']")
    PRICE_LOW_TO_HIGHT = (By.XPATH, "//option[@value='lohi']")
    ACTIVE_OPTION_ZONE = (By.CSS_SELECTOR, '.active_option')


    def __init__(self, driver, timeout=5):
        self.driver = driver
        self.timeout = timeout

    def open_page(self, link):
        self.driver.get(link)
        logging.info(f'Open page to link {link}')

    def check_page(self, page_url):
        WebDriverWait(self.driver, self.timeout).until(EC.url_to_be(page_url))
        logging.info("Check if correct page opened")
        assert self.driver.current_url == page_url, f'Expected {page_url}'

    def login(self, name, password):
        WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(SaucedemoPage.USER_NAME_FIELD)
                                                       ).send_keys(name)
        WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(SaucedemoPage.PASSWORD_FIELD)
                                                       ).send_keys(password)
        WebDriverWait(self.driver, self.timeout).until(EC.element_to_be_clickable(SaucedemoPage.LOGIN_BUTTON)
                                                       ).click()
        logging.info("User login")


    def sort_product(self, value, type):
        WebDriverWait(self.driver, self.timeout).until(EC.element_to_be_clickable(SaucedemoPage.SORT)
                                                       ).click()

        WebDriverWait(self.driver, self.timeout).until(EC.element_to_be_clickable(value)
                                                       ).click()
        logging.info(f"Checking sort product by selected cathegory: {type}")


    def check_correct_sort(self, expected_text):
        actual_text = WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(
            SaucedemoPage.ACTIVE_OPTION_ZONE)
        ).text
        logging.info(f"Checking sort text: expected '{expected_text}', got '{actual_text}'")
        assert actual_text == expected_text, f'Expected {expected_text}, but got {actual_text}'






