import os
import pytest
from selenium import webdriver
import logging
import allure
from selenium.webdriver.chrome.options import Options

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome"
    )

    parser.addoption(
        "--base-url",
        action="store",
        default="http://prestashop"
    )

@pytest.fixture
def browser(request):
    browser_name = request.config.getoption("--browser")

    if browser_name == "chrome":
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--force-device-scale-factor=1")

        selenoid_url = os.getenv("SELENOID_URL")
        browser_version = os.getenv("BROWSER_VERSION")

        options.set_capability("browserVersion", browser_version)

        if selenoid_url:
            driver = webdriver.Remote(
                command_executor=selenoid_url,
                options=options
            )
        else:
            driver = webdriver.Chrome(options=options)

    elif browser_name == "firefox":
        options = webdriver.FirefoxOptions()
        options.add_argument("--headless")
        options.add_argument("--width=1920")
        options.add_argument("--height=1080")

        selenoid_url = os.getenv("SELENOID_URL")
        browser_version = os.getenv("BROWSER_VERSION")

        options.set_capability("browserVersion", browser_version)

        if selenoid_url:
            driver = webdriver.Remote(
                command_executor=selenoid_url,
                options=options
            )
        else:
            driver = webdriver.Firefox(options=options)

    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    yield driver
    driver.quit()

@pytest.fixture
def base_url(request):
    return request.config.getoption("--base-url")

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        browser = item.funcargs.get("browser")

        if browser:
            try:
                allure.attach(
                    browser.get_screenshot_as_png(),
                    name="screenshot",
                    attachment_type=allure.attachment_type.PNG
                )
            except Exception as e:
                print(f"Не удалось сделать screenshot: {e}")