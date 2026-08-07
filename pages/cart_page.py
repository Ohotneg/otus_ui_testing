from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CartPage(BasePage):

    PRODUCT_NAME = (By.CSS_SELECTOR, "a.product-line__title:not(.product-line__item)")

    def get_product_name(self):
        return self.find(self.PRODUCT_NAME).text