from pages.catalog_page import CatalogPage

def test_catalog_page(browser, base_url):

    page = CatalogPage(browser, base_url)

    page.open()

    assert page.get_title().is_displayed()
    assert page.get_product_list().is_displayed()
    assert page.get_product().is_displayed()
    assert page.get_price().is_displayed()
    assert page.get_sort().is_displayed()