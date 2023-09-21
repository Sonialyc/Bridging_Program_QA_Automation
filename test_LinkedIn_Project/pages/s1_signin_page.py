import time
from test_LinkedIn_Project.pages.base_page import BasePage
from test_LinkedIn_Project.pages.s1_signin_page_locators import SigninPageLocators
from test_LinkedIn_Project.resources.constants import MAX_WAIT_INTERVAL


class SigninPage(BasePage):

    def wait_and_type_user_email(self, useremailandpwlist):
        # Wait for the email text box to be located and type the user's email
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, SigninPageLocators.EMAIL_TEXT_BOX).send_keys(
            useremailandpwlist[0])

    def type_password(self, useremailandpwlist):
        # Type the user's password in the password text box
        self.find_element(SigninPageLocators.PASSWORD_TEXT_BOX).send_keys(
            useremailandpwlist[1])

    def click_signin_button(self):
        # Click the "Sign In" button
        signin_button = self.find_element(SigninPageLocators.SIGNIN_BUTTON)
        self.click_element_alternatively(signin_button)
        time.sleep(8)

    def wait_and_close_messaging_box(self):
        # Wait for the messaging box to be located and close it
        close_messaging_box = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, SigninPageLocators.CLOSE_MESSAGING_BOX)
        self.click_element_alternatively(close_messaging_box)
        time.sleep(3)
