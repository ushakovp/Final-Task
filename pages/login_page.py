from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert self.is_element_in_url('login'), 'Url does not contain string "login"'

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'Login form is not present'

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FROM), 'Register form is not present'

    def register_new_user(self, email, password):
        input_email = self.browser.find_element(*LoginPageLocators.EMAIL_INPUT)
        input_email.send_keys(email)
        input_pass = self.browser.find_element(*LoginPageLocators.PASSWORD_INPUT)
        input_pass.send_keys(password)
        input_confirm = self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD_INPUT)
        input_confirm.send_keys(password)
        reg_btn = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        reg_btn.click()
