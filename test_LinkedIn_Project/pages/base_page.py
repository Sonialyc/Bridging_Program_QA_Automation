import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException
from selenium.common import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def navigate_to(self, url):
        self.driver.get(url)

    def explicitly_wait_and_find_element(self, interval, locator_type_and_locator_tuple):
        return WebDriverWait(self.driver, interval).until(
            ec.presence_of_element_located(locator_type_and_locator_tuple))

    def explicitly_wait_element_to_be_clickable(self, interval, locator_type_and_locator_tuple):
        return WebDriverWait(self.driver, interval).until(
            ec.element_to_be_clickable(locator_type_and_locator_tuple))

    def find_element(self, locator_type_and_locator_tuple):
        return self.driver.find_element(*locator_type_and_locator_tuple)

    def is_element_present(self, locator_type_and_locator_tuple):
        try:
            self.driver.find_element(*locator_type_and_locator_tuple)
            return True
        except NoSuchElementException:
            return False

    def click_element_alternatively(self, element):
        try:
            # Use JavaScript to click the element
            self.driver.execute_script("arguments[0].click();", element)
            time.sleep(3)
        except TimeoutException:
            # If the button is not clickable, attempt to click using ActionChains
            actions = ActionChains(self.driver)
            actions.move_to_element(element).click().perform()
            time.sleep(3)
            pass
