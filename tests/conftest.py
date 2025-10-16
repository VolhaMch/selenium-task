import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def browser():
    # path to driver
    service = Service(ChromeDriverManager().install())
    # browser behavior
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--incognito")

    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()