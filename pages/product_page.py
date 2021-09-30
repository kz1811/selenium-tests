from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators
#from .login_page import LoginPage


class ProductPage(BasePage):
    def add_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()

    def get_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def get_basket_price(self):
        return self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text

    def get_name_of_product(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def get_name_of_added_to_basket_product(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_MESSAGE).text

    def check_the_prices_of_the_basket_and_the_item_should_be_the_same(self):
        assert self.get_price() in self.get_basket_price(), "Prices of added product and the product are unequal."

    def check_the_names_of_the_item_and_the_alert_should_be_the_same(self):
        assert self.get_name_of_product() == self.get_name_of_added_to_basket_product(), "Names of added product and the product are unequal."

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be."

    def should_dissapear_of_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is not dissapear, but should be."
