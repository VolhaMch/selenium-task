import random

import allure
import pytest
from faker import Faker
from selenium.webdriver.support.wait import WebDriverWait

from pages.DemoQA.base_page import DemoQAMainPage
from utils.config import DemoQABasePageConfig




@pytest.fixture()
def demoqa_page(browser):
    page = DemoQAMainPage(browser)
    with allure.step("Open form page"):
        page.open_page(DemoQABasePageConfig.BASE_PAGE_URL)
        return page

@pytest.fixture()
def faker():
    return Faker()

def generate_fake_data(faker):
    first_name = faker.name()[:7]
    last_name = faker.name()[:15]
    email = faker.email()
    mobile_number = '00' + ''.join(faker.random_choices(elements='0123456789', length=8))
    text = faker.word()
    address = faker.address()

    return {
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "mobile_number": mobile_number,
        "text": text,
        "address": address
    }


def generate_invalid_fake_data(faker):

    email = faker.email().replace("@", "")
    mobile_number = '00' + ''.join(faker.random_choices(elements='0123456789', length=3))

    return {
        "email": email,
        "mobile_number": mobile_number,

    }


@pytest.fixture()
def fake_data(faker):
    return generate_fake_data(faker)

@pytest.fixture()
def invalid_faked_data(faker):
    return generate_invalid_fake_data(faker)


@pytest.fixture()
def random_state_city():
    state_city_dict = {
        "NCR": ["Delhi", "Gurgaon", "Noida"],
        "Uttar Pradesh": ["Agra", "Lucknow", "Merrut"],
        "Haryana": ["Karnal", "Panipat"],
        "Rajasthan": ["Jaipur", "Jaiselmer"]
    }

    state = random.choice(list(state_city_dict.keys()))
    city = random.choice(state_city_dict[state])
    return state, city