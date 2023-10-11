import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class TestActionPause(unittest.TestCase):
    # Initialize the driver variable
    driver = None

    @classmethod
    def setUp(cls):
        # Initialize the Chrome WebDriver
        cls.driver = webdriver.Chrome()

        # Maximize the browser window
        cls.driver.maximize_window()

    @classmethod
    def tearDown(cls):
        # Close the driver
        cls.driver.quit()

    def test_action_pause(self):
        # Navigate to the Selenium Mouse Interaction page
        self.driver.get("https://www.selenium.dev/selenium/web/mouse_interaction.html")

        # Create an instance of ActionChains with the driver.
        self.actions = ActionChains(self.driver)

        # Record the current time before performing a series of actions
        start_time = time.time()

        # Move the mouse cursor to the element with the ID "clickable"
        self.actions.move_to_element(self.driver.find_element(By.ID, "clickable"))

        # Pause for 1 second
        self.actions.pause(1)

        # Click and hold the element
        self.actions.click_and_hold()

        # Pause for 1 second
        self.actions.pause(1)
        
        # Send the keys "action pause"
        self.actions.send_keys("action pause")

        # Perform the accumulated actions
        self.actions.perform()

        # Record the current time after performing a series of actions
        end_time = time.time()

        # Calculate the elapsed time by subtracting the start time from the end time
        elapsed_time = end_time - start_time

        # Check that the elapsed time falls within the expected range of 2 to 3 seconds
        self.assertTrue(2 <= elapsed_time <= 3)


if __name__ == "__main__":
    unittest.main()
