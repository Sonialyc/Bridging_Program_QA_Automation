import time
from test_LinkedIn_Project.pages.base_page import BasePage
from test_LinkedIn_Project.pages.s2_send_message_page_locators import SendMessagePageLocators
from test_LinkedIn_Project.resources.constants import MAX_WAIT_INTERVAL


class SendMessagePage(BasePage):

    def wait_and_click_my_network_button(self):
        # Wait for the "My Network" button to be located and click it
        my_network_button = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, SendMessagePageLocators.MY_NETWORK)
        self.click_element_alternatively(my_network_button)

    def wait_and_click_connection_button(self):
        # Wait for the "Connection" button to be located and click it
        connection_button = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, SendMessagePageLocators.CONNECTION)
        self.click_element_alternatively(connection_button)

    def wait_and_click_message_button(self):
        # Wait for the "Message" button to be located and click it
        message_button = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, SendMessagePageLocators.MESSAGE)
        self.click_element_alternatively(message_button)

    def wait_and_expand_new_message_box(self):
        # Wait for the "Expand Message Box" button for initiating a New Conversation to be located and click it
        expand_new_message_box = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, SendMessagePageLocators.EXPAND_NEW_MESSAGE_BOX)
        self.click_element_alternatively(expand_new_message_box)

    def wait_and_expand_message_box(self):
        # Wait for the "Expand Message Box" button for an Existing Conversation to be located and click it
        expand_message_box = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, SendMessagePageLocators.EXPAND_MESSAGE_BOX)
        self.click_element_alternatively(expand_message_box)

    def wait_and_type_message(self, privatemessage):
        # Wait for the message box to be located, type the private message, and sleep
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, SendMessagePageLocators.WRITE_A_MESSAGE_BOX).send_keys(privatemessage[0])
        time.sleep(2)

    def click_send_button(self):
        # Click the "Send" button and sleep
        send_button = self.find_element(SendMessagePageLocators.SEND)
        self.click_element_alternatively(send_button)
        time.sleep(3)

    def message_sent_successfully_label(self):
        # Method to get the text of the message sent successfully label
        lbl_message_sent_successfully_txt = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, SendMessagePageLocators.MESSAGE_SENT_SUCCESSFULLY).text
        return lbl_message_sent_successfully_txt

