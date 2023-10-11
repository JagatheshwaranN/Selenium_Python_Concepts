import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


class TestMouseDragAndDrop(unittest.TestCase):
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

    def test_mouse_drag_and_drop(self):
        # Navigate to the Selenium Mouse Interaction page
        self.driver.get("https://www.selenium.dev/selenium/web/mouse_interaction.html")

        # Create an instance of ActionChains with the driver.
        self.actions = ActionChains(self.driver)

        # Find the draggable element on the webpage by its 'id' attribute
        draggable_element = self.driver.find_element(By.ID, "draggable")

        # Find the droppable element on the webpage by its 'id' attribute
        droppable_element = self.driver.find_element(By.ID, "droppable")

        # Using ActionChains object 'actions' and perform the drag-and-drop action from 'draggable_element' to
        # 'droppable_element'
        self.actions.drag_and_drop(draggable_element, droppable_element).perform()

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
