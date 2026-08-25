from pages.admin_login_page import AdminLoginPage
from pages.admin_dashboard_page import AdminDashboardPage
from pages.admin_products_page import AdminProductsPage
from pages.new_product_modal import NewProductModal
from pages.admin_product_form_page import AdminProductFormPage
import time
import allure

ADMIN_EMAIL = "admin@example.com"
ADMIN_PASSWORD = "Admin1357!"

@allure.title("Создание нового товара в админ-панели")
def test_admin_create_product(browser, base_url):

    login_page = AdminLoginPage(browser, base_url)

    login_page.open()

    login_page.login(
        ADMIN_EMAIL,
        ADMIN_PASSWORD
    )

    dashboard_page = AdminDashboardPage(browser, base_url)

    with allure.step("Проверяем, что открыта административная панель"):
        assert dashboard_page.is_opened()

    products_page = AdminProductsPage(browser, base_url)

    products_page.open_products()

    with allure.step("Проверяем, что открыт раздел товаров"):
        assert products_page.is_opened()

    products_page.click_add_new_product()

    modal = NewProductModal(browser, base_url)

    modal.create_standard_product()

    product_form = AdminProductFormPage(browser, base_url)

    with allure.step("Проверяем, что открыта форма товара"):
        assert product_form.is_opened()

    product_name = f"Otus test product {int(time.time())}"

    product_form.enter_product_name(product_name)

    with allure.step("Проверяем название товара"):
        assert product_form.get_product_name() == product_name

    product_form.save()

    with allure.step("Проверяем успешное сохранение товара"):
        assert "Successful update" in product_form.get_success_message()