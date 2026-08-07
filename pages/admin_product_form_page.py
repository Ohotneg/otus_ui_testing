from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class AdminProductFormPage(BasePage):

    PRODUCT_NAME = (By.ID, "product_header_name_1")
    SAVE_BUTTON = (By.ID, "product_footer_save")
    SUCCESS_ALERT = (By.CSS_SELECTOR, "div.alert.alert-success.d-print-none")

    def is_opened(self):
        element = self.find(self.PRODUCT_NAME)
        return element.is_displayed()

    def enter_product_name(self, name):
        self.type(self.PRODUCT_NAME, name)

    def get_product_name(self):
        return self.find(self.PRODUCT_NAME).get_attribute("value")

    def save(self):
        self.click(self.SAVE_BUTTON)

    def get_success_message(self):
        return self.find(self.SUCCESS_ALERT).text