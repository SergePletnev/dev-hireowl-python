from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import pytest


class Browser:
    __web_driver = None

    @staticmethod
    def get_driver():
        return Browser.__web_driver

    @staticmethod
    def set_up_driver(browser_name):
        if browser_name == "chrome":
            options = webdriver.ChromeOptions()
            Browser.__web_driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
        elif browser_name == "firefox":
            fp = webdriver.FirefoxProfile()
            Browser.__web_driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), firefox_profile=fp)
        else:
            raise pytest.UsageError("--browser_name should be chrome or firefox")

    @staticmethod
    def quit_browser():
        Browser.__web_driver.quit()
