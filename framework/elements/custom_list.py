from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from framework.browser.browser import Browser


class CustomList(list):

    def __init__(self, locator, decorator_class, timeout=5):
        self.driver = Browser.get_driver()
        self.locator = locator
        self.wait = WebDriverWait(self.driver, timeout)
        # self.web_elements = self._find_all()
        self.elements = self._decorate_web_elements(decorator_class)
        super().__init__(self.elements)

    def _find_all(self):
        elements = self.wait.until(
            EC.visibility_of_all_elements_located(locator=self.locator)
        )
        return elements

    def _decorate_web_elements(self, decorator_class):
        web_elements = self._find_all()
        elements = [decorator_class(web_element=element) for element in web_elements]
        return elements
