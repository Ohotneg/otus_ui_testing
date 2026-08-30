from pages.admin_login_page import AdminLoginPage
from pages.admin_dashboard_page import AdminDashboardPage
from pages.admin_products_page import AdminProductsPage
import allure

ADMIN_EMAIL = "admin@example.com"
ADMIN_PASSWORD = "Admin1357!"

@allure.title("Проверка страницы товаров в админ-панели")
def test_admin_products_page(browser, base_url):

    login = AdminLoginPage(browser, base_url)

    login.open()

    login.login(
        ADMIN_EMAIL,
        ADMIN_PASSWORD
    )

    dashboard = AdminDashboardPage(browser, base_url)

    with allure.step("Проверяем, что открыта административная панель"):
        assert dashboard.is_opened()

    products = AdminProductsPage(browser, base_url)

    products.open_products()

    with allure.step("Проверяем, что открыт раздел товаров"):
        assert products.is_opened()