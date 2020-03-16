import random

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from selenium.webdriver.support.ui import Select
from .locators import AccountPageLocators


class AccountPage(BasePage):
    def go_to_address_book(self):
        adr_book = self.browser.find_element(*AccountPageLocators.ADDRESS_BOOK)
        adr_book.click()

    def add_new_address(self):
        pagedown = self.browser.find_element(*AccountPageLocators.HTML)
        pagedown.send_keys(Keys.END)
        add_new_address_button = self.browser.find_element(*AccountPageLocators.ADDRESS_ADD_BTN)
        add_new_address_button.click()

        Select(self.browser.find_element(*AccountPageLocators.TITLE)).select_by_value("Mr")
        self.browser.find_element(*AccountPageLocators.FIRST_NAME).send_keys("Иван")
        self.browser.find_element(*AccountPageLocators.LAST_NAME).send_keys("Иванов")
        self.browser.find_element(*AccountPageLocators.ADR_LINE1).send_keys(random.randint(0, 2942))
        self.browser.find_element(*AccountPageLocators.ADR_LINE2).send_keys(random.randint(0, 242))
        self.browser.find_element(*AccountPageLocators.ADR_LINE4).send_keys("Адрес3")
        self.browser.find_element(*AccountPageLocators.STATE).send_keys("Область")
        self.browser.find_element(*AccountPageLocators.POSTCODE).send_keys("190000")
        pagedown2 = self.browser.find_element(*AccountPageLocators.HTML)
        pagedown2.send_keys(Keys.END)
        Select(self.browser.find_element(*AccountPageLocators.COUNTRY)).select_by_value("RU")
        save = self.browser.find_element(*AccountPageLocators.BTN_SAVE_ADR)
        save.click()

    def check_success_message(self):
        assert self.is_element_present(*AccountPageLocators.SUCCESS_SAVE)
