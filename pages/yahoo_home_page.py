from selenium.webdriver.common.by import By

from constants import GLOBAL_TIME_OUT
from pages.base_page import BasePage


class YahooHomePage(BasePage):
    """ Contains element locators in Yahoo Home in page.
        Page: Yahoo home Page.
    """

    def __init__(self, driver, timeout=GLOBAL_TIME_OUT):
        super().__init__(driver, timeout)

        # Page locators
        self.btn_SIGN_IN = (By.CSS_SELECTOR, "#ybarAccountProfile a[href*='login.yahoo.com']")
        self.btn_AVTAR = (By.CSS_SELECTOR, "#ybarAccountMenu>label#ybarAccountMenuOpener")
        self.lbl_USER_NAME = (By.CSS_SELECTOR,
                              "div#ybarAccountMenuBody div[class='_yb_12004 _yb_2m8kz'] span:nth-child(2)")
        self.btn_SIGN_OUT = (By.ID, "profile-signout-link")
        self.lnk_FINANCE = (By.ID, "root_7")
