from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        CURRENT_URLL = self.browser.current_url
        assert 'login' in CURRENT_URLL, 'incorrect login URL: expected "login" to be substring of URL'

    def should_be_login_form(self):
        assert self.browser.find_element(*LoginPageLocators.LOGIN_FORM_LINK), "Login form is not presented"

    def should_be_register_form(self):
        assert self.browser.find_element(*LoginPageLocators.REGISTER_FORM_LINK), "Register form is not presented"

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL_FIELD).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_FIELD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.SECOND_REGISTER_PASSWORD_FIELD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_SUBMIT_BUTTON).click()
