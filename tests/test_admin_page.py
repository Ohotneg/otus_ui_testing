from pages.admin_login_page import AdminLoginPage
import allure

@allure.title("Проверка элементов страницы авторизации")
def test_admin_page(browser, base_url):

    page = AdminLoginPage(browser, base_url)

    page.open()
    with allure.step("Проверяем наличие элементов страницы авторизации"):
        assert page.get_email().is_displayed()
        assert page.get_password().is_displayed()
        assert page.get_login_button().is_displayed()
        assert page.get_forgot_password().is_displayed()
        assert page.get_stay_logged_in() is not None