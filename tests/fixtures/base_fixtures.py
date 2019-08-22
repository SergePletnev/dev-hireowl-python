import pytest
from framework.po.home_page import HomePage


@pytest.fixture(scope='class')
def home_page(browser):
    home_page = HomePage(browser)
    home_page.open()
    return home_page
