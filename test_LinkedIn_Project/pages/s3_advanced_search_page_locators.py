from selenium.webdriver.common.by import By


class AdvancedSearchPageLocators:
    FILTERS = (By.CSS_SELECTOR, "[aria-label*='all filters']")
    ENTRY_LEVEL_CHECKBOX = (By.XPATH, "//label[contains(., 'Entry level')]")
    ASSOCIATE_CHECKBOX = (By.XPATH, "//label[contains(., 'Associate')]")
    FULL_TIME_CHECKBOX = (By.XPATH, "//label[contains(., 'Full-time')]")
    CONTRACT_CHECKBOX = (By.XPATH, "//label[contains(., 'Contract')]")
    LOCATION_TORONTO_CHECKBOX = (By.XPATH, "//label[contains(., 'Toronto, ON')]")
    LOCATION_NORTHYORK_CHECKBOX = (By.XPATH, "//label[contains(., 'North York, ON')]")
    LOCATION_SCARBOROUGH_CHECKBOX = (By.XPATH, "//label[contains(., 'Scarborough, ON')]")
    QUALITY_ASSURANCE_CHECKBOX = (By.XPATH, "//label[contains(., 'Quality Assurance')]")
    SHOW_RESULTS_BUTTON = (By.CSS_SELECTOR, "[class*='results']")
