import os
from dotenv import load_dotenv

load_dotenv()

class SteampoweredBasePageConfig:
    BASE_PAGE_URL = 'https://store.steampowered.com/'
    ABOUT_PAGE = 'https://store.steampowered.com/about/'
    TOP_SELLING_PAGE = 'https://store.steampowered.com/charts/topselling/global'

class DemoQABasePageConfig:
    BASE_PAGE_URL = 'https://demoqa.com/automation-practice-form'
    AUTOMATION_PRACTICE_FORM_URL = 'https://demoqa.com/automation-practice-form'

class SaucedemoConfig:
    LOGIN_PAGE_URL = 'https://www.saucedemo.com/'
    BASE_PAGE_URL = 'https://www.saucedemo.com/inventory.html'
    LOGIN_USERNAME = os.getenv("LOGIN_USERNAME")
    LOGIN_PASSWORD = os.getenv("LOGIN_PASSWORD")
