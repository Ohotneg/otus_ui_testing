from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_admin_page(browser, base_url):
    browser.get(f"{base_url}/admin_test")

    wait = WebDriverWait(browser, 10)

    email = wait.until(
        EC.visibility_of_element_located(
            (By.ID, "email")
        )
    )
    assert email.is_displayed()

    password = wait.until(
        EC.visibility_of_element_located(
            (By.ID, "passwd")
        )
    )
    assert password.is_displayed()

    login_button = wait.until(
        EC.visibility_of_element_located(
            (By.ID, "submit_login")
        )
    )
    assert login_button.is_displayed()

    forgot_password = wait.until(
        EC.visibility_of_element_located(
            (By.ID, "forgot-password-link")
        )
    )
    assert forgot_password.is_displayed()

    stay_logged_in = wait.until(
        EC.presence_of_element_located(
            (By.ID, "stay_logged_in")
        )
    )
    assert stay_logged_in is not None