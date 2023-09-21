import time
from test_LinkedIn_Project.pages.base_page import BasePage
from test_LinkedIn_Project.pages.s1_signout_page_locators import SignoutPageLocators


class SignoutPage(BasePage):

    def click_me_button(self):
        # Click on the "Me" button
        me_button = self.find_element(SignoutPageLocators.ME_BUTTON)
        self.click_element_alternatively(me_button)
        time.sleep(5)

    def click_signout_button(self):
        # Click on the "Sign Out" button
        signout_button = self.find_element(SignoutPageLocators.SIGNOUT_BUTTON)
        self.click_element_alternatively(signout_button)