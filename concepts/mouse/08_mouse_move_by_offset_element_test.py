import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class TestMouseMoveToElementByOffset(unittest.TestCase):
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

    def test_mouse_move_by_offset_element(self):
        # Navigate to the Selenium Mouse Interaction page
        self.driver.get("https://www.selenium.dev/selenium/web/mouse_interaction.html")

        # Create an instance of ActionChains
        self.actions = ActionChains(self.driver)

        # Move the mouse pointer to a specific element with an offset
        # - The element is located using its 'ID' attribute with the value "mouse-tracker".
        # - The horizontal offset is set to 20 pixels (positive value), which moves the pointer to the right.
        # - The vertical offset is set to 0 pixels (no vertical movement).
        # - The 'perform()' method executes the mouse move action.
        self.actions.move_to_element_with_offset(self.driver.find_element(By.ID, "mouse-tracker"), 20, 0).perform()

        # Find the result element displaying the absolute location
        result = self.driver.find_element(By.XPATH, "//span[@id='absolute-location']")

        # Get the text content of the located result element
        result_text = result.text

        # Use the `assertEqual` method to check if the text matches the expected value
        self.assertEqual(result_text, "139, 586")


if __name__ == "__main__":
    unittest.main()
