from test_LinkedIn_Project.pages.base_page import BasePage
from test_LinkedIn_Project.pages.s3_job_search_success_page_locators import JobSearchSuccessPageLocators
from test_LinkedIn_Project.resources.constants import MAX_WAIT_INTERVAL


class JobSearchSuccessPage(BasePage):

    def get_job_search_success_label(self):
        # Wait for the element with the specified locator to be present
        # Retrieve the text of the element and store it in lbl_job_search_success_txt
        lbl_job_search_success_txt = self.explicitly_wait_and_find_element(
            MAX_WAIT_INTERVAL, JobSearchSuccessPageLocators.RESULTS_LIST_TITLE).text
        return lbl_job_search_success_txt
