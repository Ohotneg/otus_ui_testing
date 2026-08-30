import pytest
from selenium import webdriver
import logging
import allure

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
        default="http://localhost:8080"
    )


@pytest.fixture
def browser(request):
    browser_name = request.config.getoption("--browser")

    if browser_name == "chrome":
        driver = webdriver.Chrome()

    elif browser_name == "firefox":
        driver = webdriver.Firefox()

    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    driver.maximize_window()

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
            allure.attach(
                browser.get_screenshot_as_png(),
                name="screenshot",
                attachment_type=allure.attachment_type.PNG
            )