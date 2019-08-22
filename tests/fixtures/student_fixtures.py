import pytest

from framework.po.login_page import LoginPage


@pytest.fixture(scope='class', autouse=True)
def student_(self, browser):
    login_page = LoginPage(browser)
    login_page.open()
    login_page.login_user(self.email_student, self.password_student)
    yield
    login_page.log_out()
