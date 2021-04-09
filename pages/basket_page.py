from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_page(self):
        self.should_be_basket_page_url()

    def should_be_basket_page_url(self):
        assert "basket" in self.browser.current_url, "Basket page url is not correct"

    def should_be_basket_form(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_FORM), \
            "Basket form is not presented"

    def should_not_be_list_of_products(self):
        assert self.is_not_element_present(*BasketPageLocators.LIST_OF_PRODUCTS_IN_BASKET), \
            "List of products is presented"

    def should_be_basket_is_empty_message(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_IS_EMPTY_MESSAGE), \
            "Basket is empty message is not presented"
