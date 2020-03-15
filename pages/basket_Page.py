from  pages.base_page import BasePage
from pages.locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_basket(self):
        self.should_be_no_goods()
        self.should_be_msg_basket_is_empty()

    def should_be_no_goods(self):
        assert self.is_not_element_present(*BasketPageLocators.GOODS_IN_BASKET)

    def should_be_msg_basket_is_empty(self):
        assert self.browser.find_element(*BasketPageLocators.BASKET_IS_EMPTY).text == "Your basket is empty. " \
                                                                                          "Continue shopping"

    def is_not_element_present(self, param):
        pass

