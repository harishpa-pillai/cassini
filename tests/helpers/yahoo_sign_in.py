from utilslib.custom_logger import CLogger

c_logger = CLogger.log_gen()


class YahooSignIn:
    """ Helper class for Yahoo sign in/sign out and verifications"""

    def __init__(self, home_page, sign_in_page):
        self.home_page = home_page
        self.sign_in_page = sign_in_page

    def sign_in(self, username, password):
        """Method for Yahoo sign in
        Args :
            username : Name of user to sign in
            password : User password
        Returns:
            True - if successful
        Raises:
            None
        """
        c_logger.info("Verifying that the Yahoo sign in page is opened")
        assert self.sign_in_page.is_element_visible(self.sign_in_page.btn_NEXT, "Next button")
        c_logger.info("Filling in Sign in page -> user name")
        self.sign_in_page.clear_and_fill_in_field(self.sign_in_page.txt_USER_NAME, username, "User name")
        c_logger.info("Clicking Sign in page -> next button")
        self.sign_in_page.click(self.sign_in_page.btn_NEXT, "Next button")
        c_logger.info(f"Verifying that the user name '{username}' is valid")
        assert not self.sign_in_page.is_element_visible(
            self.sign_in_page.lbl_INVALID_USER_NAME,
            "Invalid user name error message"), f"Invalid username: '{username}'"
        c_logger.info("Sign in page -> filling in password")
        self.sign_in_page.clear_and_fill_in_field(self.sign_in_page.txt_PASSWORD, password, "User password",
                                                  sensitive_data=True)
        self.sign_in_page.click(self.sign_in_page.btn_NEXT, "Next button")
        c_logger.info(f"Verifying that the user '{username}' password is valid")
        assert not self.sign_in_page.is_element_visible(self.sign_in_page.lbl_INVALID_PASSWORD,
                                                        "Invalid password error message"), "Invalid password"
        c_logger.info(f"Verifying that the '{username}' is displayed on the home page")
        self.home_page.click(self.home_page.btn_AVTAR, "Avtar button")
        assert self.home_page.get_text(self.home_page.lbl_USER_NAME, "User Name") == username.lower()

        return True

    @staticmethod
    def sign_out(active_page):
        """Method for Yahoo sign in
        Args :
            active_page : current page, from where sign out to be performed
        Returns:
            True - if successful
        Raises:
            None
        """
        active_page.click(active_page.btn_AVTAR, "Finance page -> Avtar")
        active_page.click(active_page.btn_SIGN_OUT, "Sign out button")
        return True
