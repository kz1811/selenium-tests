from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import BasketPageLocators

class BasketPage(BasePage):

    def should_be_empty_cart_message(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_IS_EMPTY_MESSAGE_LINK), \
            "Empty basket message is not presented, but should be"

    def should_not_be_any_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEM_LINK), \
            "At least one item is presented in the basket, but should not be"
