import logging
import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

logger = logging.getLogger(__name__)

class AdminLoginPage(BasePage):

    URL = "/admin_test"

    EMAIL = (By.ID, "email")
    PASSWORD = (By.ID, "passwd")
    LOGIN_BUTTON = (By.ID, "submit_login")
    FORGOT_PASSWORD = (By.ID, "forgot-password-link")
    STAY_LOGGED_IN = (By.ID, "stay_logged_in")

    def enter_email(self, email):
        logger.info("Вводим email администратора")
        self.type(self.EMAIL, email)

    def enter_password(self, password):
        logger.info("Вводим пароль администратора")
        self.type(self.PASSWORD, password)

    def click_login(self):
        logger.info("Нажимаем кнопку входа в административную панель")
        self.click(self.LOGIN_BUTTON)

    @allure.step("Входим в административную панель")
    def login(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_login()

    def get_email(self):
        return self.find(self.EMAIL)

    def get_password(self):
        return self.find(self.PASSWORD)

    def get_login_button(self):
        return self.find(self.LOGIN_BUTTON)

    def get_forgot_password(self):
        return self.find(self.FORGOT_PASSWORD)

    def get_stay_logged_in(self):
        return self.browser.find_element(*self.STAY_LOGGED_IN)