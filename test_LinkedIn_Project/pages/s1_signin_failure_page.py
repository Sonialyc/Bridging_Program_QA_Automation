import time
from test_LinkedIn_Project.pages.base_page import BasePage
from test_LinkedIn_Project.pages.s1_signin_failure_page_locators import SigninFailurePageLocators
from test_LinkedIn_Project.resources.constants import MAX_WAIT_INTERVAL


class SigninFailurePage(BasePage):

    def wait_and_type_user_email(self, useremailandpwlist):
        # Wait for the email text box to be located and type the user's email
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, SigninFailurePageLocators.EMAIL_TEXT_BOX).send_keys(
            useremailandpwlist[0])

    def type_incorrect_password(self, useremailandpwlist):
        # Type the incorrect password in the password text box
        self.find_element(SigninFailurePageLocators.PASSWORD_TEXT_BOX).send_keys(
            useremailandpwlist[2])

    def click_signin_button(self):
        # Click the "Sign In" button
        signin_button = self.find_element(SigninFailurePageLocators.SIGNIN_BUTTON)
        self.click_element_alternatively(signin_button)
        time.sleep(2)

    def get_signin_failure_label(self):
        # Get the text of the sign-in failure warning message
        lbl_signin_failure_txt = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, SigninFailurePageLocators.WARNING_MSG).text
        return lbl_signin_failure_txt
