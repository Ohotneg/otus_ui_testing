from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

ADMIN_EMAIL = "admin@example.com"
ADMIN_PASSWORD = "Admin1234!"


def test_admin_login_logout(browser, base_url):
    browser.get(f"{base_url}/admin_test")

    wait = WebDriverWait(browser, 10)

    email = wait.until(
        EC.visibility_of_element_located(
            (By.ID, "email")
        )
    )
    email.send_keys(ADMIN_EMAIL)

    password = wait.until(
        EC.visibility_of_element_located(
            (By.ID, "passwd")
        )
    )
    password.send_keys(ADMIN_PASSWORD)

    login_button = wait.until(
        EC.element_to_be_clickable(
            (By.ID, "submit_login")
        )
    )
    login_button.click()

    dashboard = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "h1.page-title")
        )
    )

    assert dashboard.text == "Dashboard"

    profile = wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "#employee_infos a.employee_name")
        )
    )

    profile.click()

    logout_button = wait.until(
        EC.element_to_be_clickable(
            (By.ID, "header_logout")
        )
    )
    logout_button.click()

    email = wait.until(
        EC.visibility_of_element_located(
            (By.ID, "email")
        )
    )

    assert email.is_displayed()