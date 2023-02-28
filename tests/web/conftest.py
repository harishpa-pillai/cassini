import pytest
from selenium import webdriver

from utilslib.custom_logger import CLogger

c_logger = CLogger.log_gen()


class BaseConfig(object):
    def __init__(self):
        self.driver = None


class WebDriverGenerator:
    def __init__(self, browser):
        self._browser = browser.lower()

    def create_local_web_driver(self):
        if self._browser == "chrome":
            driver = webdriver.Chrome()
            driver.maximize_window()
        else:
            raise BrowserInstanceException(f"Browser, {self._browser} not supported")
        return driver


class BrowserInstanceException(Exception):
    pass


@pytest.fixture(scope="function")
def t_config():
    webdriver_generator = WebDriverGenerator("chrome")

    cfg = BaseConfig()
    cfg.driver = webdriver_generator.create_local_web_driver()
    cfg.yahoo_url = "https://uk.yahoo.com/?p=us"

    yield cfg

    cfg.driver.quit()
