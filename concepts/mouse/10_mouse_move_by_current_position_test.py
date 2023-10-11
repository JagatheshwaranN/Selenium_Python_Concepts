import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


class TestMouseMoveByCurrentPosition(unittest.TestCase):
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

    def test_mouse_move_by_current_position(self):
        # Navigate to the Selenium Mouse Interaction page
        self.driver.get("https://www.selenium.dev/selenium/web/mouse_interaction.html")

        # Initialize an ActionBuilder with the WebDriver instance to perform actions.
        self.actions = ActionBuilder(self.driver)

        # Use the pointer_action to create a move_to_location action.
        # Move the mouse cursor to the specified location (8, 12) on the viewport.
        self.actions.pointer_action.move_to_location(8, 12)

        # Perform the actions.
        self.actions.perform()

        # Create an instance of ActionChains with the driver.
        self.actions_chains = ActionChains(self.driver)

        # Move the mouse cursor by an offset of 13 pixels to the right (X) and 15 pixels down (Y).
        self.actions_chains.move_by_offset(13, 15).perform()

        # Find the element with ID "absolute-location" and get its text content.
        result = self.driver.find_element(By.ID, "absolute-location").text

        # Split the text content by ", " to extract the X and Y coordinate values.
        result_values = [int(val.strip()) for val in result.split(",")]

        # Assert that the absolute difference between the X coordinate value (result_values[0]) and 8 is less than 2.
        self.assertTrue(abs(result_values[0] - 8 - 13) < 2)

        # Assert that the absolute difference between the Y coordinate value (result_values[1]) and 12 is less than 2.
        self.assertTrue(abs(result_values[1] - 12 - 15) < 2)

        # Wait for a moment - For demo purpose
        time.sleep(5)


if __name__ == "__main__":
    unittest.main()
