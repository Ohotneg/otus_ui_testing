from pages.main_page import MainPage
import allure

@allure.title("Смена валюты на главной странице")
def test_change_currency_main(browser, base_url):

    page = MainPage(browser, base_url)

    page.open()

    price_before = page.get_first_product_price()

    page.change_currency("USD $")

    price_after = page.get_first_product_price()

    with allure.step("Проверяем изменение цены после смены валюты"):
        assert price_before != price_after