import math
import allure
from allure_commons.types import AttachmentType

from config.links import Links
from pages.locators import BasePageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException, TimeoutException, NoSuchElementException

class BasePage:
    def __init__(self, browser):
        self.browser = browser
        self.browser.implicitly_wait(1.0)

    PAGE_URL = Links.HOST

    def open(self, link=""):
        with allure.step(f"Open '{self.PAGE_URL}' page"):
            self.browser.get(self.PAGE_URL)

    def make_screenshot(self, screenshot_name):
        allure.attach(body=self.browser.get_screenshot_as_png(), name=screenshot_name, attachment_type=AttachmentType.PNG)

    def delete_user(self, password):
        self.browser.find_element(*BasePageLocators.USER_ICON).click()
        self.browser.find_element(*BasePageLocators.DELETE_PROFILE_BUTTON).click()
        self.browser.find_element(*BasePageLocators.PASSWORD_INPUT).send_keys(password)
        self.browser.find_element(*BasePageLocators.CONFIRM_DELETION_BUTTON).click()

    def element_is_disappeared(self, how, what, timeout=5):
        try:
            WebDriverWait(self.browser, timeout, 0.5, TimeoutException).until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def go_to_login_page(self):
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()

    def go_to_basekt_page(self):
        basket_link = self.browser.find_element(*BasePageLocators.BASKET_LINK)
        basket_link.click()

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=5):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                     " probably unauthorised user"
