from pages.base_page import BasePage
from pages.locators import BasketPageLocators, AccountPageLocators
from selenium.webdriver.common.keys import Keys

class BasketPage(BasePage):
    def should_be_empty_basket(self):
        self.should_be_no_goods()
        self.should_be_msg_basket_is_empty()

    def should_be_no_goods(self):
        assert self.browser.is_not_element_present(*BasketPageLocators.GOODS_IN_BASKET)

    def should_be_msg_basket_is_empty(self):
        assert self.get_text(*BasketPageLocators.BASKET_IS_EMPTY).find("is empty") > 0, "basket is not empty"


    def set_goods_amount(self, quantity):
        number = self.browser.find_element(*BasketPageLocators.QTY_INPUT)
        number.clear()
        number.send_keys(quantity)
        btn = self.browser.find_element(*BasketPageLocators.QTY_BTN)
        btn.click()

    def normal_site_offer_assert(self):
        pagedown2 = self.browser.find_element(*AccountPageLocators.HTML)
        pagedown2.send_keys(Keys.END)
        assert self.get_text(*BasketPageLocators.OFFER_TYPE).find("Normal site offer") > 0,  'wrong site offer'