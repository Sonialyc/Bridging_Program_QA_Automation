from selenium.webdriver.common.by import By


class JobSearchPageLocators:
    JOBS = (By.XPATH, "//*[@id='global-nav']/div/nav/ul/li[3]/a")
    SEARCH_BOX = (By.CSS_SELECTOR, '[id*="jobs-search-box-keyword-id"]')
    LOCATION_BOX = (By.CSS_SELECTOR, '[id*="jobs-search-box-location-id"]')
