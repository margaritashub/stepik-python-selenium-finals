from pages.account_page import AccountPage
from pages.basket_page import BasketPage
from pages.books_page import BooksPage
from pages.main_page import MainPage
from pages.login_page import LoginPage
import pytest

from pages.product_page import ProductPage


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty_basket()

@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()

    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com"
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()


# @pytest.mark.need_review_custom_scenarios
def test_guest_can_add_books_to_basket_and_delete(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_books_catalogue()
    books_page = BooksPage(browser, browser.current_url)
    books_page.move_to_book_page()
    product_page = ProductPage(browser, browser.current_url)
    product_page.add_product_to_basket()
    product_page.should_be_success()
    product_page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.set_goods_amount(0)
    basket_page.should_be_msg_basket_is_empty()

@pytest.mark.need_review_custom_scenarios3
def test_user_can_add_address(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()
    login_page.authorization()
    login_page.go_to_account_page()
    acc_page = AccountPage(browser, browser.current_url)
    acc_page.open()
    acc_page.go_to_address_book()
    acc_page.add_new_address()
    acc_page.check_success_message()
    acc_page.logout()
@pytest.mark.need_review_custom_scenarios4
def test_normal_site_offer(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_books_catalogue()
    books_page = BooksPage(browser, browser.current_url)
    books_page.move_to_book_page()
    product_page = ProductPage(browser, browser.current_url)
    product_page.add_product_to_basket()
    product_page.should_be_success()
    product_page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.set_goods_amount(3)
    basket_page.normal_site_offer_assert()
