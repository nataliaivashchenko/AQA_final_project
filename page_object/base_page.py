from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, chrome_driver, url):
        self.chrome_driver = chrome_driver
        self. url = url

    def open(self):
        self.chrome_driver.get(self.url)

    def find_element(self, locator, timeout=10):
        try:
            element = WebDriverWait(self.chrome_driver, timeout).until(EC.presence_of_element_located(locator))
            return element
        except TimeoutException:
            return None
