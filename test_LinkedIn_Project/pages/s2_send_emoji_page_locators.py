from selenium.webdriver.common.by import By


class SendEmojiPageLocators:
    OPEN_EMOJI_KEYBOARD = (By.XPATH, "//button[@title='Open Emoji Keyboard' and @aria-label='Open Emoji Keyboard']")
    WRITE_A_MESSAGE_BOX = (By.CSS_SELECTOR, "[aria-label*='Write a message…']")
    EMOJI_SMILING_FACE_WITH_SMILING_EYES = (By.XPATH, "//section[@id='emojis-section-people']//button[contains(@title, 'smiling face with smiling eyes')]")
    EMOJI_THUMBS_UP = (By.XPATH, "//section[@id='emojis-section-people']//button[contains(@title, 'thumbs up')]")
    EMOJI_SUM_WITH_FACE = (By.XPATH, "//section[@id='emojis-section-travel']//button[contains(@title, 'sun with face')]")
    SEND = (By.CSS_SELECTOR, "[type*='submit']")
    MESSAGE_WITH_EMOJI_SENT_SUCCESSFULLY = (By.XPATH, "//li[contains(@class, 'msg-s-message-list__event') and contains(@class, 'clearfix')][last()]")
