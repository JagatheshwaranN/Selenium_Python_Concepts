import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestGetJavaScriptLog(unittest.TestCase):
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

    async def test_get_javascript_log(self):
        # Using an asynchronous context manager to establish a bidi connection with the driver
        async with self.driver.bidi_connection() as session:

            # Enable the JavaScript log.
            await session.log.enable()

            # Clear the JavaScript log.
            await session.log.clear()

            # Navigate to the page with the JavaScript log entry.
            self.driver.get("https://www.selenium.dev/selenium/web/bidi/logEntryAdded.html")

            # Click the button to generate the JavaScript log entry.
            self.driver.find_element(By.XPATH, "//button[@id='jsException']").click()

            # Get the JavaScript log entries.
            async for log_entry in session.log.mutation_events():

                # Check if the log entry is a JavaScript log entry.
                if log_entry["type"] == "javascript":
                    javascript_log_entry = log_entry["entry"]

                    # Assert that the text in the JavaScript log entry matches the expected value.
                    self.assertEqual(javascript_log_entry["text"], "Error: Not working")

                    # Assert that the type of the JavaScript log entry is "javascript".
                    self.assertEqual(javascript_log_entry["type"], "javascript")

                    # Assert that the log level of the JavaScript log entry is "SEVERE".
                    self.assertEqual(javascript_log_entry["level"], "SEVERE")

                    # Break out of the loop.
                    break


if __name__ == "__main__":
    unittest.main()
