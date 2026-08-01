from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_main_page(browser, base_url):
    browser.get(base_url)

    wait = WebDriverWait(browser, 10)

    logo = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "img.logo")
        )
    )
    assert logo.is_displayed()

    search = wait.until(
        EC.visibility_of_element_located(
            (By.NAME, "s")
        )
    )
    assert search.is_displayed()

    product = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "article.product-miniature")
        )
    )
    assert product.is_displayed()

    add_to_cart = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, 'button[data-button-action="add-to-cart"]')
        )
    )
    assert add_to_cart.is_displayed()

    contact_us = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, 'a[href$="contact-us"]')
        )
    )
    assert contact_us.is_displayed()