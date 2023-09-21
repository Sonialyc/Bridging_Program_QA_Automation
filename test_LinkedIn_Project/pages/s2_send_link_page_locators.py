from selenium.webdriver.common.by import By


class SendLinkPageLocators:
    WRITE_A_MESSAGE_BOX = (By.CSS_SELECTOR, "[aria-label*='Write a message…']")
    SEND = (By.CSS_SELECTOR, "[type*='submit']")
    CLOSE_MESSAGE_BOX = (By.XPATH, "//button[contains(., 'Close your conversation with')]")
    LINK_SENT_SUCCESSFULLY = (By.XPATH, "//li[contains(@class, 'msg-s-message-list__event')][last()]//p[contains(text(), 'Sharing my GitHub profile:')]")
