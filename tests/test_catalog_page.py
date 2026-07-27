from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_catalog_page(browser, base_url):
    browser.get(f"{base_url}/6-accessories")

    wait = WebDriverWait(browser, 10)

    title = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "h1.page-title-section")
        )
    )
    assert title.is_displayed()

    product_list = wait.until(
        EC.visibility_of_element_located(
            (By.ID, "js-product-list")
        )
    )
    assert product_list.is_displayed()

    product = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "article.product-miniature")
        )
    )
    assert product.is_displayed()

    price = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "div.product-miniature__price")
        )
    )
    assert price.is_displayed()

    sort = wait.until(
        EC.visibility_of_element_located(
            (By.ID, "sort_dropdown_button")
        )
    )
    assert sort.is_displayed()