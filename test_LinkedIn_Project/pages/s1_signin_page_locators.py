from selenium.webdriver.common.by import By


class SigninPageLocators:
    EMAIL_TEXT_BOX = (By.ID, "username")
    PASSWORD_TEXT_BOX = (By.ID, "password")
    SIGNIN_BUTTON = (By.XPATH, "//*[@id='organic-div']/form/div[3]/button")
    CLOSE_MESSAGING_BOX = (By.XPATH, "//div[contains(@class, 'msg-overlay-bubble-header__controls display-flex')]/child::button[2]")
