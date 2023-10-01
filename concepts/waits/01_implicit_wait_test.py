from selenium import webdriver
from selenium.webdriver.common.by import By


def test_implicit_wait():
    # Initialize the Chrome WebDriver
    driver = webdriver.Chrome()

    try:
        # Maximize the browser window
        driver.maximize_window()

        # Set the implicit wait timeout to 5 seconds
        driver.implicitly_wait(5)

        # Navigate to the specified HTML file
        driver.get("file:///D:/Environment_Collection/Eclipse_Env/Workspace/Selenium_Concepts/"
                   "src/main/resources/supportFiles/DisabledElement.html")

        # Find the input element using CSS selector
        input_element = driver.find_element(By.CSS_SELECTOR, "input[id='myText']")

        # Send keys to the input element
        input_element.send_keys("python")

        # Get the attribute "value" from the input element
        result = input_element.get_attribute("value")

        # Assert that the result matches the expected value
        assert result == "python"

    finally:
        # Close the Chrome browser
        driver.quit()
