import allure


from pages.Saucedemo.base_page import SaucedemoPage
from utils.config import SaucedemoConfig


@allure.description('Confirm that selected sort type is visible and accurate in the active filter display')
def test_sort_products(sausedemo_page):
    page = sausedemo_page
    with allure.step("Login user"):
        page.login(SaucedemoConfig.LOGIN_USERNAME, SaucedemoConfig.LOGIN_PASSWORD)
    with allure.step("Check if user page is opened"):
        page.check_page(SaucedemoConfig.BASE_PAGE_URL)
    with allure.step("Soft product 'from low to hight'"):
        page.sort_product(SaucedemoPage.PRICE_LOW_TO_HIGHT, 'from low to high')
    with allure.step("Check if chosen filter option 'from low to hight' is visible on filter"):
        page.check_correct_sort('Price (low to high)')
