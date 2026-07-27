def test_browser(browser, base_url):
    browser.get(base_url)

    assert browser.title