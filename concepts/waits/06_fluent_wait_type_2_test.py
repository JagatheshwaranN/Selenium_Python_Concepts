from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException


def test_fluent_wait_type_2():
    # Initialize the Chrome WebDriver
    driver = webdriver.Chrome()

    try:
        # Maximize the browser window
        driver.maximize_window()

        # Navigate to the login page of the nopCommerce admin demo
        driver.get("https://admin-demo.nopcommerce.com/login")

        # Create a WebDriverWait instance for fluent waiting
        wait = WebDriverWait(driver, timeout=10, poll_frequency=2, ignored_exceptions=[NoSuchElementException])

        # Define the locator for the login element using CSS selector
        login_element_locator = (By.CSS_SELECTOR, ".button-1.login-button")

        # Use WebDriverWait to locate the element with fluent wait conditions
        is_login_element_displayed = wait.until(
            # Lambda function that checks if the login element is displayed
            lambda driver_instance: driver.find_element(*login_element_locator).is_displayed()
        )

        # Check if the login element is displayed
        if is_login_element_displayed:
            # Find the login element again using By.CSS_SELECTOR
            login_element = driver.find_element(By.CSS_SELECTOR, ".button-1.login-button")

            # Click the login element
            login_element.click()

        # Get the text of the heading element on the dashboard page
        result = driver.find_element(By.XPATH, "//div[@class='content-header']//h1").text

        # Assert that the result matches the expected value
        assert result == "Dashboard"

    finally:
        # Close the browser
        driver.quit()
