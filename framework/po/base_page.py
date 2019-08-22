import time

from framework.constants.locators import HeaderLocators as locators
from framework.elements.link import Link
from framework.elements.button import Button


class BasePage(object):
    url = None

    @property
    def account_link(self):
        return Link(locator=locators.ACCOUNT_LINK)

    @property
    def sign_out_link(self):
        return Link(locator=locators.SIGN_OUT_LINK)

    @property
    def join_button(self):
        return Button(locator=locators.JOIN_BUTTON)

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.url)

    def get_page_title(self):
        return self.driver.title

    def is_user_logged_in(self):
        return self.account_link.is_displayed()

    def log_out(self):
        self.account_link.click()
        self.sign_out_link.click()



    def join(self):
        self.join_button.click()
        time.sleep(3)