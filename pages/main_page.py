from selenium.webdriver.common.by import By
from pages.locators import MainPageLocators
from pages.base_page import BasePage

class MainPage(BasePage):
    def __init__(self, browser, url):
        super().__init__(browser, url)
