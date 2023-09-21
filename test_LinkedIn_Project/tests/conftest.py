import time
import pytest as pytest
from selenium import webdriver
# Project created by Sonialyc


# Fixture to create and close a browser instance
@pytest.fixture(scope="module")
def driver():
    _driver = webdriver.Chrome()
    # _driver = webdriver.Edge()
    time.sleep(3)
    _driver.refresh()
    _driver.maximize_window()
    yield _driver
    _driver.quit()


# Fixture to provide email and password for login
@pytest.fixture(scope="function")
def email_password():
    email = "[your email address]"
    password = "[correct password]"
    incorrectpw = "[incorrect password]"
    return [email, password, incorrectpw]


# Fixture to provide content for private messages
@pytest.fixture(scope="function")
def private_message():
    greeting = "Hello! How are you?"
    image_path = "[your image path]"
    sunny = "It's a sunny day. "
    link = "Sharing my GitHub profile: [your GitHub link]. Feel free to take a look or reach out with any questions."
    return [greeting, image_path, sunny, link]


# Fixture to provide keyword and location for job search
@pytest.fixture(scope="function")
def keyword_location():
    keyword = "Quality Assurance"
    location = "Toronto, Ontario, Canada"
    return [keyword, location]
