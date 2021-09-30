from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.ID, "login_link")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini .btn-group .btn:nth-child(1)")

class MainPageLocators():
    pass

class LoginPageLocators():
    LOGIN_FORM_LINK = (By.ID, "login_form")
    REGISTER_FORM_LINK = (By.ID, "register_form")
    REGISTER_EMAIL_FIELD = (By.ID, "id_registration-email")
    REGISTER_PASSWORD_FIELD = (By.ID, "id_registration-password1")
    SECOND_REGISTER_PASSWORD_FIELD = (By.ID, "id_registration-password2")
    REGISTRATION_SUBMIT_BUTTON = (By.NAME, "registration_submit")

class ProductPageLocators():
    BASKET_PRICE = (By.CLASS_NAME, "basket-mini")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    ADD_TO_BASKET_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".alertinner > p > strong")
    PRODUCT_NAME_IN_MESSAGE = (By.CSS_SELECTOR, ".alertinner strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages div:nth-child(1)")

class BasketPageLocators():
    BASKET_ITEM_LINK = (By.ID, "basket_formset")
    BASKET_IS_EMPTY_MESSAGE_LINK = (By.CSS_SELECTOR, "#content_inner p")
