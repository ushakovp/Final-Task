from selenium.webdriver.common.by import By


class BasePageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group a.btn.btn-default")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, '.icon-user')


class MainPageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators(object):
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FROM = (By.ID, 'register_form')
    EMAIL_INPUT = (By.ID, 'id_registration-email')
    PASSWORD_INPUT = (By.ID, 'id_registration-password1')
    CONFIRM_PASSWORD_INPUT = (By.ID, 'id_registration-password2')
    REGISTER_BUTTON = (By.NAME, 'registration_submit')


class ProductPageLocators(object):
    ADD_TO_BASKET = (By.CSS_SELECTOR, '.btn-add-to-basket')
    ALERT_PRODUCT_NAME = (By.CSS_SELECTOR, '#messages .alert:first-child strong')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main h1')
    BASKET_PRICE = (By.CSS_SELECTOR, '.alertinner p strong')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
    ALERT_ADD_TO_BASKET = (By.CSS_SELECTOR, '#messages .alert:first-child')


class CartPageLocators(object):
    BASKET_MESSAGE = (By.CSS_SELECTOR, '#content_inner p')
    BASKET_GOODS = (By.CSS_SELECTOR, '#basket_fromset')
