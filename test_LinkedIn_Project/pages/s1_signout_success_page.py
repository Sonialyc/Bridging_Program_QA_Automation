from test_LinkedIn_Project.pages.base_page import BasePage
from test_LinkedIn_Project.pages.s1_signout_success_page_locators import SignoutSuccessPageLocators
from test_LinkedIn_Project.resources.constants import MAX_WAIT_INTERVAL


class SignoutSuccessPage(BasePage):

    def get_signout_success_label(self):
        # Get the text of the logout success label
        lbl_signout_success_txt = self.explicitly_wait_and_find_element(
            MAX_WAIT_INTERVAL, SignoutSuccessPageLocators.LOGOUT_SUCCESS_LBL).text
        return lbl_signout_success_txt
