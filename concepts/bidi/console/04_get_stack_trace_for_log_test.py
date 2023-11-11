import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestGetStackTraceForLog(unittest.TestCase):
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

    async def test_get_stack_trace_for_log(self):
        # Using an asynchronous context manager to establish a bidi connection with the driver
        async with self.driver.bidi_connection() as session:

            # Enable the JavaScript log.
            await session.log.enable()

            # Clear the JavaScript log.
            await session.log.clear()

            # Navigate to the page with the JavaScript log entry.
            self.driver.get("https://www.selenium.dev/selenium/web/bidi/logEntryAdded.html")

            # Click the button to generate the JavaScript log entry with stack trace.
            self.driver.find_element(By.XPATH, "//button[@id='logWithStacktrace']").click()

            # Get the JavaScript log entries.
            async for log_entry in session.log.mutation_events():

                # Check if the log entry is a JavaScript log entry.
                if log_entry["type"] == "javascript":
                    javascript_log_entry = log_entry["entry"]

                    # Assert that the JavaScript log entry is correct.
                    self.assertIsNotNone(javascript_log_entry["stack_trace"])

                    # Break out of the loop.
                    break

            # Get the stack trace from the JavaScript log entry.
            stack_trace = javascript_log_entry["stack_trace"]

            # Assert that the stack trace is correct.
            self.assertEqual(len(stack_trace["callFrames"]), 3)


if __name__ == "__main__":
    unittest.main()
