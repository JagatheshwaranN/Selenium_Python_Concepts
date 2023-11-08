import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.log import Log


class TestGetJavaScriptError(unittest.TestCase):
    # Initialize the driver variable
    driver = None

    @classmethod
    def setUpClass(cls):
        # Initialize the Chrome WebDriver
        cls.driver = webdriver.Chrome()

        # Maximize the browser window
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        # Close the driver
        cls.driver.quit()

    async def test_get_javascript_error(self):
        # Navigate to a specific URL
        self.driver.get('https://www.selenium.dev/selenium/web/bidi/logEntryAdded.html')

        # Establish a bidi connection to the session
        async with self.driver.bidi_connection() as session:
            # Create a log instance using the driver and session
            log = Log(self.driver, session)

            # Using an asynchronous context manager to listen for JavaScript errors
            async with log.add_js_error_listener() as messages:
                # Simulate a click action on an element that may trigger a JavaScript error
                self.driver.find_element(By.ID, 'jsException').click()

            # Assert that the expected error message is present in the collected exception details
            assert "Error: Not working" in messages.exception_details.exception.description


if __name__ == "__main__":
    unittest.main()
