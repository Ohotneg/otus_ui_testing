import logging
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

logger = logging.getLogger(__name__)

class RegistrationPage(BasePage):

    URL = "/registration"
    TITLE = (By.CSS_SELECTOR, "h1.page-title-section")
    FIRST_NAME = (By.ID, "field-firstname")
    EMAIL = (By.ID, "field-email")
    AGREE_TERMS = (By.ID, "field-psgdpr")
    CUSTOMER_PRIVACY = (By.ID, "field-customer_privacy")
    CREATE_BUTTON = (By.CSS_SELECTOR, 'button[data-link-action="save-customer"]')
    LAST_NAME = (By.ID, "field-lastname")
    PASSWORD = (By.ID, "field-password")

    def get_title(self):
        return self.find(self.TITLE)

    def get_first_name(self):
        return self.find(self.FIRST_NAME)

    def get_email(self):
        return self.find(self.EMAIL)

    def get_agree_terms(self):
        return self.wait.until(EC.presence_of_element_located(self.AGREE_TERMS))

    def get_create_button(self):
        return self.find(self.CREATE_BUTTON)

    @allure.step("Вводим имя пользователя")
    def enter_first_name(self, first_name):
        logger.info("Вводим имя пользователя")
        self.type(self.FIRST_NAME, first_name)

    @allure.step("Вводим email")
    def enter_email(self, email):
        logger.info("Вводим email пользователя")
        self.type(self.EMAIL, email)

    @allure.step("Принимаем условия использования")
    def agree_terms(self):
        logger.info("Принимаем условия использования")
        element = self.find(self.AGREE_TERMS)

        self.browser.execute_script(
            "arguments[0].click();",
            element
        )

    @allure.step("Создаём аккаунт")
    def click_create_account(self):
        logger.info("Нажимаем кнопку «Создать аккаунт»")

        self.scroll_to(self.CREATE_BUTTON)
        self.click(self.CREATE_BUTTON)

    @allure.step("Вводим фамилию пользователя")
    def enter_last_name(self, last_name):
        logger.info("Вводим фамилию пользователя")
        self.type(self.LAST_NAME, last_name)

    @allure.step("Вводим пароль пользователя")
    def enter_password(self, password):
        logger.info("Вводим пароль пользователя")
        self.type(self.PASSWORD, password)

    @allure.step("Принимаем политику конфиденциальности")
    def accept_customer_privacy(self):
        logger.info("Принимаем политику конфиденциальности")
        element = self.find(self.CUSTOMER_PRIVACY)

        self.browser.execute_script(
            "arguments[0].click();",
            element
        )