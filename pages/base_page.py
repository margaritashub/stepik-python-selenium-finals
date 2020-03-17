from selenium.common.exceptions import NoSuchElementException
from .locators import BasePageLocators
from .locators import BasketPageLocators


class BasePage():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)

    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                     "unauthorised user"

    def go_to_basket(self):
        link = self.browser.find_element(*BasePageLocators.BTN_GO_TO_BASKET)
        link.click()

    def go_to_books_catalogue(self):
        link = self.browser.find_element(*BasePageLocators.BOOKS_CAT)
        link.click()

    def logout(self):
        link = self.browser.find_element(*BasePageLocators.LOGOUT_LINK)
        link.click()

    def go_to_account_page(self):
        link = self.browser.find_element(*BasePageLocators.USER_ICON)
        link.click()

    def get_text(self, how, what):
        try:
            return self.browser.find_element(how, what).text
        except NoSuchElementException:
            return None
