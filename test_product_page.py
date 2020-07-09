from .pages.product_page import ProductPage
import time


def test_add_to_basket_get_code(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_add_message()
    page.basket_equal_product_price()
