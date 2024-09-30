# pytest -v login_withoutBDD.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up the Chrome driver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    # Step 1: Navigate to the OrangeHRM login page
    driver.get("https://opensource-demo.orangehrmlive.com/")
    driver.maximize_window()
    time.sleep(5)

    # Step 2: Enter valid credentials
    username = driver.find_element(By.NAME, "username")
    password = driver.find_element(By.NAME, "password")
    username.send_keys("Admin")
    password.send_keys("admin123")

    # Step 3: Click the login button
    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    login_button.click()

    # Wait for the dashboard to load
    time.sleep(5)  # This is just a simple wait. Consider using WebDriverWait for a more robust solution.

    # Step 4: Verify redirection to the dashboard
    expected_url = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
    assert driver.current_url == expected_url, f"Expected URL: {expected_url}, but got: {driver.current_url}"

    # Step 5: Logout from the dashboard page
    # WebDriverWait: Added to wait for the user dropdown and logout button to be clickable.
    # Dynamic Handling: The EC.element_to_be_clickable condition checks if the element is clickable.
    user_dropdown = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//p[@class='oxd-userdropdown-name']"))
    )
    user_dropdown.click()

    logout_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Logout"))
    )
    logout_button.click()

    # Wait for the login page to load
    time.sleep(5)  # This is just a simple wait. Consider using WebDriverWait for a more robust solution.

    # Verify redirection to the login page
    expected_login_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    assert driver.current_url == expected_login_url, f"Expected URL: {expected_login_url}, but got: {driver.current_url}"

finally:
    # Close the browser
    driver.quit()