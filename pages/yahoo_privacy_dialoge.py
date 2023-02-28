from selenium.webdriver.common.by import By

from constants import GLOBAL_TIME_OUT
from pages.base_page import BasePage


class YahooPrivacyPolicyDialoge(BasePage):
    def __init__(self, driver, timeout=GLOBAL_TIME_OUT):
        super().__init__(driver, timeout)
        # Page locators
        self.btn_ACCEPT_ALL = (By.CSS_SELECTOR, "button[name=agree]")
