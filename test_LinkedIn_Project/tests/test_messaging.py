from test_LinkedIn_Project.tests.test_utils import *
from test_LinkedIn_Project.pages.s1_index_page import IndexPage
from test_LinkedIn_Project.pages.s1_signin_page import SigninPage
from test_LinkedIn_Project.pages.s1_signin_success_page import SigninSuccessPage
from selenium.common import NoSuchElementException
from test_LinkedIn_Project.pages.s2_send_message_page import SendMessagePage
from test_LinkedIn_Project.pages.s2_send_image_page import SendImagePage
from test_LinkedIn_Project.pages.s2_send_image_page_locators import SendImagePageLocators
from test_LinkedIn_Project.pages.s2_send_emoji_page import SendEmojiPage
from test_LinkedIn_Project.pages.s2_send_emoji_page_locators import SendEmojiPageLocators
from test_LinkedIn_Project.pages.s2_react_to_message_page import ReactToMessagePage
from test_LinkedIn_Project.pages.s2_react_to_message_page_locators import ReactToMessagePageLocators
from test_LinkedIn_Project.pages.s2_send_link_page import SendLinkPage
from test_LinkedIn_Project.pages.s2_send_link_page_locators import SendLinkPageLocators
from test_LinkedIn_Project.pages.s1_signout_page import SignoutPage
from test_LinkedIn_Project.pages.s1_signout_success_page import SignoutSuccessPage
from test_LinkedIn_Project.resources.constants import TEST_SITE_URL
# Project created by Sonialyc


class TestMessaging:
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

    # Test Cases 6 - 10 (Send Messages, image, emojis, react to messages and send links)
    def test_messaging(self, driver, private_message):
        # Navigate to the messaging section of the site
        send_message_page = SendMessagePage(driver)
        send_message_page.wait_and_click_my_network_button()
        send_message_page.wait_and_click_connection_button()
        send_message_page.wait_and_click_message_button()
        try:
            send_message_page.wait_and_expand_new_message_box()
        except NoSuchElementException:
            send_message_page.wait_and_expand_message_box()

        # Test Case 6: Send a private message to a connection
        send_message_page.wait_and_type_message(private_message)
        send_message_page.click_send_button()

        # Assertion: Check if the message was sent successfully
        message_sent_successfully_lbl = send_message_page.message_sent_successfully_label()
        assert message_sent_successfully_lbl.__contains__("Hello! How are you?"), "Private message sending unsuccessful!"

        # Test Case 7: Send an image attachment through a message
        send_image_page = SendImagePage(driver)
        send_image_page.upload_image(private_message)
        send_image_page.click_send_button()

        # Assertion: Check if the image was sent successfully
        assert send_image_page.is_element_present(SendImagePageLocators.IMAGE_SENT_SUCCESSFULLY), "Image sending unsuccessful!"

        # Test Case 8: Use emojis in a message and confirm their display
        send_emoji_page = SendEmojiPage(driver)

        # Send first emoji
        send_emoji_page.wait_and_open_emoji_keyboard()
        send_emoji_page.wait_and_select_emoji_smiling_face_with_smiling_eyes()
        send_emoji_page.click_send_button()

        # Send second emoji
        send_emoji_page.wait_and_open_emoji_keyboard()
        send_emoji_page.wait_and_select_emoji_thumbs_up()
        send_emoji_page.click_send_button()

        # Assertion: Check if the emojis were successfully added to the message
        assert send_emoji_page.is_element_present(SendEmojiPageLocators.EMOJI_SMILING_FACE_WITH_SMILING_EYES), "Emoji not added to message."
        assert send_emoji_page.is_element_present(SendEmojiPageLocators.EMOJI_THUMBS_UP), "Emoji not added to message."
        assert send_emoji_page.is_element_present(SendEmojiPageLocators.EMOJI_SUM_WITH_FACE), "Emoji not added to message."

        # Send a message with emoji
        send_emoji_page.wait_and_type_message(private_message)
        send_emoji_page.wait_and_open_emoji_keyboard()
        send_emoji_page.wait_and_select_emoji_sun_with_face()
        send_emoji_page.click_send_button()

        # Assertion: Check if the emojis were added successfully to the message
        message_with_emoji_sent_successfully_text = send_emoji_page.message_with_emoji_sent_successfully_label()
        assert message_with_emoji_sent_successfully_text.__contains__("It's a sunny day. 🌞"), "Message with emoji sending unsuccessful!"

        # Test Case 9: Verify the functionality of reacting to the latest message
        react_to_message_page = ReactToMessagePage(driver)
        react_to_message_page.wait_and_find_latest_message()
        react_to_message_page.wait_and_select_emoji_thumbs_up()

        # Assertion: Check if the emojis were added successfully to the message
        assert react_to_message_page.is_element_present(ReactToMessagePageLocators.REACTED_SUCCESSFULLY), "Emojis not added to message!"

        # Test Case 10: Send a message with a link and confirm link preview
        send_link_page = SendLinkPage(driver)
        send_link_page.wait_and_type_link(private_message)
        send_link_page.click_send_button()

        # Assertion: Check if the link message was sent and link preview is displayed
        assert send_link_page.is_element_present(SendLinkPageLocators.LINK_SENT_SUCCESSFULLY), "Link message sending or preview unsuccessful!"

        send_link_page.click_close_messaging_box()

    # Test Case 4: Logout and verify user is logged out successfully
    def test_signout(self, driver):
        signout_page = SignoutPage(driver)
        signout_page.click_me_button()
        signout_page.click_signout_button()

        signout_success_page = SignoutSuccessPage(driver)
        signout_success_lbl = signout_success_page.get_signout_success_label()
        assert signout_success_lbl.__contains__("About"), "User sign out unsuccessful!"
