from pages.main_page import MainPage

def test_browser(browser, base_url):

    page = MainPage(browser, base_url)

    page.open()

    assert page.is_opened()