from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_invalid")
    BASKET_LINK = (By.XPATH, "//div[contains(@class, 'basket-mini')]/span/a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CLASS_NAME, "login_form")
    REGISTER_FORM = (By.CLASS_NAME, "register_form")
    REGISTRATION_EMAIL = (By.ID, "id_registration-email")
    REGISTRATION_PASSWORD = (By.ID, "id_registration-password1")
    REGISTRATION_PASSWORD_CONFIRM = (By.ID, "id_registration-password2")
    REGISTRATION_BUTTON = (By.NAME, "registration_submit")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    MESSAGE_ADD_TO_BASKET = (By.XPATH, "//div[contains( @class, 'alert-success')][1]")
    MESSAGE_PRICE_OF_BASKET = (By.XPATH, "//div[contains( @class, 'alert-info')]")
    PRODUCT_NAME_FROM_MESSAGE = (By.XPATH,
                                 "//div[contains( @class, 'alert-success')][1]/div[@class='alertinner ']/strong")
    PRODUCT_PRICE_FROM_MESSAGE = (By.XPATH,
                                  "//div[contains( @class, 'alert-info')]/div[@class='alertinner ']/p/strong")
    PRODUCT_NAME = (By.XPATH, "//div[contains(@class, 'product_main')]/h1")
    PRODUCT_PRICE = (By.XPATH, "//p[@class='price_color']")


class BasketPageLocators:
    BASKET_FORM = (By.XPATH, "//div[@class='content']")
    LIST_OF_PRODUCTS_IN_BASKET = (By.XPATH, "//div[@id='basket_formset']")
    BASKET_IS_EMPTY_MESSAGE = (By.XPATH, "//div[@id='content_inner']/p")
