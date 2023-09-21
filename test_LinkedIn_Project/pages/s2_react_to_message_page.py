import time
from test_LinkedIn_Project.pages.base_page import BasePage
from test_LinkedIn_Project.pages.s2_react_to_message_page_locators import ReactToMessagePageLocators
from test_LinkedIn_Project.resources.constants import MAX_WAIT_INTERVAL


class ReactToMessagePage(BasePage):

    def wait_and_find_latest_message(self):
        # Wait for the latest message element to be present and visible, then click it
        latest_message = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, ReactToMessagePageLocators.LATEST_MESSAGE)
        self.click_element_alternatively(latest_message)
        time.sleep(2)

    def wait_and_open_emoji_keyboard(self):
        # Hover over a message and wait for the "Open Emoji Keyboard" button to be present and click it
        emoji_keyboard = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, ReactToMessagePageLocators.OPEN_EMOJI_KEYBOARD)
        self.click_element_alternatively(emoji_keyboard)
        time.sleep(3)

    def wait_and_open_second_emoji_keyboard(self):
        # Wait for the "Open Emoji Keyboard" button, under a message, to be present and click it
        second_emoji_keyboard = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, ReactToMessagePageLocators.OPEN_SECOND_EMOJI_KEYBOARD)
        self.click_element_alternatively(second_emoji_keyboard)
        time.sleep(3)

    def wait_and_select_emoji_thumbs_up(self):
        # Wait for the "Thumbs Up" emoji button to be present and click it
        emoji_thumbs_up = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL,
                                              ReactToMessagePageLocators.REACT_WITH_THUMBS_UP)
        self.click_element_alternatively(emoji_thumbs_up)
        time.sleep(2)

    def wait_and_select_emoji_grinning_face_with_smiling_eyes(self):
        # Wait for the "Grinning Face with Smiling Eyes" emoji button to be clickable and click it
        emoji_grinning_face_with_smiling_eyes = self.explicitly_wait_element_to_be_clickable(MAX_WAIT_INTERVAL, ReactToMessagePageLocators.REACT_GRINNING_FACE_WITH_SMILING_EYES)
        self.click_element_alternatively(emoji_grinning_face_with_smiling_eyes)
        time.sleep(3)
