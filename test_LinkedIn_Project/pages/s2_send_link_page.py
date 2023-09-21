import time
from test_LinkedIn_Project.pages.base_page import BasePage
from test_LinkedIn_Project.pages.s2_send_link_page_locators import SendLinkPageLocators
from test_LinkedIn_Project.resources.constants import MAX_WAIT_INTERVAL


class SendLinkPage(BasePage):

    def wait_and_type_link(self, privatemessage):
        # Wait for the message box to be located, type the private link, and sleep
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, SendLinkPageLocators.WRITE_A_MESSAGE_BOX).send_keys(privatemessage[3])
        time.sleep(2)

    def click_send_button(self):
        # Click the "Send" button and sleep
        send_button = self.find_element(SendLinkPageLocators.SEND)
        self.click_element_alternatively(send_button)
        time.sleep(8)

    def click_close_messaging_box(self):
        # Click the "Close" button on the message box and sleep
        close_message = self.find_element(SendLinkPageLocators.CLOSE_MESSAGE_BOX)
        self.click_element_alternatively(close_message)
        time.sleep(3)
