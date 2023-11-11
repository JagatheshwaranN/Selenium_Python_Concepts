import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.log import Log


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
        # Navigate to a specific URL
        self.driver.get('https://www.selenium.dev/selenium/web/bidi/logEntryAdded.html')

        # Establish a bidi connection to the session
        async with self.driver.bidi_connection() as session:

            # Create a log instance using the driver and session
            log = Log(self.driver, session)

            # Establish a bidi connection to the session and add a JavaScript error listener
            async with log.add_js_error_listener() as messages:

                # Simulate a click action on an element that may trigger a JavaScript error
                self.driver.find_element(By.XPATH, "//button[@id='logWithStacktrace']").click()

            # Iterate over collected messages from the JavaScript error listener
            for log_entry in messages:

                # Check if the log entry corresponds to a JavaScript exception
                if log_entry["type"] == "javascript_exception":

                    # Extract the stack trace information from the log entry
                    stack_trace = log_entry["stack_trace"]

                    # Assert that the number of call frames in the stack trace is 3
                    self.assertEqual(len(stack_trace["callFrames"]), 3)


if __name__ == "__main__":
    unittest.main()
