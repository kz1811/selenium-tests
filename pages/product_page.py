from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators
#from .login_page import LoginPage


class ProductPage(BasePage):
    def add_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    def check_price(self):
        price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        return(price.text)

    def check_basket_price(self):
        bkt_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE)
        return(bkt_price.text)

    def check_name_of_product(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        return(product_name.text)

    def check_name_of_added_to_basket_product(self):
        product_name_in_message = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_MESSAGE)
        return(product_name_in_message.text)

    def check_the_prices_of_the_basket_and_the_item_should_be_the_same(self):
        a = self.check_price()
        b = self.check_basket_price()
        assert a in b, f"expected the price in the basket and the price of the item are the same."

    def check_the_names_of_the_item_and_the_alert_should_be_the_same(self):
        a = self.check_name_of_product()
        b = self.check_name_of_added_to_basket_product()
        assert a == b, f"expected the name of current product and the name of the item on alert message are the same."
