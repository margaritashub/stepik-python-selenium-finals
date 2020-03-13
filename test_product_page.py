from selenium.webdriver.common.by import By

from pages.product_page import ProductPage


#def test_guest_can_add_product_to_basket(browser):
  # link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
  # page = ProductPage(browser, link)
  # page.open()
  # page.add_product_to_basket()

def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser,
                       link)
    page.open()
    page.add_product_to_basket()
    page.is_not_element_present(By.CSS_SELECTOR, ".alertinner strong")

def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser,link)
    page.open()
    page.is_not_element_present(By.CSS_SELECTOR, ".alertinner strong")

def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.is_disappeared(By.CSS_SELECTOR, ".alertinner strong")