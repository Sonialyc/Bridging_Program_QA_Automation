from selenium.webdriver.common.by import By


class SendMessagePageLocators:
    MY_NETWORK = (By.XPATH, "//*[@id='global-nav']/div/nav/ul/li[2]/a")
    CONNECTION = (By.CLASS_NAME, "mn-community-summary__entity-info")
    MESSAGE = (By.CSS_SELECTOR, "[aria-label*='Send a message to [your connection profile name]]']")
    EXPAND_NEW_MESSAGE_BOX = (By.CSS_SELECTOR, "[type*='maximize']")
    EXPAND_MESSAGE_BOX = (By.XPATH, "//button[contains(., 'Expand your conversation with')]")
    WRITE_A_MESSAGE_BOX = (By.CSS_SELECTOR, "[aria-label*='Write a message…']")
    SEND = (By.CSS_SELECTOR, "[type*='submit']")
    MESSAGE_SENT_SUCCESSFULLY = (By.XPATH, "//li[contains(@class, 'msg-s-message-list__event') and contains(@class, 'clearfix')][last()]")
