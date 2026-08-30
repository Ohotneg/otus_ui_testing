from pages.admin_login_page import AdminLoginPage
from pages.admin_dashboard_page import AdminDashboardPage
import allure

ADMIN_EMAIL = "admin@example.com"
ADMIN_PASSWORD = "Admin1357!"

@allure.title("Авторизация и выход из административной панели")
def test_admin_login_logout(browser, base_url):

    login_page = AdminLoginPage(browser, base_url)

    login_page.open()

    login_page.login(
        ADMIN_EMAIL,
        ADMIN_PASSWORD
    )

    dashboard = AdminDashboardPage(browser, base_url)

    with allure.step("Проверяем успешную авторизацию"):
        assert dashboard.is_opened()

    dashboard.logout()

    with allure.step("Проверяем возврат на страницу авторизации"):
        assert login_page.get_email().is_displayed()