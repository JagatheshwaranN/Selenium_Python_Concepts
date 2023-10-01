from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_wait_until_type_3():
    # Initialize the Chrome WebDriver
    driver = webdriver.Chrome()

    try:
        # Maximize the browser window
        driver.maximize_window()

        # Navigate to the login page of the nopCommerce admin demo
        driver.get("https://admin-demo.nopcommerce.com/login")

        # Create WebDriverWait with custom conditions
        wait = WebDriverWait(driver, 10, poll_frequency=2)

        # Wait until the element is present using custom condition
        login_element = wait\
            .until(EC.presence_of_element_located((By.CSS_SELECTOR, ".button-1.login-button")))

        # Click the login element
        login_element.click()

        # Get the text of the heading element on the dashboard page
        result = driver.find_element(By.XPATH, "//div[@class='content-header']//h1").text

        # Assert that the result matches the expected value
        assert result == "Dashboard"

    finally:
        # Close the Chrome browser
        driver.quit()
