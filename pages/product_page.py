from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ProductPage(BasePage):

    URL = "/3-13-the-best-is-yet-to-come-framed-poster.html"
    PRODUCT_NAME = (By.CSS_SELECTOR, "h1.product__name")
    ADD_TO_CART = (By.CSS_SELECTOR, 'button[data-button-action="add-to-cart"]')
    PRODUCT_IMAGE = (By.CSS_SELECTOR, "div.product__images img")
    PRICE = (By.CSS_SELECTOR, "div.product__price")
    SIZE_SELECT = (By.ID, "input_3_3")

    def get_product_name(self):
        return self.find(self.PRODUCT_NAME)

    def get_add_to_cart_button(self):
        return self.find(self.ADD_TO_CART)

    def get_product_image(self):
        return self.find(self.PRODUCT_IMAGE)

    def get_price(self):
        return self.find(self.PRICE)

    def get_size_select(self):
        return self.find(self.SIZE_SELECT)

    def add_to_cart(self):
        self.click(self.ADD_TO_CART)