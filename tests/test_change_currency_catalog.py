from pages.catalog_page import CatalogPage
import allure

@allure.title("Смена валюты в каталоге")
def test_change_currency_catalog(browser, base_url):

    page = CatalogPage(browser, base_url)

    page.open()

    prices_before = page.get_all_prices()

    page.change_currency("USD $")

    prices_after = page.get_all_prices()

    with allure.step("Проверяем изменение цен после смены валюты"):
        assert prices_before != prices_after