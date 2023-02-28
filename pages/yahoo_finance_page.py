from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from constants import GLOBAL_TIME_OUT
from pages.base_page import BasePage


class YahooFinancePage(BasePage):
    """ Contains element locators in Yahoo Home in page.
        Page: Yahoo Finance Page.
    """

    def __init__(self, driver, timeout=GLOBAL_TIME_OUT):
        super().__init__(driver, timeout)

        # Page locators
        self.lnk_FINANCE_HOME = (By.CSS_SELECTOR, "a[title='Finance Home']")
        self.lnk_MARKET_DATA = (By.CSS_SELECTOR, "div[title='Market Data']")
        self.lnk_CALENDER = (By.CSS_SELECTOR, "a[title='Calendar']")
        self.btn_AVTAR = (By.CSS_SELECTOR, "#uh-profile>svg")
        self.btn_SIGN_OUT = (By.CSS_SELECTOR, "#uh-signedout>span")

        self.btn_DATE_PICKER = (By.CSS_SELECTOR, "div[class*='datePickerBtn'] svg[class*='datePickerBtn:']")
        self.lbl_CURRENT_MONTH = (By.CSS_SELECTOR, "span[class*='current-month'] span")
        self.btn_PREVIOUS_MONTH = (By.CSS_SELECTOR, "a[class*='previous Start'] svg")
        self.lnk_DATE_FEB_15 = (By.XPATH, "//tbody[contains(@class, 'month')]/tr/td/div/span[text()='15']")

        self.lnk_FEB_15_EARNINGS = (By.CSS_SELECTOR, "a[title='Prev']~ul li:nth-child(4) a:nth-child(2)")
        self.lnk_FEB_15_STOCK_SPLITS = (By.CSS_SELECTOR, "a[title='Prev']~ul li:nth-child(4) a:nth-child(3)")
        self.lnk_FEB_15_IPO_PRICING = (By.CSS_SELECTOR, "a[title='Prev']~ul li:nth-child(4) a:nth-child(4)")
        self.lnk_FEB_15_ECO_EVENTS = (By.CSS_SELECTOR, "a[title='Prev']~ul li:nth-child(4) a:nth-child(5)")

    def open_calender(self):
        """
        Method for opening the Finance ->Market data - Calender page
        Args:
        Returns:
            True - if successful
        Raises:
            None
        """
        actions = ActionChains(self.driver)
        market_link = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.lnk_MARKET_DATA))
        actions.move_to_element(market_link).perform()
        calender_menu_item = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.lnk_CALENDER))
        actions.click(calender_menu_item).perform()
        return True
