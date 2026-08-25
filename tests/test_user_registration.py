import time
from pages.registration_page import RegistrationPage
from pages.main_page import MainPage
import allure

@allure.title("Регистрация нового пользователя")
def test_user_registration(browser, base_url):

    first_name = "Petr"
    last_name = "Ivanov"
    email = f"otus_{int(time.time())}@mail.test"
    password = "Qetu1357!"

    page = RegistrationPage(browser, base_url)
    page.open()

    page.enter_first_name(first_name)
    page.enter_last_name(last_name)
    page.enter_email(email)
    page.enter_password(password)

    page.accept_customer_privacy()

    page.agree_terms()

    page.click_create_account()

    main_page = MainPage(browser, base_url)

    with allure.step("Проверяем имя зарегистрированного пользователя"):
        assert main_page.get_user_name() == f"{first_name} {last_name}"