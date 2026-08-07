from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC

class MainPage(BasePage):

    LOGO = (By.CSS_SELECTOR, "img.logo")
    SEARCH = (By.NAME, "s")
    PRODUCT = (By.CSS_SELECTOR, "article.product-miniature")
    ADD_TO_CART = (By.CSS_SELECTOR, 'button[data-button-action="add-to-cart"]')
    CONTACT_US = (By.CSS_SELECTOR, 'a[href$="contact-us"]')
    PRODUCTS = (By.CSS_SELECTOR, "article.product-miniature")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, 'button[data-button-action="add-to-cart"]')
    PRODUCT_TITLE = (By.CSS_SELECTOR, "a.product-miniature__title")
    USER_NAME = (By.ID, "userMenuButton")
    FIRST_PRODUCT = (By.CSS_SELECTOR, "article.product-miniature")
    FIRST_PRODUCT_PRICE = (By.CSS_SELECTOR, ".product-miniature__price")
    CURRENCY_SELECTOR = (By.CSS_SELECTOR, "select.js-currency-selector")

    def get_logo(self):
        return self.find(self.LOGO)

    def get_search(self):
        return self.find(self.SEARCH)

    def get_product(self):
        return self.find(self.PRODUCT)

    def get_add_to_cart_button(self):
        return self.find(self.ADD_TO_CART)

    def get_contact_us_link(self):
        return self.find(self.CONTACT_US)

    def get_available_products(self):
        products = self.find_all(self.PRODUCTS)

        available_products = []

        for product in products:
            buttons = product.find_elements(*self.ADD_TO_CART_BUTTON)

            if buttons:
                available_products.append(product)

        return available_products

    def get_product_name(self, product):
        return product.find_element(
            *self.PRODUCT_TITLE
        ).text

    def add_product_to_cart(self, product):
        self.hover(product)

        button = product.find_element(
            *self.ADD_TO_CART_BUTTON
        )
        button.click()

    def get_user_name(self):
        text = self.find(self.USER_NAME).text
        return text.splitlines()[-1].strip()

    def get_first_product_price(self):

        product = self.find(self.FIRST_PRODUCT)

        return product.find_element(
            *self.FIRST_PRODUCT_PRICE
        ).text

    def change_currency(self, currency):

        product = self.find(self.FIRST_PRODUCT)

        Select(
            self.find(self.CURRENCY_SELECTOR)
        ).select_by_visible_text(currency)

        self.wait.until(
            EC.staleness_of(product)
        )

        self.find(self.FIRST_PRODUCT)

    def is_opened(self):
        return self.find(self.FIRST_PRODUCT).is_displayed()