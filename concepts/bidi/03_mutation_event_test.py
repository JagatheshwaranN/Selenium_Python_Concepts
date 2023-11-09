import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.log import Log


class TestMutationEvent(unittest.TestCase):
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

    async def test_mutation_event(self):
        # Using an asynchronous context manager to establish a bidi connection with the driver
        async with self.driver.bidi_connection() as session:

            # Create a log instance using the driver and session
            log = Log(self.driver, session)

        # Using an asynchronous context manager to listen for mutation events
        async with log.mutation_events() as event:

            # Navigate to a specific URL
            self.driver.get("https://www.selenium.dev/selenium/web/dynamic.html")

            # Simulate a click action on an element
            self.driver.find_element(By.ID, "reveal").click()

        # Assert that the expected element is present in the collected mutation events
        assert event["element"] == self.driver.find_element(By.ID, "revealed")
        assert event["attribute_name"] == "style"
        assert event["current_value"] == ""
        assert event["old_value"] == "display:none;"


if __name__ == "__main__":
    unittest.main()

