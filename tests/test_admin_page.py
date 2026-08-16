from pages.admin_login_page import AdminLoginPage

def test_admin_page(browser, base_url):

    page = AdminLoginPage(browser, base_url)

    page.open()

    assert page.get_email().is_displayed()
    assert page.get_password().is_displayed()
    assert page.get_login_button().is_displayed()
    assert page.get_forgot_password().is_displayed()
    assert page.get_stay_logged_in() is not None