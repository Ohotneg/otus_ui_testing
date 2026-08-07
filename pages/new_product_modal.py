from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class NewProductModal(BasePage):

    MODAL_IFRAME = (By.NAME, "modal-create-product-iframe")

    CREATE_BUTTON = (By.ID, "create_product_create")

    def create_standard_product(self):

        self.wait.until(
            lambda d: d.find_element(*self.MODAL_IFRAME)
        )

        self.browser.switch_to.frame(
            self.find(self.MODAL_IFRAME)
        )

        self.click(self.CREATE_BUTTON)

        self.browser.switch_to.default_content()