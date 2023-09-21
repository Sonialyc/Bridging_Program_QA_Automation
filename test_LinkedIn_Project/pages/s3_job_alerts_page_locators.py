from selenium.webdriver.common.by import By


class JobAlertsPageLocators:
    SET_ALERT = (By.XPATH, "//span[contains(., 'Set alert')]")
    REMOVE_ALERT = (By.XPATH, "//span[contains(., 'Alert on')]")
