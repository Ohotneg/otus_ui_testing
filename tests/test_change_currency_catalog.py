from pages.catalog_page import CatalogPage

def test_change_currency_catalog(browser, base_url):

    page = CatalogPage(browser, base_url)

    page.open()

    prices_before = page.get_all_prices()

    page.change_currency("USD $")

    prices_after = page.get_all_prices()

    assert prices_before != prices_after