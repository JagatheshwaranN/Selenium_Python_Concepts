from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_wait_until_type_2():
    # Initialize the Chrome WebDriver
    driver = webdriver.Chrome()

    try:
        # Maximize the browser window
        driver.maximize_window()

        # Navigate to the login page of the nopCommerce admin demo
        driver.get("https://admin-demo.nopcommerce.com/login")

        # Wait until the login button becomes clickable (with a timeout of 5 seconds)
        login_element = WebDriverWait(driver, 5, 1.5)\
            .until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".button-1.login-button")))

        # Click the login element
        login_element.click()

        # Get the text of the heading element on the dashboard page
        result = driver.find_element(By.XPATH, "//div[@class='content-header']//h1").text

        assert result == "Dashboard"

    finally:
        # Close the Chrome browser
        driver.quit()
