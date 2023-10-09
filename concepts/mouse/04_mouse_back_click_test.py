import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.mouse_button import MouseButton


class TestMouseBackClick(unittest.TestCase):
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

    def test_mouse_back_click(self):
        # Navigate to the Selenium Mouse Interaction page
        self.driver.get("https://www.selenium.dev/selenium/web/mouse_interaction.html")

        # Create an instance of ActionChains
        self.actions = ActionChains(self.driver)

        # Create an instance of ActionBuilder
        self.action_builder = ActionBuilder(self.driver)

        # Find an element by its ID with the value "click"
        element = self.driver.find_element(By.ID, "click")

        # Perform a click on the identified clickable element.
        element.click()

        # Assert that the title of the page is "We Arrive Here"
        self.assertEqual(self.driver.title, "We Arrive Here")

        # Wait for a moment
        self.wait_for_some_time(3)

        # Perform a mouse button down action on the BACK button
        self.action_builder.pointer_action.pointer_down(MouseButton.BACK)

        # Perform a mouse button up action on the BACK button
        self.action_builder.pointer_action.pointer_up(MouseButton.BACK)

        # Perform the actions in the action builder
        self.action_builder.perform()

        # Wait for a moment
        self.wait_for_some_time(3)

        # Assert that the page title has changed back
        self.assertEqual(self.driver.title, "BasicMouseInterfaceTest")

    def wait_for_some_time(self, seconds):
        # Helper method to wait for a specified number of seconds
        import time
        time.sleep(seconds)


if __name__ == "__main__":
    unittest.main()
