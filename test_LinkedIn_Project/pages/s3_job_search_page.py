import time
from test_LinkedIn_Project.pages.base_page import BasePage
from test_LinkedIn_Project.pages.s3_job_search_page_locators import JobSearchPageLocators
from selenium.webdriver.common.keys import Keys
from test_LinkedIn_Project.resources.constants import MAX_WAIT_INTERVAL


class JobSearchPage(BasePage):

    def wait_and_click_jobs_button(self):
        # Wait for the "Jobs" button to be located and click it
        jobs_button = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, JobSearchPageLocators.JOBS)
        self.click_element_alternatively(jobs_button)

    def wait_and_type_job_keyword(self, postandlocation):
        # Wait for the job search box, type the job keyword, and sleep
        job_search_box = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, JobSearchPageLocators.SEARCH_BOX)
        job_search_box.send_keys(postandlocation[0])
        time.sleep(2)

    def type_location(self, postandlocation):
        # Type the location in the location search box, press Enter, and sleep
        location_search_box = self.find_element(JobSearchPageLocators.LOCATION_BOX)
        location_search_box.send_keys(postandlocation[1])
        time.sleep(2)
        location_search_box.send_keys(Keys.ENTER)
