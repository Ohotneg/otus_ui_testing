from pages.main_page import MainPage

def test_main_page(browser, base_url):
    page = MainPage(browser, base_url)
    page.open()

    assert page.get_logo().is_displayed()
    assert page.get_search().is_displayed()
    assert page.get_product().is_displayed()
    assert page.get_add_to_cart_button().is_displayed()
    assert page.get_contact_us_link().is_displayed()