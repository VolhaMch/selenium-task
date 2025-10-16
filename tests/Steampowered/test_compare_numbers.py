import allure

from pages.Steampowered.about_page import AboutPage
from utils.config import SteampoweredBasePageConfig

@allure.description('The test validates if the number of online players is greater that the number of playing now users')
def test_compare_number(browser):
    page = AboutPage(browser)
    with allure.step("Open main page"):
        page.open_page(SteampoweredBasePageConfig.BASE_PAGE_URL)
    with allure.step("Click to the link 'about'"):
        page.click_link_about()
    with allure.step("Check about page is opened"):
        page.check_page(SteampoweredBasePageConfig.ABOUT_PAGE)
    with allure.step("Extract the number of online and playing now gamers"):
        online = page.get_online_players()
        playing_now = page.get_playing_now_players()
    with allure.step("Validate the number of online players is greater than playing_now"):
        assert page.validate_players_number(online, playing_now), "Playing now cannot exceed online players"
