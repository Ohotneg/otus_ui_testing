from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class AdminProductsPage(BasePage):

    CATALOG = (By.ID, "subtab-AdminCatalog")
    PRODUCTS = (By.ID, "subtab-AdminProducts")
    PAGE_TITLE = (By.CSS_SELECTOR, "h1")
    NEW_PRODUCT_BUTTON = (By.ID, "page-header-desc-configuration-add")
    CONFIRM_DELETE_BUTTON = (By.CSS_SELECTOR, "button.btn-confirm-submit")
    SUCCESS_DELETE_ALERT = (By.CSS_SELECTOR, "div.alert.alert-success.d-print-none")

    def open_products(self):
        self.click(self.CATALOG)
        self.click(self.PRODUCTS)

    def is_opened(self):
        return "Products" in self.get_title()

    def get_title(self):
        return self.find(self.PAGE_TITLE).text

    def click_add_new_product(self):
        self.click(self.NEW_PRODUCT_BUTTON)

    def open_product_menu(self, product_name):
        xpath = (
            f'//tr[.//a[normalize-space()="{product_name}"]]'
            '//a[contains(@class,"dropdown-toggle")]'
        )

        self.browser.find_element(By.XPATH, xpath).click()

    def click_delete(self):
        delete_button = self.browser.find_element(
            By.XPATH,
            '//a[contains(@class,"grid-delete-row-link")]'
        )

        delete_button.click()

    def confirm_delete(self):
        self.click(self.CONFIRM_DELETE_BUTTON)

    def get_delete_success_message(self):
        return self.find(self.SUCCESS_DELETE_ALERT).text