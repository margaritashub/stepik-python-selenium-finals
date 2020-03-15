from .base_page import BasePage
from selenium.common.exceptions import NoAlertPresentException

from .locators import LoginPageLocators, MainPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):

        current_url = self.browser.current_url
        assert "login" in current_url, f"No login substring in the {current_url}"
        assert True

    def should_be_login_form(self):

        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"
        assert True

    def should_be_register_form(self):

        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"
        assert True

    def go_to_login_page(self):
        link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        link.click()
        # return LoginPage(browser=self.browser, url=self.browser.current_url)

    def register_new_user(self, email, password):
        input_email = self.browser.find_element(*LoginPageLocators.INPUT_EMAIL_FOR_REGISTRATION)
        input_email.send_keys(email)
        input_pwd = self.browser.find_element(*LoginPageLocators.INPUT_PASSWORD_FOR_REGISTRATION)
        input_pwd.send_keys(password)
        repeat_pwd = self.browser.find_element(*LoginPageLocators.REPEAT_PASSWORD_FOR_REGISTRATION)
        repeat_pwd.send_keys(password)
        register_btn = self.browser.find_element(*LoginPageLocators.REGISTER_BTN)
        register_btn.click()

    def authorization (self, email, password):
    input