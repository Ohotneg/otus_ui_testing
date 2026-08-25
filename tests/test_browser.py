from pages.main_page import MainPage
import allure

@allure.title("Проверка открытия главной страницы")
def test_browser(browser, base_url):

    page = MainPage(browser, base_url)

    page.open()

    with allure.step("Проверяем, что главная страница открыта"):
        assert page.is_opened()