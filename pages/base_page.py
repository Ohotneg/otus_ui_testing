from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    URL = ""

    def __init__(self, browser, base_url):
        self.browser = browser
        self.base_url = base_url
        self.wait = WebDriverWait(browser, 10)

    def open(self):
        self.browser.get(self.base_url + self.URL)

    def find(self, locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )

    def click(self, locator):
        element = self.wait.until(
            EC.element_to_be_clickable(locator)
        )
        element.click()

    def find_all(self, locator):
        return self.wait.until(
            EC.presence_of_all_elements_located(locator)
        )

    def hover(self, element):
        ActionChains(self.browser).move_to_element(element).perform()

    def type(self, locator, text):
        element = self.find(locator)
        element.clear()
        element.send_keys(text)

    def scroll_to(self, locator):
        element = self.find(locator)
        self.browser.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            element
        )