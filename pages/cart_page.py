from .base_page import BasePage
from .locators import CartPageLocators


class CartPage(BasePage):
    def sholud_be_empity_basket(self):
        self.should_be_empty_message()
        self.should_be_no_goods_in_basekt()

    def should_be_empty_message(self):
        message_text = self.browser.find_element(*CartPageLocators.BASKET_MESSAGE).text
        print(message_text)
        assert message_text == 'Your basket is empty. Continue shopping', 'Wrong text in basket description'

    def should_be_no_goods_in_basekt(self):
        assert self.is_not_element_present(*CartPageLocators.BASKET_GOODS)
