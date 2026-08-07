from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class AdminDashboardPage(BasePage):

    DASHBOARD_TITLE = (By.CSS_SELECTOR, "h1.page-title")
    PROFILE = (By.CSS_SELECTOR, "#employee_infos a.employee_name")
    LOGOUT = (By.ID, "header_logout")

    def get_title(self):
        return self.find(self.DASHBOARD_TITLE)

    def is_opened(self):
        return self.get_title().text == "Dashboard"

    def open_profile_menu(self):
        self.click(self.PROFILE)

    def click_logout(self):
        self.click(self.LOGOUT)

    def logout(self):
        self.open_profile_menu()
        self.click_logout()