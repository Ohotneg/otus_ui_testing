from pages.registration_page import RegistrationPage

def test_registration_page(browser, base_url):

    page = RegistrationPage(browser, base_url)

    page.open()

    assert page.get_title().is_displayed()
    assert page.get_first_name().is_displayed()
    assert page.get_email().is_displayed()
    assert page.get_agree_terms() is not None
    assert page.get_create_button().is_displayed()