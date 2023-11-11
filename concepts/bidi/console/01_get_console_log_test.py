import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestGetConsoleLog(unittest.TestCase):
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

    async def test_get_console_log(self):
        # Using an asynchronous context manager to establish a bidi connection with the driver
        async with self.driver.bidi_connection() as session:

            # Enable the console log.
            await session.log.enable()

            # Clear the console log.
            await session.log.clear()

            # Navigate to the page with the console log entry.
            self.driver.get("https://www.selenium.dev/selenium/web/bidi/logEntryAdded.html")

            # Click the button to generate the console log entry.
            self.driver.find_element(By.XPATH, "//button[@id='consoleLog']").click()

            # Get the console log entries.
            async for log_entry in session.log.mutation_events():

                # Check if the log entry is a console log entry.
                if log_entry["type"] == "console":
                    console_log_entry = log_entry["entry"]

                    # Assert that the text in the console log entry matches the expected value.
                    self.assertEqual(console_log_entry["text"], "Hello, world!")

                    # Assert that the number of arguments in the console log entry is as expected.
                    self.assertEqual(len(console_log_entry["args"]), 1)

                    # Assert that the type of the console log entry is "console".
                    self.assertEqual(console_log_entry["type"], "console")

                    # Assert that the method of the console log entry is "log".
                    self.assertEqual(console_log_entry["method"], "log")

                    # Assert that the stack trace in the console log entry is not None.
                    self.assertIsNotNone(console_log_entry["stack_trace"])

                    # Break out of the loop.
                    break


if __name__ == "__main__":
    unittest.main()
