from pages.main_page import MainPage
import allure

@allure.title("Проверка элементов главной страницы")
def test_main_page(browser, base_url):
    page = MainPage(browser, base_url)
    page.open()

    with allure.step("Проверяем наличие основных элементов главной страницы"):
        assert page.get_logo().is_displayed()
        assert page.get_search().is_displayed()
        assert page.get_product().is_displayed()
        assert page.get_add_to_cart_button().is_displayed()
        assert page.get_contact_us_link().is_displayed()