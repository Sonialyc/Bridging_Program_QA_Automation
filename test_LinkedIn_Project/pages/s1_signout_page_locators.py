from selenium.webdriver.common.by import By


class SignoutPageLocators:
    ME_BUTTON = (By.XPATH, "//button[contains(@class, 'global-nav__primary-link-me-menu-trigger')]")
    SIGNOUT_BUTTON = (By.XPATH, "//a[contains(., 'Sign Out')]")
