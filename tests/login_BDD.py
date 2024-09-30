"""
This project automates the login and logout process for the OrangeHRM demo application using Selenium WebDriver
and Behavior Driven Development (BDD) principles implemented with pytest-bdd. The test scenarios are structured to
simulate user interactions with the login page, dashboard, and logout functionality, all while following the
Given-When-Then format of Gherkin syntax.
Check complete details in project_details.txt file
"""
# Behave is a behavior-driven development (BDD) framework for Python that allows you to write tests in a natural
# language style using Gherkin syntax. It helps in creating tests that are more readable and understandable for both
# technical and non-technical stakeholders.
# pytest -v tests/login_BDD.py
# pytest -v tests/login_BDD.py --html=report.html
"""
log results:
tests/login_BDD.py::test_open_webpage PASSED
tests/login_BDD.py::test_input_valid_credentials PASSED
tests/login_BDD.py::test_click_login_button PASSED
tests/login_BDD.py::test_redirect_to_dashboard PASSED
tests/login_BDD.py::test_logout PASSED
tests/login_BDD.py::test_close_browser PASSED
"""


"""
Open Report in browser to get results:
1) Navigate to the folder where report.html is saved.
2) Double-click on report.html. It will open in your default web browser.
"""

import sys
import time
import pytest
from pytest_bdd import given, when, then, scenarios
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Add the project root to the Python path
sys.path.append(r'C:\Users\dhira\Desktop\Dhiraj HP Laptop\Projects\Selenium_Cucumber')

# Define the path to the feature file (adjust as needed)
scenarios('../features/login.feature')


@pytest.fixture(scope="session")
def driver():
    service = Service('C:\\Users\\dhira\\Documents\\Selenium WebDriver\\chromedriver.exe')
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()


@given('I am on the OrangeHRM login page')
def visit_login_page(driver):
    driver.get("https://opensource-demo.orangehrmlive.com/")
    time.sleep(5)


@when('I enter valid credentials')
def input_userid_password(driver):
    username = driver.find_element(By.NAME, "username")
    password = driver.find_element(By.NAME, "password")
    username.send_keys("Admin")
    password.send_keys("admin123")


@when('I click the login button')
def click_login_button(driver):
    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    login_button.click()
    time.sleep(5)


@then('I should be redirected to the dashboard page')
def dashboard_page(driver):
    expected_url = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
    assert driver.current_url == expected_url, f"Expected URL: {expected_url}, but got: {driver.current_url}"



@then('I log out from the dashboard page')
def logout(driver):
    user_dropdown = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//p[@class='oxd-userdropdown-name']"))
    )
    user_dropdown.click()

    logout_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Logout"))
    )
    logout_button.click()

    time.sleep(5)

    expected_login_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    assert driver.current_url == expected_login_url, f"Expected URL: {expected_login_url}, but got: {driver.current_url}"


@then('I close the browser')
def close_the_browser(driver):
    driver.quit()
