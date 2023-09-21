from test_LinkedIn_Project.pages.base_page import BasePage
from test_LinkedIn_Project.pages.s1_index_page_locators import IndexPageLocators
from test_LinkedIn_Project.resources.constants import MAX_WAIT_INTERVAL


class IndexPage(BasePage):

    def wait_and_click_signin_button(self):
        # Wait for the "Sign In" button to be located and click it
        signin_button = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, IndexPageLocators.SIGNIN)
        self.click_element_alternatively(signin_button)
