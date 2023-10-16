import sys
import unittest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class TestCopyAndPaste(unittest.TestCase):
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

    def test_copy_paste(self):
        # Navigate to the Selenium Text Input page
        self.driver.get("https://www.selenium.dev/selenium/web/single_text_input.html")

        # Create an ActionChains object for performing actions on the driver
        self.actions = ActionChains(self.driver)

        # Find the input element by its ID
        input_element = self.driver.find_element(By.ID, "textInput")

        # Determine the appropriate command/control key based on the platform
        cmd_ctrl = Keys.COMMAND if sys.platform == 'darwin' else Keys.CONTROL

        # Simulate key presses and other actions using ActionChains
        # Enters the text "Automation!" into the input element
        # Presses the left arrow key to move the cursor one position to the left
        # Holds down the Shift key
        # Presses the up arrow key
        # Releases the Shift key
        # Holds down the Control key
        # Enters the text "xvv"
        # Releases the Control key
        # Performs the sequence of actions on the input element
        self.actions.send_keys_to_element(input_element, "Automation!") \
            .send_keys(Keys.ARROW_LEFT) \
            .key_down(Keys.SHIFT) \
            .send_keys(Keys.ARROW_UP) \
            .key_up(Keys.SHIFT) \
            .key_down(cmd_ctrl) \
            .send_keys("xvv") \
            .key_up(cmd_ctrl) \
            .perform()

        # Get the current value of the input element
        input_element_value = input_element.get_attribute("value")

        # Assert that the input element's value is equal to "Python"
        self.assertEqual(input_element_value, "AutomationAutomation!")


if __name__ == "__main__":
    unittest.main()
