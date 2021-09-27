from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        CURRENT_URLL = self.browser.current_url
        assert 'login' in CURRENT_URLL, f'expected "login" to be substring of URL'

    def should_be_login_form(self):
        assert self.browser.find_element(*MainPageLocators.LOGIN_FORM_LINK), "Login form is not presented"
        #assert True

    def should_be_register_form(self):
        assert self.browser.find_element(*MainPageLocators.REGISTER_FORM_LINK), "Register form is not presented"
        #assert True
