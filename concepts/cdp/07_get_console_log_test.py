import unittest
from selenium import webdriver
from selenium.webdriver.common.bidi.console import Console
from selenium.webdriver.common.by import By
from selenium.webdriver.common.log import Log


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
        # Navigate to a specific URL
        self.driver.get('https://www.selenium.dev/selenium/web/bidi/logEntryAdded.html')

        # Establish a bidi connection to the session
        async with self.driver.bidi_connection() as session:
            # Create a log instance using the driver and session
            log = Log(self.driver, session)

            # Add a listener for all console messages
            async with log.add_listener(Console.ALL) as messages:
                # Simulate a click action on an element
                self.driver.find_element(By.ID, 'consoleLog').click()

            # Assert the content of the message received
            assert messages["message"] == "Hello, world!"

            # Add a listener for console error messages
            async with log.add_listener(Console.ERROR) as messages:
                # Simulate a click action on an element
                self.driver.find_element(By.ID, 'consoleError').click()

            # Assert the content of the message received
            assert messages["message"] == "I am console error"


if __name__ == "__main__":
    unittest.main()
