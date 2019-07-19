from selenium.webdriver.common.by import By


class MainPageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators(object):
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FROM = (By.ID, 'register_form')

class ProductPageLocators(object):
    ADD_TO_BASKET = (By.CSS_SELECTOR, '.btn-add-to-basket')
    ALERT_PRODUCT_NAME = (By.CSS_SELECTOR, '#messages .alert:first-child strong')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main h1')
    BASKET_PRICE = (By.CSS_SELECTOR, '.alertinner p strong')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')