from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_wait_until_type_1():
    # Initialize the Chrome WebDriver
    driver = webdriver.Chrome()

    try:
        # Maximize the browser window
        driver.maximize_window()

        # Navigate to the login page of the demoQA application
        driver.get("https://demoqa.com/login")

        # Wait until the input element with CSS selector "input[id='username']" is present
        # on the page (up to 5 seconds)
        input_element = WebDriverWait(driver, 5)\
            .until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[id='userName']")))

        # Send keys to the input element
        input_element.send_keys("Admin")

        result = input_element.get_attribute("value")

        assert result == "Admin"

    finally:
        # Close the Chrome browser
        driver.quit()
