import os

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import logging

class DemoQAMainPage:
    FIRST_NAME_FIELD = (By.CSS_SELECTOR, "#firstName")
    LAST_NAME_FIELD = (By.CSS_SELECTOR, "#lastName")
    EMAIL_FIELD = (By.CSS_SELECTOR, "#userEmail")
    MALE_RADIO = (By.CSS_SELECTOR, "label[for='gender-radio-1']")
    FEMALE_RADIO = (By.CSS_SELECTOR, "label[for='gender-radio-2']")
    OTHER_RADIO = (By.CSS_SELECTOR, "label[for='gender-radio-3']")
    MOBILE_NUMBER = (By.CSS_SELECTOR, "#userNumber")
    SUBJECT_FIELD = (By.XPATH, "//input[@id='subjectsInput']")
    SPORT_HOBBIES_CHECKBOX = (By.XPATH, "//label[@for='hobbies-checkbox-1']")
    READING_HOBBIES_CHECKBOX = (By.XPATH, "//label[@for='hobbies-checkbox-2']")
    MUSIC_HOBBIES_CHECKBOX = (By.XPATH, "//label[@for='hobbies-checkbox-3']")
    CHOOSE_FILE_BUTTON = (By.XPATH, "//input[@id='uploadPicture']")
    CURRENT_ADDRESS_TEXTAREA = (By.XPATH, "//textarea[@id='currentAddress']")
    STATE_DROPDOWN = (By.XPATH, "//div[@id='state']//div[@class=' css-1wy0on6']")
    CITY_DROPDOWN = (By.XPATH, "//div[@id='city']//div[@class=' css-1wy0on6']")
    SUBMIT_BUTTON = (By.XPATH, "//button[@id='submit']")
    IFRAME = (By.XPATH, "//iframe[contains(@src, 'https://www.google.com/recaptcha/api2/aframe')]")

    REQUIRED_FIELDS = [FIRST_NAME_FIELD, LAST_NAME_FIELD, MOBILE_NUMBER, FEMALE_RADIO, MALE_RADIO, OTHER_RADIO]


    def __init__(self, driver, timeout=5):
        self.driver = driver
        self.timeout = timeout

    def open_page(self, link):
        self.driver.get(link)
        logging.info(f'Open page to link {link}')

    def fill_field(self, locator, data, type):
        element = WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(data)
        logging.info(f"Input {type}: '{data}'")

    def choose_radio(self, locator, type):
        element = WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located(locator)
        )
        element.click()
        logging.info(f'Chose radio button: {type}')

    def choose_file(self, locator, relative_path):
        file_path = os.path.abspath(relative_path)
        upload_file = WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(locator))
        upload_file.send_keys(file_path)
        logging.info(f"Uploaded file from: {file_path}")

    @staticmethod
    def get_state_city_locator(value):
        return (By.XPATH,
                f"//div[@class=' css-26l3qy-menu']//div[text()='{value}']")


    def choose_dropdown_value(self, dropdown_locator, value, type):
        # create locator
        element_locator = DemoQAMainPage.get_state_city_locator(value)
        # dropdown click
        WebDriverWait(self.driver, self.timeout).until(EC.element_to_be_clickable(dropdown_locator)).click()
    #     element click
        WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(
            element_locator)).click()
        logging.info(f"Send {type}: {value}")


    def click_button(self, locator, type):
        element = WebDriverWait(self.driver, self.timeout).until(EC.element_to_be_clickable(locator))
        element.click()
        logging.info(f"Click button: {type}")

    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        logging.info('Scroll down')

    def check_form_submitted_successfully(self):
            WebDriverWait(self.driver, self.timeout).until(
                EC.frame_to_be_available_and_switch_to_it(DemoQAMainPage.IFRAME)
            )

            logging.info('Check that form was fulfilled with valid data and iframe has not appeared')

    def check_form_not_submitted(self):
            WebDriverWait(self.driver, self.timeout).until(
                EC.invisibility_of_element_located(DemoQAMainPage.IFRAME)
            )
            logging.info('Check that form was fulfilled with invalid data and iframe has not appeared')


    def check_field_contains_invalid_value(self, locator):
        email_field = WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(locator))
        actual_border_color = email_field.value_of_css_property("border-color")
        r, g, b = map(int, actual_border_color.strip().replace('rgb(', '').replace(')', '').split(','))
        assert r > g and r > b, f"Expected red border color, but got: {actual_border_color}"
        logging.info(f'Confirm the following field borders are red{locator[1]}')
