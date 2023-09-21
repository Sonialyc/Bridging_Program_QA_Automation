import time
from test_LinkedIn_Project.pages.base_page import BasePage
from test_LinkedIn_Project.pages.s3_advanced_search_page_locators import AdvancedSearchPageLocators
from test_LinkedIn_Project.resources.constants import MAX_WAIT_INTERVAL


class AdvancedSearchPage(BasePage):

    def wait_and_click_all_filters_button(self):
        # Wait for the "All Filters" button to be located and click it
        all_filters_button = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, AdvancedSearchPageLocators.FILTERS)
        self.click_element_alternatively(all_filters_button)

    def wait_and_click_experience_level_button(self):
        # Wait for the experience level checkboxes to be located and click them
        entry_level = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, AdvancedSearchPageLocators.ENTRY_LEVEL_CHECKBOX)
        self.click_element_alternatively(entry_level)
        time.sleep(2)
        associate = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, AdvancedSearchPageLocators.ASSOCIATE_CHECKBOX)
        self.click_element_alternatively(associate)
        time.sleep(2)

    def click_job_type(self):
        # Click on the job type checkboxes
        full_time = self.find_element(AdvancedSearchPageLocators.FULL_TIME_CHECKBOX)
        self.click_element_alternatively(full_time)
        time.sleep(2)
        contract = self.find_element(AdvancedSearchPageLocators.CONTRACT_CHECKBOX)
        self.click_element_alternatively(contract)
        time.sleep(2)

    def click_location(self):
        # Click on the location checkboxes
        toronto = self.find_element(AdvancedSearchPageLocators.LOCATION_TORONTO_CHECKBOX)
        self.click_element_alternatively(toronto)
        time.sleep(2)
        north_york = self.find_element(AdvancedSearchPageLocators.LOCATION_NORTHYORK_CHECKBOX)
        self.click_element_alternatively(north_york)
        time.sleep(2)
        scarborough = self.find_element(AdvancedSearchPageLocators.LOCATION_SCARBOROUGH_CHECKBOX)
        self.click_element_alternatively(scarborough)
        time.sleep(2)

    def click_job_function(self):
        # Click on the job function checkboxes
        job_function = self.find_element(AdvancedSearchPageLocators.QUALITY_ASSURANCE_CHECKBOX)
        self.click_element_alternatively(job_function)
        time.sleep(2)

    def click_show_results_button(self):
        # Click on the "Show Results" button
        show_results = self.find_element(AdvancedSearchPageLocators.SHOW_RESULTS_BUTTON)
        self.click_element_alternatively(show_results)
        time.sleep(2)
