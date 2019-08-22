import pytest

from framework.browser.browser import Browser

from framework.po.home_page import HomePage


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='en',
                     help="Choose locale: en, ru")


pytest_plugins = ['tests.fixtures.base_fixtures']


@pytest.fixture(scope='class')
def browser(request):
    browser_name = request.config.getoption('browser_name')

    Browser.set_up_driver(browser_name)
    browser = Browser.get_driver()

    yield browser
    Browser.quit_browser()


@pytest.fixture(scope='class')
def test_main_fixture(browser):
    home_page = HomePage(browser)
    home_page.open()
