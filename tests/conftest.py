import os

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
    options.add_argument("--headless")
    options.add_argument("--start-maximized")
    options.add_argument("--incognito")
    options.add_argument("--no-sandbox")        # for Docker
    options.add_argument("--disable-dev-shm-usage")  # for Docker

    # путь внутри Linux‑системы или Docker‑контейнера, куда ставится бинарник chromedriver
    chromedriver_path = "/usr/bin/chromedriver"
    if os.path.exists(chromedriver_path):
        service = Service(chromedriver_path)
    else:
        # use webdriver_manager
        service = Service(ChromeDriverManager().install())

    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()