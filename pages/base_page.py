from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException, \
    StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from utilslib.custom_logger import CLogger

c_logger = CLogger.log_gen()


class BasePage:
    """ Base page which is the parent of all pages. Contains all generic methods for all pages"""

    def __init__(self, driver, time_out):
        self.driver = driver
        self.time_out = time_out

    def click(self, locator, field_name="Not Defined", time_out=None):
        """ Performs click operation on a given element
        Args :
            locator : element locator
            field_name : name of the web element
            time_out : value in seconds overriding the default TIMEOUT
        Returns:
            True - if successful
        Raises:
            BasePageException: If the click fails.
        """
        if time_out is None:
            time_out = self.time_out

        try:
            c_logger.info(f"\t\tclicking '{field_name}'")
            WebDriverWait(self.driver, time_out).until(EC.element_to_be_clickable(locator)).click()
            return True
        except TimeoutException:
            raise BasePageException("BasePage : click - TimeoutException: Unable to click on the element.")
        except ElementClickInterceptedException:
            raise BasePageException("BasePage : click - ElementClickInterceptedException: Click is intercepted.")
        except StaleElementReferenceException:
            WebDriverWait(self.driver, time_out).until(EC.visibility_of_element_located(locator)).click()

    def get_title(self):
        """ Returns the title of a page
        Args :
            No args
        Returns:
            Title of the page if success, None otherwise
        Raises:
            None
        """
        try:
            return self.driver.title
        except TimeoutException:
            c_logger.warning("TimeoutException while fetching the title, returning None.")
            return None

    def is_element_visible(self, locator, field_name="Not Defined", time_out=None):
        """ Returns whether the element is in visible state
        Args :
            locator : element locator
            time_out : value in seconds overriding the default TIMEOUT of 60 seconds
            field_name : name of the web element
        Returns:
            True or False based on element's visible state
        Raises:
            None
        """
        if time_out is None:
            time_out = self.time_out

        try:
            c_logger.info(f"\t\tretrieving visibility state of element '{field_name}'")
            return WebDriverWait(self.driver, time_out).until(EC.visibility_of_element_located(locator)).is_displayed()
        except TimeoutException:
            c_logger.info(f"\t\tthe element is not visible, returning False.")
            return False

    def get_text(self, locator, field_name="Not Defined", time_out=None):
        """ Returns the text associated with an element
        Args :
            locator : element locator
            time_out : value in seconds overriding the default TIMEOUT
            field_name : name of the web element
        Returns:
            Element's text/None
        Raises:
            None
        """
        if time_out is None:
            time_out = self.time_out

        try:
            c_logger.info(f"\t\tretrieving text from field '{field_name}'")
            return WebDriverWait(self.driver, time_out).until(EC.visibility_of_element_located(locator)).text
        except TimeoutException:
            c_logger.warning("TimeoutException while fetching the element's text, returning None")
            return None

    def clear(self, locator, field_name="Not Defined", time_out=None):
        """ Clear the current value in a text field
        Args :
            locator : element locator
            field_name : name of the web element
            time_out : value in seconds overriding the default TIMEOUT
        Returns:
            True - if successful
        Raises:
            BasePageException: If the clear operation fails.
        """
        if time_out is None:
            time_out = self.time_out

        try:
            c_logger.info(f"\t\tclearing field '{field_name}'")
            WebDriverWait(self.driver, time_out).until(EC.element_to_be_clickable(locator)).clear()
            return True
        except TimeoutException:
            raise BasePageException("BasePage : clear - TimeoutException while clearing the text field")

    def fill_in_field(self, locator, text, field_name="Not Defined", sensitive_data=False, time_out=None):
        """ Fill in the given text - Used for element types - text box
        Args :
            locator : element locator
            text : text to be filled in
            field_name : name of the web element
            sensitive_data : boolean value indicating whether the input text should be displayed in logs or not
            time_out : value in seconds overriding the default TIMEOUT
        Returns:
            True - if successful
        Raises:
            BasePageException: If the fill in text field operation fails.
        """
        if time_out is None:
            time_out = self.time_out

        try:
            if not sensitive_data:
                c_logger.info(f"\t\tfilling in field '{field_name}' with value '{text}'")
            else:
                c_logger.info(f"\t\tfilling in field '{field_name}' with value '*****'")
            WebDriverWait(self.driver, time_out).until(EC.element_to_be_clickable(locator)).send_keys(text)
            return True
        except TimeoutException:
            raise BasePageException("BasePage : fill_in_field - TimeoutException while filling in text.")

    def clear_and_fill_in_field(self, locator, text, field_name="Not Defined", sensitive_data=False, time_out=None):
        """ Clear the current value and fill in the given text - Used for element types - text box
        Args :
            locator : element locator
            text : text to be filled in
            field_name : name of the web element
            sensitive_data : boolean value indicating whether the input text should be displayed in logs or not
            time_out : value in seconds overriding the default TIMEOUT
        Returns:
            True - if successful
        Raises:
            None.
        """
        if time_out is None:
            time_out = self.time_out

        self.clear(locator, field_name, time_out)
        self.fill_in_field(locator, text, field_name, sensitive_data, time_out)
        return True


class BasePageException(Exception):
    """Exception class for BasePage """
    pass
