from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):

    def enter_email(self, email):
        email_input = self.browser.find_element(*LoginPageLocators.EMAIL_INPUT)
        email_input.send_keys(email)

    def enter_password(self, password):
        password_input = self.browser.find_element(*LoginPageLocators.PASSWORD_INPUT)
        password_input.send_keys(password)

    def confirm_password(self, password):
        confirm_password_input = self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD_INPUT)
        confirm_password_input.send_keys(password)

    def click_submit_registration_button(self):
        submit_button = self.browser.find_element(*LoginPageLocators.SUBMIT_REGISTRATION_BUTTON)
        submit_button.click()

    def register_new_user(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.confirm_password(password)
        self.click_submit_registration_button()

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
