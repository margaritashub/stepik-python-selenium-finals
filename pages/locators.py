from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    INPUT_EMAIL_FOR_REGISTRATION = (By.NAME, "registration-email")
    INPUT_PASSWORD_FOR_REGISTRATION = (By.NAME, "registration-password1")
    REPEAT_PASSWORD_FOR_REGISTRATION = (By.NAME, "registration-password2")
    REGISTER_BTN = (By.NAME, "registration_submit")
    USERNAME_LOGIN = (By.NAME, "login-username")
    PASSWORD_LOGIN = (By.NAME, "login-password")
    BTN_LOGIN = (By.NAME, "login_submit")
    SUCCESS_LOGIN = (By.CSS_SELECTOR, ".alertinner wicon")

class ProductPageLocators:
    BTN_ADD_TO_BASKET = (By.CSS_SELECTOR, ".product_main form button.btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main p.price_color")
    PRODUCT_DESCRIPTION = (By.CSS_SELECTOR, "#product_description+p")
    SUCCESS_MESSAGES = (By.CSS_SELECTOR, ".alertinner strong")
    REVIEW_BTN = (By.ID, "write_review")
    REVIEW_TITLE = (By.ID, "id_title")
    REVIEW_BODY = (By.ID, "id_body")
    REVIEW_BTN_ADD = (By.CSS_SELECTOR, '#add_review_form button')
    FIVE_STAR_RATING = (By.CSS_SELECTOR, ".star-rating:nth-child(5)")
class BasePageLocators():
    BTN_GO_TO_BASKET = (By.CSS_SELECTOR, '.btn-group a.btn-default')
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    BOOKS_CAT = (By.CSS_SELECTOR, '#browse .dropdown-submenu')
    LOGOUT_LINK = (By.CSS_SELECTOR, "#logout_link")

class BasketPageLocators:

    GOODS_IN_BASKET = (By.CSS_SELECTOR, "#content_inner div.basket-title div.row")
    BASKET_IS_EMPTY = (By.CSS_SELECTOR, "#content_inner p")
    QTY_INPUT = (By.NAME, "form-0-quantity")
    QTY_BTN = (By.CSS_SELECTOR, ".input-group-btn")

class BooksPageLocators:
    BOOK_TO_ADD = (By.LINK_TEXT, "Hacking Exposed Wireless")

class AccountPageLocators:
    ADDRESS_BOOK = (By.PARTIAL_LINK_TEXT, "Address")
    ADDRESS_ADD_BTN = (By.CLASS_NAME, 'btn-primary')
    TITLE = (By.ID, 'id_title')
    FIRST_NAME = (By.NAME, 'first_name')
    LAST_NAME = (By.NAME, 'last_name')
    ADR_LINE1 = (By.ID, "id_line1")
    ADR_LINE2 = (By.ID, "id_line2")
    ADR_LINE4 = (By.NAME, "line4")
    STATE = (By.NAME, 'state')
    POSTCODE = (By.NAME, 'postcode')
    HTML = (By.TAG_NAME, 'html')
    COUNTRY = (By.NAME, 'country')
    BTN_SAVE_ADR = (By.CSS_SELECTOR, '.btn-lg')
    SUCCESS_SAVE = (By.CSS_SELECTOR, ".alert-success")

