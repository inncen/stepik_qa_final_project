from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()

    def should_be_product_add_to_basket_message(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_ADD_TO_BASKET), \
            "No message about adding to basket"
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        name_in_message = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_FROM_MESSAGE).text
        assert product_name == name_in_message, "Incorrect product name in message about adding to basket"

    def should_be_price_of_basket(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_PRICE_OF_BASKET), \
            "No message about price of basket"
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        price_in_message = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_FROM_MESSAGE).text
        assert product_price == price_in_message, "Incorrect price in message with total price of basket"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_ADD_TO_BASKET), \
            "Success message is presented, but should not be"

    def should_be_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.MESSAGE_ADD_TO_BASKET), \
            "Success message is not disappeared"
