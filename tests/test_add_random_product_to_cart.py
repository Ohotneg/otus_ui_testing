import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

def test_add_random_product_to_cart(browser, base_url):
    browser.get(base_url)

    wait = WebDriverWait(browser, 10)

    products = wait.until(
        EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, "article.product-miniature")
        )
    )
    available_products = []

    for product in products:
        buttons = product.find_elements(
            By.CSS_SELECTOR,'button[data-button-action="add-to-cart"]'
        )
        if buttons:
            available_products.append(product)

    product = random.choice(available_products)

    product_name = product.find_element(
        By.CSS_SELECTOR,"a.product-miniature__title").text

    add_button = product.find_element(
        By.CSS_SELECTOR,'button[data-button-action="add-to-cart"]')

    ActionChains(browser).move_to_element(product).perform()

    add_button.click()

    modal = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "div.modal-footer")
        )
    )

    checkout_button = modal.find_element(
        By.CSS_SELECTOR,"a.btn.btn-primary")

    checkout_button.click()

    cart_product = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR,"a.product-line__title:not(.product-line__item)")
        )
    )

    cart_product_name = cart_product.text

    assert product_name == cart_product_name