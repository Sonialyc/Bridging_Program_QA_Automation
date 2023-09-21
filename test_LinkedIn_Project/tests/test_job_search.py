from test_LinkedIn_Project.tests.test_utils import *
from test_LinkedIn_Project.pages.s1_index_page import IndexPage
from test_LinkedIn_Project.pages.s1_signin_page import SigninPage
from test_LinkedIn_Project.pages.s1_signin_success_page import SigninSuccessPage
from selenium.common import NoSuchElementException
from test_LinkedIn_Project.pages.s3_job_search_page import JobSearchPage
from test_LinkedIn_Project.pages.s3_advanced_search_page import AdvancedSearchPage
from test_LinkedIn_Project.pages.s3_job_alerts_page import JobAlertsPage
from test_LinkedIn_Project.pages.s3_job_search_success_page import JobSearchSuccessPage
from test_LinkedIn_Project.pages.s1_signout_page import SignoutPage
from test_LinkedIn_Project.pages.s1_signout_success_page import SignoutSuccessPage
from test_LinkedIn_Project.resources.constants import TEST_SITE_URL
# Project created by Sonialyc


class TestJobSearch:
    # Test Case 1: Validate successful login using valid credentials and verify accurate display of user profile information post-login
    def test_signin(self, driver, email_password):
        # Test steps to log in
        index_page = IndexPage(driver)
        index_page.navigate_to(TEST_SITE_URL)
        index_page.navigate_to(TEST_SITE_URL)
        index_page.wait_and_click_signin_button()

        signin_page = SigninPage(driver)
        signin_page.wait_and_type_user_email(email_password)
        signin_page.type_password(email_password)
        signin_page.click_signin_button()

        # Verify the login success label
        signin_success_page = SigninSuccessPage(driver)
        signin_success_lbl = signin_success_page.get_signin_success_label()
        assert signin_success_lbl.__contains__("[Your profile name]"), "User sign in unsuccessful!"

        # Close the messaging box if it appears
        try:
            signin_page.wait_and_close_messaging_box()
        except NoSuchElementException:
            print("Messaging box not appeared")

    # Test Cases 11 to 13 (Job Search, Advanced Search, and Job Alerts)
    def test_job_search(self, driver, keyword_location):
        # Test Case 11:	Search for job listings based on keywords and location
        job_search_page = JobSearchPage(driver)
        job_search_page.wait_and_click_jobs_button()
        job_search_page.wait_and_type_job_keyword(keyword_location)
        job_search_page.type_location(keyword_location)

        # Test Case 12: Use advanced search filters for job listings
        advanced_search_page = AdvancedSearchPage(driver)
        advanced_search_page.wait_and_click_all_filters_button()
        advanced_search_page.wait_and_click_experience_level_button()
        advanced_search_page.click_job_type()
        advanced_search_page.click_location()
        advanced_search_page.click_job_function()
        advanced_search_page.click_show_results_button()

        # Test Case 13: Sets a job alert and verifies the removal of the job alert
        job_alerts_page = JobAlertsPage(driver)
        job_alerts_page.click_set_alert_button()
        job_alerts_page.click_remove_alert_button()

        # Verify the job search success label
        job_search_success_page = JobSearchSuccessPage(driver)
        job_search_success_lbl = job_search_success_page.get_job_search_success_label()
        assert job_search_success_lbl.__contains__(f"{keyword_location[0]} in {keyword_location[1]}"), f"Job search for '{keyword_location[0]}' in '{keyword_location[1]}' unsuccessful."

    # Test Case 4: Logout and verify user is logged out successfully
    def test_signout(self, driver):
        signout_page = SignoutPage(driver)
        signout_page.click_me_button()
        signout_page.click_signout_button()

        signout_success_page = SignoutSuccessPage(driver)
        signout_success_lbl = signout_success_page.get_signout_success_label()
        assert signout_success_lbl.__contains__("About"), "User sign out unsuccessful!"
