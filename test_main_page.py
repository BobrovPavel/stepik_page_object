import pytest
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage

@pytest.mark.login_guest
class TestLoginFromMainPage:
    def test_guest_should_see_login_link(self, browser):
        page = MainPage(browser)
        page.open()
        page.should_be_login_link()

    def test_guest_can_go_to_login_page(self, browser):
        page = MainPage(browser)
        login_page = LoginPage(browser)
        page.open()
        page.go_to_login_page()
        login_page.should_be_login_page()

    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):
        main_page = MainPage(browser)
        main_page.open()
        main_page.go_to_basekt_page()
        basket_page = BasketPage(browser)
        basket_page.should_be_empty_basket()
        basket_page.should_be_message_that_basket_is_empty()



