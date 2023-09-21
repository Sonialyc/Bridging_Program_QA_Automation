from selenium.webdriver.common.by import By


class ReactToMessagePageLocators:
    LATEST_MESSAGE = (By.XPATH, "//li[contains(@class, 'msg-s-message-list__event') and contains(@class, 'clearfix')][last()]")
    OPEN_EMOJI_KEYBOARD = (By.XPATH, "//button[@title='Open Emoji Keyboard' and @aria-label='Open Emoji Keyboard' and @aria-expanded='true']")
    REACT_WITH_THUMBS_UP = (By.CSS_SELECTOR, "[aria-label*='React with thumbs up']")
    REACTED_SUCCESSFULLY = (By.XPATH, "//li[contains(@class, 'msg-s-message-list__event') and contains(@class, 'clearfix')][last()]")
