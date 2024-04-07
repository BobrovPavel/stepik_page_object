from selenium.webdriver.common.by import By
from pages.locators import LoginPageLocators
from .base_page import BasePage

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        url = self.browser.current_url
        assert "login" in url, "There's no 'login' in the current url"

    def should_be_login_form(self):
        login_from = self.browser.find_element(*LoginPageLocators.LOGIN_FORM)
        assert login_from.is_displayed(), "There's no Login form"

    def should_be_register_form(self):
        login_from = self.browser.find_element(*LoginPageLocators.REGISTER_FORM)
        assert login_from.is_displayed(), "There's no Register form"
