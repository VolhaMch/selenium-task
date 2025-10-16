import allure
import pytest

from pages.Saucedemo.base_page import SaucedemoPage
from utils.config import SaucedemoConfig


@pytest.fixture()
def sausedemo_page(browser):
    page = SaucedemoPage(browser)
    with allure.step("Open form page"):
        page.open_page(SaucedemoConfig.LOGIN_PAGE_URL)
        return page
