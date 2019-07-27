from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        self.browser.implicitly_wait(5)
        btn = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        btn.click()
        self.solve_quiz_and_get_code()
        self.should_be_description()
        self.should_be_price()
        
    
    def should_be_description(self):
        # assert self.is_element_present(*ProductPageLocators.LOGIN_FORM), 'Login form is not present'
        alert_product_name = self.browser.find_element(*ProductPageLocators.ALERT_PRODUCT_NAME).text
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        assert alert_product_name == product_name, 'Different names in alert and product card'

    def should_be_price(self):
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        assert basket_price == product_price, 'Different prices in alert and product card'

    def should_be_message_of_success_add_to_basket(self):
        assert self.is_not_element_present(*ProductPageLocators.ALERT_ADD_TO_BASKET)

    def should_be_message_disappeared(self):
        assert self.is_diasappeared(*ProductPageLocators.ALERT_ADD_TO_BASKET)
