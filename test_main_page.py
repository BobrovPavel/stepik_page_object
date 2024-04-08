import time

from selenium.webdriver.common.by import By

from pages.basket_page import BasketPage
from pages.product_page import ProductPage
from pages.main_page import MainPage
from pages.login_page import LoginPage

def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, "http://selenium1py.pythonanywhere.com/")
    login_page = LoginPage(browser, "http://selenium1py.pythonanywhere.com/")
    page.open()
    page.go_to_login_page()
    login_page.should_be_login_page()

def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    main_page = MainPage(browser, link)
    main_page.open()
    main_page.go_to_basekt_page()
    basket_page = BasketPage(browser, link)
    basket_page.should_be_empty_basket()
    basket_page.should_be_message_that_basket_is_empty()



