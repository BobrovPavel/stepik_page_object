from selenium.webdriver.common.by import By


class LoginPageLocators:
    EMAIL_INPUT = (By.ID, "id_registration-email")
    PASSWORD_INPUT = (By.ID, "id_registration-password1")
    CONFIRM_PASSWORD_INPUT = (By.ID, "id_registration-password2")
    SUBMIT_REGISTRATION_BUTTON = (By.NAME, "registration_submit")
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")


class ProductPageLocators:
    ADD_TO_BASKET_BTN = (By.CSS_SELECTOR, ".btn-add-to-basket")
    SUCCESS_TOAST = (By.CSS_SELECTOR, ".alertinner ")
    ITEM_TITLE = (By.CSS_SELECTOR, ".product_main h1")
    BASkET_TOTAL = (By.CSS_SELECTOR, ".navbar-btn.btn-cart")
    ITEM_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")


class BasePageLocators:
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini a")
    DELETE_PROFILE_BUTTON = (By.ID, "delete_profile")
    PASSWORD_INPUT = (By.ID, "id_password")
    CONFIRM_DELETION_BUTTON = (By.CSS_SELECTOR, "#delete_profile_form button")


class BasketPageLocators():
    BASKET_ITEM = (By.CSS_SELECTOR, ".basket-items")
    BASKET_IS_EMPTY_MESSAGE = (By.CSS_SELECTOR, "#content_inner p")
