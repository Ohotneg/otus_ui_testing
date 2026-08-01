from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_product_page(browser, base_url):
    browser.get(f"{base_url}/3-13-the-best-is-yet-to-come-framed-poster.html")

    wait = WebDriverWait(browser, 10)

    product_name = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "h1.product__name")
        )
    )
    assert product_name.is_displayed()

    add_to_cart = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, 'button[data-button-action="add-to-cart"]')
        )
    )
    assert add_to_cart.is_displayed()

    product_image = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "div.product__images img")
        )
    )
    assert product_image.is_displayed()

    price = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "div.product__price")
        )
    )
    assert price.is_displayed()

    form_select = wait.until(
        EC.visibility_of_element_located(
            (By.ID, "input_3_3")
        )
    )
    assert form_select.is_displayed()