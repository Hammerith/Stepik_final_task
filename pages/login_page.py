from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "There is no login in url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login link is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        email_link = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        password_link = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD)
        password_repeat_link = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_REPEAT)
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        email_link.send_keys(email)
        password_link.send_keys(password)
        password_repeat_link.send_keys(password)
        register_button.click()
