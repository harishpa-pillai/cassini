from selenium.webdriver.common.by import By

from constants import GLOBAL_TIME_OUT
from pages.base_page import BasePage


class YahooSigninPage(BasePage):
    """ Contains element locators in Yahoo Sign in page.
        Page: Signin Page.
    """
    def __init__(self, driver, timeout=GLOBAL_TIME_OUT):
        super().__init__(driver, timeout)

        # Page locators
        self.txt_USER_NAME = (By.ID, "login-username")
        self.txt_PASSWORD = (By.ID, "login-passwd")
        self.btn_NEXT = (By.ID, "login-signin")
        self.lbl_INVALID_PASSWORD = (By.CSS_SELECTOR, "p[class='error-msg'][data-error*='ERROR_INVALID_PASSWORD']")
        self.lbl_INVALID_USER_NAME = (By.CSS_SELECTOR, "p[id='username-error'][data-error*='INVALID_USERNAME']")
