import random
from pages.main_page import MainPage
from pages.add_to_cart_modal import AddToCartModal
from pages.cart_page import CartPage

def test_add_random_product_to_cart(browser, base_url):

    page = MainPage(browser, base_url)

    page.open()

    products = page.get_available_products()

    product = random.choice(products)

    product_name = page.get_product_name(product)

    page.add_product_to_cart(product)

    modal = AddToCartModal(browser, base_url)

    modal.proceed_to_checkout()

    cart = CartPage(browser, base_url)

    cart_product_name = cart.get_product_name()

    assert product_name == cart_product_name