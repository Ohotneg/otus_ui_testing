from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class AddToCartModal(BasePage):

    MODAL = (By.CSS_SELECTOR, "div.modal-footer")
    CHECKOUT_BUTTON = (By.CSS_SELECTOR, "a.btn.btn-primary")

    def proceed_to_checkout(self):
        modal = self.find(self.MODAL)

        button = modal.find_element(
            *self.CHECKOUT_BUTTON
        )

        button.click()