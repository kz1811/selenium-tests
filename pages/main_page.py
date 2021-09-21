from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators
from .login_page import LoginPage

class MainPage(BasePage):
    def go_to_login_page(self):
        log_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        log_link.click()
        #return LoginPage(browser=self.browser, url=self.browser.current_irl)

    def should_be_login_link(self):
        assert self.browser.find_element(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
