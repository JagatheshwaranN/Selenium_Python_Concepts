import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class TestMouseDragAndDropByOffset(unittest.TestCase):
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

    def test_mouse_drag_drop_by_offset(self):
        # Navigate to the Selenium Mouse Interaction page
        self.driver.get("https://www.selenium.dev/selenium/web/mouse_interaction.html")

        # Create an instance of ActionChains with the driver.
        self.actions = ActionChains(self.driver)

        # Find the draggable element on the webpage by its 'id' attribute
        draggable_element = self.driver.find_element(By.ID, "draggable")

        # Find the droppable element on the webpage by its 'id' attribute
        droppable_element = self.driver.find_element(By.ID, "droppable")

        """
        Alternate option to get the element position
        
        # Get the starting position (Location) of the draggable element
        start = draggable_element.location

        # Get the ending position (Location) of the droppable element
        finish = droppable_element.location
        """

        # Get the starting position (Rectangle) of the draggable element
        start = draggable_element.rect

        # Get the ending position (Rectangle) of the droppable element
        finish = droppable_element.rect

        # Calculate the X and Y offset for drag-and-drop
        x_offset = finish['x'] - start['x']
        y_offset = finish['y'] - start['y']

        # Perform drag-and-drop by offset using the 'actions' object
        self.actions.drag_and_drop_by_offset(draggable_element, x_offset, y_offset).perform()

        # Find the result element using an XPath expression, which contains the dropped status
        result_element = self.driver.find_element(By.XPATH, "//strong[@id='drop-status']")

        # Get the text from the 'result_element' to check if the expected "dropped" status is displayed
        result_text = result_element.text

        # Use the 'assertEqual' method to verify that the 'result_text' matches the expected text "dropped"
        self.assertEqual(result_text, "dropped")

        # Wait for a moment - For demo purpose
        time.sleep(3)


if __name__ == "__main__":
    unittest.main()
