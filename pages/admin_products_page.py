import logging
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure

logger = logging.getLogger(__name__)

class AdminProductsPage(BasePage):

    CATALOG = (By.ID, "subtab-AdminCatalog")
    PRODUCTS = (By.ID, "subtab-AdminProducts")
    PAGE_TITLE = (By.CSS_SELECTOR, "h1")
    NEW_PRODUCT_BUTTON = (By.ID, "page-header-desc-configuration-add")
    CONFIRM_DELETE_BUTTON = (By.CSS_SELECTOR, "button.btn-confirm-submit")
    SUCCESS_DELETE_ALERT = (By.CSS_SELECTOR, "div.alert.alert-success.d-print-none")

    @allure.step("Открываем раздел товаров")
    def open_products(self):
        logger.info("Открываем раздел товаров")
        self.click(self.CATALOG)
        self.click(self.PRODUCTS)

    def is_opened(self):
        return "Products" in self.get_title()

    def get_title(self):
        return self.find(self.PAGE_TITLE).text

    @allure.step("Нажимаем кнопку добавления нового товара")
    def click_add_new_product(self):
        logger.info("Нажимаем кнопку добавления нового товара")
        self.click(self.NEW_PRODUCT_BUTTON)

    @allure.step("Открываем меню товара «{product_name}»")
    def open_product_menu(self, product_name):
        logger.info("Открываем меню товара: %s", product_name)

        xpath = (
            f'//tr[.//a[normalize-space()="{product_name}"]]'
            '//a[contains(@class,"dropdown-toggle")]'
        )

        self.browser.find_element(By.XPATH, xpath).click()

    @allure.step("Удаляем товар")
    def click_delete(self):
        logger.info("Нажимаем кнопку удаления товара")

        delete_button = self.browser.find_element(
            By.XPATH,
            '//a[contains(@class,"grid-delete-row-link")]'
        )

        delete_button.click()

    @allure.step("Подтверждаем удаление товара")
    def confirm_delete(self):
        logger.info("Подтверждаем удаление товара")
        self.click(self.CONFIRM_DELETE_BUTTON)

    def get_delete_success_message(self):
        return self.find(self.SUCCESS_DELETE_ALERT).text