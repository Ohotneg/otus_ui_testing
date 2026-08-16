from pages.product_page import ProductPage

def test_product_page(browser, base_url):

    page = ProductPage(browser, base_url)

    page.open()

    assert page.get_product_name().is_displayed()
    assert page.get_add_to_cart_button().is_displayed()
    assert page.get_product_image().is_displayed()
    assert page.get_price().is_displayed()
    assert page.get_size_select().is_displayed()