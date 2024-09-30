from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@given('I am on the OrangeHRM login page')
def step_impl(context):
    service = Service('C:\\Users\\dhira\\Documents\\Selenium WebDriver\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe')
    context.driver = webdriver.Chrome(service=service)
    context.driver.get("https://opensource-demo.orangehrmlive.com/")

@when('I enter valid credentials')
def step_impl(context):
    WebDriverWait(context.driver, 30).until(
        EC.presence_of_element_located((By.NAME, "username"))
    )
    context.driver.find_element(By.NAME, "username").send_keys("Admin")
    context.driver.find_element(By.NAME, "password").send_keys("admin123")

@when('I click the login button')
def step_impl(context):
    WebDriverWait(context.driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
    ).click()

@then('I should be redirected to the dashboard page')
def step_impl(context):
    time.sleep(20)  # Wait for the page to load
    actual_url = context.driver.current_url
    print(f"Actual URL after login: {actual_url}")  # Debugging print statement

    # Capture a screenshot for debugging purposes
    context.driver.save_screenshot("screenshot_after_login.png")

    expected_url = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
    assert actual_url == expected_url, f"Expected URL: {expected_url}, but got: {actual_url}"

    # Print the page source for further debugging
    print(context.driver.page_source)

    context.driver.quit()