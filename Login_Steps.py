
#From CMD window, run the Tests
#Ensure your virtual environment is activated:
#cd "C:\Users\dhira\Desktop\Dhiraj HP Laptop\Projects\Selenium_Cucumber"
#venv\Scripts\activate
#Run the behave command:
#behave

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


@given('I am on the OrangeHRM login page')
def step_impl(context):
    service = Service(
        'C:\\Users\\dhira\\Documents\\Selenium WebDriver\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe')
    context.driver = webdriver.Chrome(service=service)
    context.driver.get("https://opensource-demo.orangehrmlive.com/")
    print("Page title:", context.driver.title)


@when('I enter valid credentials')
def step_impl(context):
    try:
        # Wait for the username field
        username_field = WebDriverWait(context.driver, 30).until(
            EC.presence_of_element_located((By.NAME, "username"))
        )
        username_field.send_keys("Admin")

        # Find and fill the password field
        password_field = context.driver.find_element(By.NAME, "password")
        password_field.send_keys("admin123")

        print("Credentials entered successfully")
    except Exception as e:
        print("Error while entering credentials:", str(e))
        context.driver.save_screenshot("error_screenshot.png")
        raise e


@when('I click the login button')
def step_impl(context):
    try:
        login_button = context.driver.find_element(By.XPATH, "//button[@type='submit']")
        login_button.click()
        WebDriverWait(context.driver, 30)
        print("Login button clicked")
    except Exception as e:
        print("Error while clicking login button:", str(e))
        context.driver.save_screenshot("error_screenshot_login.png")
        raise e


@then('I should be redirected to the dashboard page')
def step_impl(context):
    try:
        WebDriverWait(context.driver, 30).until(
            EC.url_contains("/dashboard")
        )
        print("Current URL:", context.driver.current_url)
        assert "dashboard" in context.driver.current_url
    except Exception as e:
        print("Error while checking dashboard:", str(e))
        context.driver.save_screenshot("error_screenshot_dashboard.png")
        raise e
    finally:
       context.driver.quit()