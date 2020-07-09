from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        add_button.click()

    def should_be_add_message(self):
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        success_msg = self.browser.find_element(*ProductPageLocators.SUCCESS_MSG).text
        assert book_name == success_msg, "wrong book name"

    def basket_equal_product_price(self):
        book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text
        assert book_price == basket_price, "wrong price"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MSG),\
            "success message is presented, but shouldn't"

    def message_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MSG), \
            "message not disappeared, but should"
