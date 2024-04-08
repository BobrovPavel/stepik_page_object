from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEM), "The basket doesn't seem to be empty"

    def should_be_message_that_basket_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_IS_EMPTY_MESSAGE), f"Missing message that the basket is empty\n" \
                                                                                     f"Element located at {BasketPageLocators.BASKET_IS_EMPTY_MESSAGE}" \
                                                                                     f" was expected to be presented on the page"
