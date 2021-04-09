import pytest
import time
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage


class TestProductPage:
    def test_guest_should_see_login_link_on_product_page(self, browser):
        link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()

    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    @pytest.mark.skip(reason="So as not to wait")
    @pytest.mark.parametrize('promo', ["?promo=offer0", "?promo=offer1", "?promo=offer2",
                                       "?promo=offer3", "?promo=offer4", "?promo=offer5",
                                       "?promo=offer6", pytest.param("?promo=offer7", marks=pytest.mark.xfail),
                                       "?promo=offer8", "?promo=offer9"])
    def test_guest_can_add_product_to_basket(self, browser, promo):
        link = f"https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/{promo}"
        page = ProductPage(browser, link)
        page.open()
        page.add_product_to_basket()
        page.solve_quiz_and_get_code()
        page.should_be_product_add_to_basket_message()
        page.should_be_price_of_basket()

    @pytest.mark.skip
    def test_message_disappeared_after_adding_product_to_basket(self, browser):
        link = f"https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.add_product_to_basket()
        page.should_be_disappeared_success_message()

    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        link = f"https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.go_to_basket_page()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.should_be_basket_page()
        basket_page.should_not_be_list_of_products()
        basket_page.should_be_basket_is_empty_message()


@pytest.mark.user_on_product_page
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        link = "https://selenium1py.pythonanywhere.com/accounts/login/"
        login_page = LoginPage(browser, link)
        login_page.open()
        email = str(time.time()) + "@fakemail.org"
        password = "fakePas1901"
        login_page.register_new_user(email, password)
        login_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = f"https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    def test_user_can_add_product_to_basket(self, browser):
        link = f"https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
        page = ProductPage(browser, link)
        page.open()
        page.add_product_to_basket()
        page.solve_quiz_and_get_code()
        page.should_be_product_add_to_basket_message()
        page.should_be_price_of_basket()
