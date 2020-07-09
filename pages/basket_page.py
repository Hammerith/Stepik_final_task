from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def no_product_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
            "basket items are presented, but shouldn't"

    def basket_empty_message(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY_MSG),\
            "no message that basket is empty"
