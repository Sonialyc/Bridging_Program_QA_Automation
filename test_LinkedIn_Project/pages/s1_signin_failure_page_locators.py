from selenium.webdriver.common.by import By


class SigninFailurePageLocators:
    EMAIL_TEXT_BOX = (By.ID, "username")
    PASSWORD_TEXT_BOX = (By.ID, "password")
    SIGNIN_BUTTON = (By.XPATH, "//*[@id='organic-div']/form/div[3]/button")
    WARNING_MSG = (By.ID, "error-for-password")
