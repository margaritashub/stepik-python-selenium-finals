from .locators import BasePageLocators, BooksPageLocators
from .base_page import BasePage

class BooksPage(BasePage):
    def move_to_book_page(self):
        link = self.browser.find_element(*BooksPageLocators.BOOK_TO_ADD)
        link.click()