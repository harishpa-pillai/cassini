import pytest
import time
from pages.yahoo_finance_page import YahooFinancePage
from pages.yahoo_home_page import YahooHomePage
from pages.yahoo_sign_in_page import YahooSigninPage
from tests.helpers.yahoo_sign_in import YahooSignIn
from utilslib.custom_logger import CLogger
from pages.yahoo_privacy_dialoge import YahooPrivacyPolicyDialoge
from utilslib.data_source_excel import get_credential_data

c_logger = CLogger.log_gen()

pytestmark = [pytest.mark.web, pytest.mark.all]


class TestYahooWeb:
    """Test class for Yahoo we tests"""

    @pytest.mark.parametrize("credential", get_credential_data())
    def test_verify_yahoo_login(self, t_config, credential):
        """Test to verify yahoo user sign in, parameterised for three users.
            Only the first user is valid. Other two users are invalid.
        """
        username = credential[0]
        password = credential[1]

        c_logger.info(f"Starting execution of test - test_yahoo_login for user '{username}'")
        c_logger.info("Opening Yahoo home page")
        t_config.driver.get(t_config.yahoo_url)

        c_logger.info("Accepting Yahoo - Privacy policy")
        privacy_dlg = YahooPrivacyPolicyDialoge(t_config.driver)
        privacy_dlg.click(privacy_dlg.btn_ACCEPT_ALL, "Accept All button")

        c_logger.info("Verifying that Yahoo home page is loaded, checking page title")
        home_page = YahooHomePage(t_config.driver)
        assert home_page.get_title() == "Yahoo UK | News, email and search", "Yahoo home page title doesn't match"

        c_logger.info("Yahoo Home page - clicking on Sign in button")
        home_page.click(home_page.btn_SIGN_IN, "Sign in button")

        sign_in_page = YahooSigninPage(t_config.driver)

        sign_in_helper = YahooSignIn(home_page, sign_in_page)
        assert sign_in_helper.sign_in(username, password)

        c_logger.info(f"User {username}, signing out ")
        sign_in_helper.sign_out(home_page)

        c_logger.info(f"Completed test - test_yahoo_login for user '{username}'")

    def test_verify_yahoo_market_data_feb_15(self, t_config):
        """Test to verify the market data for February 15, for the signed in user"""

        username = "FirstTestLogin_12"
        password = "TestAbc_12!"

        c_logger.info(f"Starting execution of test - test_verify_yahoo_market_data")
        c_logger.info("Opening Yahoo home page")
        t_config.driver.get(t_config.yahoo_url)

        c_logger.info("Accepting Yahoo - Privacy policy")
        privacy_dlg = YahooPrivacyPolicyDialoge(t_config.driver)
        privacy_dlg.click(privacy_dlg.btn_ACCEPT_ALL, "Accept All button")

        c_logger.info("Verifying that Yahoo home page is loaded, checking page title")
        home_page = YahooHomePage(t_config.driver)
        assert home_page.get_title() == "Yahoo UK | News, email and search", "Yahoo home page title doesn't match"

        c_logger.info("Yahoo Home page - clicking on Sign in button")
        home_page.click(home_page.btn_SIGN_IN, "Sign in button")

        sign_in_page = YahooSigninPage(t_config.driver)
        sign_in_helper = YahooSignIn(home_page, sign_in_page)
        assert sign_in_helper.sign_in(username, password)

        c_logger.info("Opening Yahoo Finance page")
        home_page.click(home_page.lnk_FINANCE)

        c_logger.info("Verifying that the Yahoo Finance page is opened")
        finance_page = YahooFinancePage(t_config.driver, timeout=10)
        assert finance_page.is_element_visible(finance_page.lnk_FINANCE_HOME,
                                               "Next button"), "Yahoo Finance page is not opened"

        c_logger.info("Opening Yahoo Finance -> Market Data -> Calender")
        finance_page.open_calender()

        c_logger.info("Opening Yahoo Finance -> Market Data -> Calender -> Date picker")
        finance_page.click(finance_page.btn_DATE_PICKER, "Date picker")

        c_logger.info("Verifying that the current month is February in Date picker")
        month = finance_page.get_text(finance_page.lbl_CURRENT_MONTH, "Date picker -> Current month")

        # To ensure that the month is February, in case if the date of execution falls in March.
        if "February" not in month:
            c_logger.info("Selecting February in Date picker, using month navigation")
            finance_page.click(finance_page.btn_PREVIOUS_MONTH, "Previous month button")

        c_logger.info("Selecting the date February 15 within Date picker,")
        finance_page.click(finance_page.lnk_DATE_FEB_15, "Date - Feb 15")

        # Pausing execution to ensure page load.
        time.sleep(10)

        c_logger.info("Verifying Earnings, February 15")
        assert finance_page.get_text(finance_page.lnk_FEB_15_EARNINGS, "Earning") == "103 Earnings"

        c_logger.info("Verifying Stock Splits, February 15")
        assert finance_page.get_text(finance_page.lnk_FEB_15_STOCK_SPLITS, "Stock Splits") == "21 Stock splits"

        c_logger.info("Verifying IPO Pricing, February 15")
        assert finance_page.get_text(finance_page.lnk_FEB_15_IPO_PRICING, "IPO Pricing") == "5 IPO pricing"

        c_logger.info("Verifying Economic events, February 15")
        assert finance_page.get_text(finance_page.lnk_FEB_15_ECO_EVENTS, "Economic Events") == "22 Economic events"

        c_logger.info(f"User {username}, signing out ")
        sign_in_helper.sign_out(finance_page)

        c_logger.info(f"Completed test - test_verify_yahoo_market_data")
