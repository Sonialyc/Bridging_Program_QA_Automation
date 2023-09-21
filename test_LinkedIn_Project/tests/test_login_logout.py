from test_LinkedIn_Project.tests.test_utils import *
from test_LinkedIn_Project.pages.s1_index_page import IndexPage
from test_LinkedIn_Project.pages.s1_signin_page import SigninPage
from test_LinkedIn_Project.pages.s1_signin_success_page import SigninSuccessPage
from selenium.common import NoSuchElementException
from test_LinkedIn_Project.pages.s1_signout_page import SignoutPage
from test_LinkedIn_Project.pages.s1_signout_success_page import SignoutSuccessPage
from test_LinkedIn_Project.pages.s1_signin_failure_page import SigninFailurePage
from test_LinkedIn_Project.resources.constants import TEST_SITE_URL
# Project created by Sonialyc


class TestSigninSignout:

    # Test Case 1: Validate successful login using valid credentials and verify accurate display of user profile information post-login
    def test_signin(self, driver, email_password):
        # Test steps to log in
        index_page = IndexPage(driver)
        index_page.navigate_to(TEST_SITE_URL)
        index_page.navigate_to(TEST_SITE_URL)
        index_page.wait_and_click_signin_button()

        signin_page = SigninPage(driver)
        signin_page.wait_and_type_user_email(email_password)
        signin_page.type_password(email_password)
        signin_page.click_signin_button()

        # Verify the login success label
        signin_success_page = SigninSuccessPage(driver)
        signin_success_lbl = signin_success_page.get_signin_success_label()
        assert signin_success_lbl.__contains__("[Your profile name]"), "User sign in unsuccessful!"

        # Close the messaging box if it appears
        try:
            signin_page.wait_and_close_messaging_box()
        except NoSuchElementException:
            print("Messaging box not appeared")

    # Test Case 4: Logout and verify user is logged out successfully
    def test_signout(self, driver):
        # Test steps to log out
        signout_page = SignoutPage(driver)
        signout_page.click_me_button()
        signout_page.click_signout_button()

        # Verify the sign out success label
        signout_success_page = SignoutSuccessPage(driver)
        signout_success_lbl = signout_success_page.get_signout_success_label()
        assert signout_success_lbl.__contains__("About"), "User sign out unsuccessful!"

    # Test Case 5: Attempt login with incorrect credentials and verify the appropriate error message
    def test_login_failure(self, driver, email_password):
        # Test steps to handle login failure
        index_page = IndexPage(driver)
        index_page.wait_and_click_signin_button()

        signin_failure_page = SigninFailurePage(driver)
        signin_failure_page.wait_and_type_user_email(email_password)
        signin_failure_page.type_incorrect_password(email_password)
        signin_failure_page.click_signin_button()

        # Verify the failure message
        signin_failure_lbl = signin_failure_page.get_signin_failure_label()
        assert signin_failure_lbl.__contains__("That's not the right password.") or signin_failure_lbl.__contains__("Wrong email or password. Try again or create an account"), "User sign-in was successful!"
