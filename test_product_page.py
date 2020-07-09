from .pages.product_page import ProductPage
import time
import pytest


@pytest.mark.parametrize('link', [0, 1, 2, 3, 4, 5, 6,
                                  pytest.param(7, marks=pytest.mark.xfail),
                                  8, 9])
def test_add_to_basket_get_code(browser, link):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_20" \
           f"7/?promo=offer{link}"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_add_message()
    page.basket_equal_product_price()
    # time.sleep(120)
