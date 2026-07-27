from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

def test_change_currency_main(browser, base_url):
    browser.get(base_url)

    wait = WebDriverWait(browser, 10)

    product = wait.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "article.product-miniature")
        )
    )

    price_before = product.find_element(
        By.CSS_SELECTOR,".product-miniature__price").text

    currency = Select(
        browser.find_element(
            By.CSS_SELECTOR, "select.js-currency-selector")
    )

    currency.select_by_visible_text("USD $")

    wait.until(
        EC.staleness_of(product)
    )

    product = wait.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "article.product-miniature")
        )
    )

    price_after = product.find_element(
        By.CSS_SELECTOR,".product-miniature__price").text

    assert price_before != price_after