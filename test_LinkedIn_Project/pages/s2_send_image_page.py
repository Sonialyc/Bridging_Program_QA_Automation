import time
import autoit  # Using AutoIt for interacting with file dialogs
from test_LinkedIn_Project.pages.base_page import BasePage
from test_LinkedIn_Project.pages.s2_send_image_page_locators import SendImagePageLocators
from test_LinkedIn_Project.resources.constants import MAX_WAIT_INTERVAL


class SendImagePage(BasePage):

    def upload_image(self, file_path):
        # Locate the "attach an image" button
        attach_button = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL,
                                                              SendImagePageLocators.UPLOAD_IMAGE_BUTTON)
        attach_button.click()  # Click on the "attach an image" button
        time.sleep(2)  # Wait a bit for the dialog to appear

        # Use autoit to interact with the file upload dialog
        autoit.control_set_text("Open", "Edit1", file_path[1])  # Set the file path
        autoit.control_click("Open", "Button1")  # Click the "Open" button
        time.sleep(3)  # Wait for the upload to complete

    def click_send_button(self):
        # Click the "Send" button and sleep
        send_button = self.find_element(SendImagePageLocators.SEND)
        self.click_element_alternatively(send_button)
        time.sleep(2)
