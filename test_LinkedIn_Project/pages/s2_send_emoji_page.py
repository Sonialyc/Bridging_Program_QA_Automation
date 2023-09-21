import time
from test_LinkedIn_Project.pages.base_page import BasePage
from test_LinkedIn_Project.pages.s2_send_emoji_page_locators import SendEmojiPageLocators
from selenium.common import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from test_LinkedIn_Project.resources.constants import MAX_WAIT_INTERVAL


class SendEmojiPage(BasePage):
    # Function to wait for and open the emoji keyboard using JavaScript click
    def wait_and_open_emoji_keyboard(self):
        try:
            emoji_keyboard = self.explicitly_wait_element_to_be_clickable(MAX_WAIT_INTERVAL,
                                                                          SendEmojiPageLocators.OPEN_EMOJI_KEYBOARD)
            self.click_element_alternatively(emoji_keyboard)
            time.sleep(3)
        except TimeoutException:
            print("Timeout while waiting for element to be clickable.")
        except Exception as e:
            print(f"An error occurred while clicking the element: {str(e)}")

    def wait_and_type_message(self, messagewithemoji):
        # Wait for the message box to be located, type the message with emoji, and sleep
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, SendEmojiPageLocators.WRITE_A_MESSAGE_BOX).send_keys(messagewithemoji[2])
        time.sleep(3)

    def wait_and_select_emoji_smiling_face_with_smiling_eyes(self):
        # Click to select the smiling face with smiling eyes emoji and wait
        emoji_smiling_face_with_smiling_eyes = self.explicitly_wait_element_to_be_clickable(MAX_WAIT_INTERVAL, SendEmojiPageLocators.EMOJI_SMILING_FACE_WITH_SMILING_EYES)
        self.click_element_alternatively(emoji_smiling_face_with_smiling_eyes)
        time.sleep(3)

    def wait_and_select_emoji_thumbs_up(self):
        # Click to select the thumbs up emoji and wait
        emoji_thumbs_up = self.explicitly_wait_element_to_be_clickable(MAX_WAIT_INTERVAL, SendEmojiPageLocators.EMOJI_THUMBS_UP)
        self.click_element_alternatively(emoji_thumbs_up)
        time.sleep(3)

    def wait_and_select_emoji_sun_with_face(self):
        # Click to select the sun with face emoji and wait
        emoji_sun_with_face = self.explicitly_wait_element_to_be_clickable(MAX_WAIT_INTERVAL, SendEmojiPageLocators.EMOJI_SUM_WITH_FACE)
        self.click_element_alternatively(emoji_sun_with_face)
        time.sleep(3)

    def click_send_button(self):
        # Click the "Send" button and sleep
        send_button = self.find_element(SendEmojiPageLocators.SEND)
        self.click_element_alternatively(send_button)
        time.sleep(3)

    def message_with_emoji_sent_successfully_label(self):
        # Get and return the text of the message with emoji sent successfully label
        lbl_message_with_emoji_sent_successfully_txt = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, SendEmojiPageLocators.MESSAGE_WITH_EMOJI_SENT_SUCCESSFULLY).text
        return lbl_message_with_emoji_sent_successfully_txt
