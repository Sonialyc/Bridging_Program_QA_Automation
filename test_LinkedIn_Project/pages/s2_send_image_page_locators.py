from selenium.webdriver.common.by import By


class SendImagePageLocators:
    UPLOAD_IMAGE_BUTTON = (By.XPATH, "//button[starts-with(@id, 'attachment-trigger-ember')]")
    SEND = (By.CSS_SELECTOR, "[type*='submit']")
    IMAGE_SENT_SUCCESSFULLY = (By.XPATH, "//li[contains(@class, 'msg-s-message-list__event') and contains(@class, 'clearfix')][last()]")
