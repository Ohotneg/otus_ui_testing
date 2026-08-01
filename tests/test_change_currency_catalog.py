from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

def test_change_currency_catalog(browser, base_url):
    browser.get(f"{base_url}/6-accessories")

    wait = WebDriverWait(browser, 10)

    products = wait.until(
        EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, "article.product-miniature")
        )
    )

    prices_before = []

    for product in products:
        price = product.find_element(
            By.CSS_SELECTOR,".product-miniature__price").text

        prices_before.append(price)

    currency = Select(
        browser.find_element(
            By.CSS_SELECTOR, "select.js-currency-selector")
    )

    currency.select_by_visible_text("USD $")

    wait.until(
        EC.staleness_of(products[0])
    )

    products = wait.until(
        EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, "article.product-miniature")
        )
    )

    prices_after = []

    for product in products:
        price = product.find_element(
            By.CSS_SELECTOR,".product-miniature__price").text

        prices_after.append(price)

    assert prices_before != prices_after