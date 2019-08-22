from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from framework.browser.browser import Browser


class BaseElement(object):

    def __init__(self, timeout=5, **kwargs):
        self.driver = Browser.get_driver()
        self.wait = WebDriverWait(self.driver, timeout)
        if 'locator' in kwargs:
            self.locator = kwargs.get('locator')
            self.web_element = self._find()
        if 'web_element' in kwargs:
            self.web_element = kwargs.get('web_element')

    def _find(self):
        element = self.wait.until(
            EC.visibility_of_element_located(locator=self.locator)
        )
        return element

    def click(self):
        element = self.wait.until(
            EC.element_to_be_clickable(locator=self.locator)
        )
        element.click()

    def is_displayed(self):
        return self.web_element.is_displayed()

    def attribute(self, attr_name):
        attribute = self.web_element.get_attribute(attr_name)
        return attribute

    @property
    def text(self):
        text = self.web_element.text
        return text
