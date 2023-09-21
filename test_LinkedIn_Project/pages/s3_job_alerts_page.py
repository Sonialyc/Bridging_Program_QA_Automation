import time
from test_LinkedIn_Project.pages.base_page import BasePage
from test_LinkedIn_Project.pages.s3_job_alerts_page_locators import JobAlertsPageLocators
from test_LinkedIn_Project.resources.constants import MAX_WAIT_INTERVAL


class JobAlertsPage(BasePage):

    def click_set_alert_button(self):
        # Wait for the "Set Alert" button to be located and click it
        set_alert = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, JobAlertsPageLocators.SET_ALERT)
        self.click_element_alternatively(set_alert)
        time.sleep(2)

    def click_remove_alert_button(self):
        # Wait for the "Remove Alert" button to be located and click it
        remove_alert = self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, JobAlertsPageLocators.REMOVE_ALERT)
        self.click_element_alternatively(remove_alert)
        time.sleep(2)
