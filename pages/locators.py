from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_BUTTON = (By.CSS_SELECTOR, ".basket-mini a.btn.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators:
    pass


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_ADDRESS_REGISTER_TEXTFIELD = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD_REGISTER_TEXTFIELD = (By.CSS_SELECTOR, "#id_registration-password1")
    CONFIRM_PASSWORD_REGISTER_TEXTFIELD = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "#register_form .btn-lg")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success:nth-child(1) .alertinner")
    SUCCESS_MESSAGE_BOOK_NAME = (By.CSS_SELECTOR, ".alert-success:nth-child(1) strong")
    SUCCESS_MESSAGE_BOOK_PRICE = (By.CSS_SELECTOR, ".alert-info strong")
    BOOK_NAME = (By.CSS_SELECTOR, ".product_main h1")
    BOOK_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")


class BasketPageLocators:
    BASKET_ITEM = (By.CSS_SELECTOR, ".basket-items")
    EMPTY_BASKET_MESSAGE = (By.XPATH, "//p[contains(text(), 'empty')]")


