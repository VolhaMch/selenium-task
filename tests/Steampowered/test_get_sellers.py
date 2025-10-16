import allure
import pytest

from pages.Steampowered.base_page import BasePage
from pages.Steampowered.personal_game_page import PersonalGamePage
from pages.Steampowered.topsellers_page import TopSellersPage
from utils.config import SteampoweredBasePageConfig


@pytest.mark.parametrize("country, indeces, index, game_number", [
    ("Global", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1], "1"),
])
@allure.description('Get top sellers')
def test_get_sellers(browser, country, indeces, index, game_number):
    page = TopSellersPage(browser)
    personal_game_page = PersonalGamePage(browser)

    with allure.step("Open main page"):
        page.open_page(SteampoweredBasePageConfig.BASE_PAGE_URL)
    with allure.step("Click button browse"):
        page.click_element(BasePage.BROWSE_BUTTON)
    with allure.step("Click top seller button om browse menu"):
        page.click_element(BasePage.TOP_SELLER_BUTTON)
    with allure.step("Check top seller page is opened"):
        page.check_page(SteampoweredBasePageConfig.TOP_SELLING_PAGE)
    with allure.step(f"Click on select country button and choose {country} option"):
        page.select_country(country)
    with allure.step("Get titles of first 10 games in list of all games"):
        page.get_game_titles(indeces)
    with allure.step("Retrieve title and price of chosen game in the list of games from the main page"):
        titles = page.get_game_titles(index)
        title_on_main_page = titles[0]
        prices = page.get_game_prices(index)
        price_on_main_page = prices[0]
    with allure.step("Go to chosen game page"):
        page.select_game(game_number)
    with allure.step("Get game title from personal page"):
        title = personal_game_page.get_game_title()
    with allure.step("Get game price from personal page"):
        price = personal_game_page.get_game_price()
    with allure.step("Confirm chosen game has the same title and price on main page and personal game page"):
        personal_game_page.compare_game_data(title_on_main_page, title)
        personal_game_page.compare_game_data(price_on_main_page, price)
