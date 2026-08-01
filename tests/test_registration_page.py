from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_registartion_page(browser, base_url):
    browser.get(f"{base_url}/registration")

    wait = WebDriverWait(browser, 10)

    title = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "h1.page-title-section")
        )
    )
    assert title.is_displayed()

    firstname = wait.until(
        EC.visibility_of_element_located(
            (By.ID, "field-firstname")
        )
    )
    assert firstname.is_displayed()

    email = wait.until(
        EC.visibility_of_element_located(
            (By.ID, "field-email")
        )
    )
    assert email.is_displayed()

    agree_terms = wait.until(
        EC.presence_of_element_located(
            (By.ID, "field-psgdpr")
        )
    )
    assert agree_terms is not None

    create_button = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, 'button[data-link-action="save-customer"]')
        )
    )
    assert create_button.is_displayed()