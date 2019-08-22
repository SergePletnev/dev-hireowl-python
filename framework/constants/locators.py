from selenium.webdriver.common.by import By


class HeaderLocators(object):
    ACCOUNT_LINK = (By.CSS_SELECTOR, '#navigation-toggle')
    SIGN_OUT_LINK = (By.LINK_TEXT, 'Sign Out')
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'a[href="/signin"]')
    JOIN_BUTTON = (By.CSS_SELECTOR, 'a[href="/signup"]')
    POPULAR_JOBS_LINK = (By.CSS_SELECTOR, 'a[href="/#popular-jobs"]')


class FooterLocators(object):
    TERMS_OF_USE_LINK = (By.CSS_SELECTOR, 'a[href="/terms_of_use"]')


class HomePageLocators(object):
    POPULAR_JOBS_SECTIONS = (By.CSS_SELECTOR, '#popular-jobs section')


class LoginPageLocators(object):
    EMAIL_INPUT = (By.CSS_SELECTOR, '#user_email')
    PASSWORD_INPUT = (By.CSS_SELECTOR, '#user_password')
    SIGN_IN_BUTTON = (By.CSS_SELECTOR, 'input[value="Sign in"]')


class TermsOfUsePage(object):
    pass
