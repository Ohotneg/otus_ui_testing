from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

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

    def enter_first_name(self, first_name):
        self.type(self.FIRST_NAME, first_name)

    def enter_email(self, email):
        self.type(self.EMAIL, email)

    def agree_terms(self):
        element = self.find(self.AGREE_TERMS)

        self.browser.execute_script(
            "arguments[0].click();",
            element
        )

    def click_create_account(self):
        self.scroll_to(self.CREATE_BUTTON)

        button = self.find(self.CREATE_BUTTON)

        self.browser.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            button
        )

        self.wait.until(
            EC.element_to_be_clickable(self.CREATE_BUTTON)
        )

        self.click(self.CREATE_BUTTON)

    def enter_last_name(self, last_name):
        self.type(self.LAST_NAME, last_name)

    def enter_password(self, password):
        self.type(self.PASSWORD, password)

    def accept_customer_privacy(self):
        element = self.find(self.CUSTOMER_PRIVACY)

        self.browser.execute_script(
            "arguments[0].click();",
            element
        )