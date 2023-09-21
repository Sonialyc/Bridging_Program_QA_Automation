from test_LinkedIn_Project.pages.base_page import BasePage
from test_LinkedIn_Project.pages.s1_signin_success_page_locators import SigninSuccessPageLocators
from test_LinkedIn_Project.resources.constants import MAX_WAIT_INTERVAL


class SigninSuccessPage(BasePage):

    def get_signin_success_label(self):
        # Get the text of the username label on the success page
        lbl_signin_success_txt = self.explicitly_wait_and_find_element(
            MAX_WAIT_INTERVAL, SigninSuccessPageLocators.USERNAME_ELEMENT).text
        return lbl_signin_success_txt
