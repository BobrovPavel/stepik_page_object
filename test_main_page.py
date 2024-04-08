import time

from selenium.webdriver.common.by import By

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



