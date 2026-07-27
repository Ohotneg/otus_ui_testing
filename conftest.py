import pytest

from selenium import webdriver


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