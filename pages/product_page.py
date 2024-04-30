from config.links import Links
from pages.base_page import BasePage
from pages.locators import ProductPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductPage(BasePage):

    PAGE_URL = Links.PRODUCT_PAGE

    def add_item_to_card(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN).click()
        if "promo" in self.browser.current_url:
            self.solve_quiz_and_get_code()
        WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(ProductPageLocators.SUCCESS_TOAST))

    def success_message_is_correct(self):
        success_message = self.browser.find_element(*ProductPageLocators.SUCCESS_TOAST).text
        item_name = self.browser.find_element(*ProductPageLocators.ITEM_TITLE).text
        assert item_name in success_message, f"The message was expected to contains the item name.\n Message: '{success_message}', Item name: '{item_name}'"

    def item_price_is_equal_basket_total(self):
        item_price = self.browser.find_element(*ProductPageLocators.ITEM_PRICE).get_attribute("textContent")
        basket_price = self.browser.find_element(*ProductPageLocators.BASkET_TOTAL).get_attribute("textContent")
        assert item_price in basket_price, f"Prices expected to be equal:\n Item price: '{item_price}', Basket price '{basket_price}'"

    def item_should_be_added(self):
        self.success_message_is_correct()
        self.item_price_is_equal_basket_total()

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_TOAST), \
            "Success message is presented, but should not be"

    def success_message_should_disappear(self):
        assert self.element_is_disappeared(*ProductPageLocators.SUCCESS_TOAST), "Message isn't disappeared"
