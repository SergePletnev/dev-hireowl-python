from framework.constants.locators import FooterLocators
from framework.constants.locators import HomePageLocators
from framework.po.base_page import BasePage
from framework.po.terms_of_use import TermsOfUsePage

from framework.elements.custom_list import CustomList
from framework.elements.link import Link
from framework.elements.section import Section


class HomePage(BasePage):
    url = 'https://dev.hireowl.com'

    @property
    def terms_of_use(self):
        return Link(locator=FooterLocators.TERMS_OF_USE_LINK)

    @property
    def popular_jobs_list(self):
        return CustomList(locator=HomePageLocators.POPULAR_JOBS_SECTIONS, decorator_class=Section)

    def __init__(self, driver):
        super().__init__(driver=driver)

    def navigate_to_terms_of_use(self):
        self.terms_of_use.click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        return TermsOfUsePage(self.driver)

    def get_popular_jobs(self):
        return self.popular_jobs_list
