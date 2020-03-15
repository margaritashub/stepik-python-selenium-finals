from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    product_name = ''
    product_price = ''
    product_description = ''

    def add_product_to_basket_and_calculate(self):
        self.should_be_name()
        self.should_be_price()
        self.should_be_description()
        self.should_be_add_button()

        self.add_product_to_basket()
        self.solve_quiz_and_get_code()
        self.should_be_success()
        self.check_success_message()

    def add_product_to_basket(self):
        btn = self.browser.find_element(*ProductPageLocators.BTN_ADD_TO_BASKET)
        btn.click()

    def is_disappered_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGES), "Wrong show success message"

    def should_be_name(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), "Name of product not found"
        self.product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def should_be_price(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), "Price of product not found"
        self.product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def should_be_description(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_DESCRIPTION), "Description of product not found"
        self.product_description = self.browser.find_element(*ProductPageLocators.PRODUCT_DESCRIPTION).text

    def should_be_success(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGES), "Message of Success added product in " \
                                                                               "basket not found "

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False
    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                    until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGES), "Wrong show success message"

    def should_be_add_button(self):
        assert self.is_element_present(*ProductPageLocators.BTN_ADD_TO_BASKET), "Button 'Add to basket' is not " \
                                                                                "presented "

    def check_success_message(self):
       assert  self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGES)


