from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.ID, "login_link")
    LOGIN_LINK_INVALID = (By.ID, "login_link_inc")

    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini .btn-group .btn:nth-child(1)")

class MainPageLocators():
    LOGIN_LINK = (By.ID, "login_link")


class LoginPageLocators():
    LOGIN_FORM_LINK = (By.ID, "login_form")
    REGISTER_FORM_LINK = (By.ID, "register_form")

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".alertinner > p > strong")
    BASKET_PRICE = (By.CLASS_NAME, "basket-mini")
    PRODUCT_NAME_IN_MESSAGE = (By.CSS_SELECTOR, ".alertinner strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages div:nth-child(1)")


class BasketPageLocators():
    BASKET_IS_EMPTY_MESSAGE_LINK = (By.CSS_SELECTOR, "#content_inner p")
    BASKET_ITEM_LINK = (By.ID, "basket_formset")
