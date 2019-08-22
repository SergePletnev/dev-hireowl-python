from framework.po.base_page import BasePage
from framework.elements.input import Input
from framework.elements.button import Button
from framework.constants.locators import LoginPageLocators as locators


class LoginPage(BasePage):
    url = 'https://dev.hireowl.com/signin'

    @property
    def email_input(self):
        return Input(locator=locators.EMAIL_INPUT)

    @property
    def password_input(self):
        return Input(locator=locators.PASSWORD_INPUT)

    @property
    def sign_in_btn(self):
        return Button(locator=locators.SIGN_IN_BUTTON)

    def __init__(self, driver):
        super().__init__(driver=driver)

    def login_user(self, email, password):
        self.email_input.input_text(email)
        self.password_input.input_text(password)
        self.sign_in_btn.click()
