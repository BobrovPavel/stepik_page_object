import os
import time

import allure
import pytest
from config.data import Data
from pages.base_page import BasePage
from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser)
    page.open()
    page.add_item_to_card()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser)
    page.open()
    page.add_item_to_card()
    page.success_message_should_disappear()


@pytest.mark.login
class TestLoginFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        browser.get(link)
        current_directory = os.getcwd()
        screenshots_directory = os.path.abspath(os.path.join(current_directory, 'tmp', 'screenshots'))

        if not os.path.exists(screenshots_directory):
            os.makedirs(screenshots_directory)
        browser.save_screenshot(f"{screenshots_directory}/{time.time()}.png")

    def test_guest_should_see_login_link_on_product_page(self, browser):
        product_page = ProductPage(browser)
        product_page.should_be_login_link()

    @allure.feature("User can add product to the basket")
    @pytest.mark.need_review
    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        print(f"Start test: 'test_guest_can_go_to_login_page_from_product_page'")
        product_page = ProductPage(browser)
        login_page = LoginPage(browser)
        browser.save_screenshot(f"stepik/tmp/screenshots/{time.time()}.png")
        product_page.go_to_login_page()
        login_page.should_be_login_page()

    @allure.feature("User can add product to the basket")
    @pytest.mark.need_review
    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        print(f"Start test: 'test_guest_cant_see_product_in_basket_opened_from_product_page'")
        product_page = ProductPage(browser)
        product_page.go_to_basekt_page()
        basket_page = BasketPage(browser)
        basket_page.should_be_empty_basket()
        basket_page.should_be_message_that_basket_is_empty()


class TestGuesAddToBasketFromProductPage:

    def test_guest_cant_see_success_message(self, browser):
        page = ProductPage(browser)
        page.open()
        page.should_not_be_success_message()

    @allure.feature("User can add product to the basket")
    @pytest.mark.need_review
    def test_guest_can_add_product_to_basket(self, browser):
        print(f"Start test: 'test_guest_can_add_product_to_basket'")
        page = ProductPage(browser)
        page.open()
        page.add_item_to_card()
        page.item_should_be_added()

@allure.feature("User can add product to the basket")
class TestUserAddToBasketFromProductPage:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        email = str(time.time()) + "@fakemail.org"
        base_page = BasePage(browser)
        login_page = LoginPage(browser)
        login_page.open()
        login_page = LoginPage(browser)
        login_page.register_new_user(email, Data.PASSWORD)
        base_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser)
        page.open()
        page.should_not_be_success_message()

    @allure.title("Registered user adds item to the basket")
    @allure.severity("Critical")
    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        print(f"Start test: 'test_user_can_add_product_to_basket'")
        page = ProductPage(browser)
        page.open()
        page.add_item_to_card()
        page.item_should_be_added()
        page.make_screenshot("Success")
