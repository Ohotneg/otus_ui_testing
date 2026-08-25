import logging
import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

logger = logging.getLogger(__name__)

class AddToCartModal(BasePage):

    MODAL = (By.CSS_SELECTOR, "div.modal-footer")
    CHECKOUT_BUTTON = (By.CSS_SELECTOR, "a.btn.btn-primary")

    @allure.step("Переходим к оформлению заказа")
    def proceed_to_checkout(self):
        logger.info("Переходим к оформлению заказа")

        modal = self.find(self.MODAL)

        button = modal.find_element(
            *self.CHECKOUT_BUTTON
        )

        button.click()