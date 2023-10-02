from selenium import webdriver
from selenium.webdriver.common.by import By


def test_page_load_wait():
    # Initialize the Chrome WebDriver
    driver = webdriver.Chrome()

    try:
        # Maximize the browser window
        driver.maximize_window()

        # Set the page load timeout to 10 seconds
        driver.set_page_load_timeout(10)

        # Navigate to the Python official website
        driver.get("https://www.python.org/")

        # Find the python_logo element using CSS selector
        python_logo = driver.find_element(By.CSS_SELECTOR, "div[class='python-logo']")

        # Assert that the python_logo is displayed
        assert python_logo.is_displayed()

    finally:
        # Close the driver
        driver.quit()
