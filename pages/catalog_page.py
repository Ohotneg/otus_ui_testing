from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC

class CatalogPage(BasePage):

    URL = "/6-accessories"

    TITLE = (By.CSS_SELECTOR, "h1.page-title-section")
    PRODUCT_LIST = (By.ID, "js-product-list")
    PRODUCT = (By.CSS_SELECTOR, "article.product-miniature")
    PRICE = (By.CSS_SELECTOR, ".product-miniature__price")
    SORT = (By.ID, "sort_dropdown_button")
    CURRENCY_SELECTOR = (By.CSS_SELECTOR, "select.js-currency-selector")

    def get_title(self):
        return self.find(self.TITLE)

    def get_product_list(self):
        return self.find(self.PRODUCT_LIST)

    def get_product(self):
        return self.find(self.PRODUCT)

    def get_price(self):
        return self.find(self.PRICE)

    def get_sort(self):
        return self.find(self.SORT)

    def get_all_prices(self):
        products = self.find_all(self.PRODUCT)

        prices = []

        for product in products:
            prices.append(
                product.find_element(*self.PRICE).text
            )

        return prices

    def change_currency(self, currency):
        products = self.find_all(self.PRODUCT)

        Select(
            self.find(self.CURRENCY_SELECTOR)
        ).select_by_visible_text(currency)

        self.wait.until(
            EC.staleness_of(products[0])
        )

        self.find_all(self.PRODUCT)