import unittest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.action_chains import ActionBuilder


class TestActionReset(unittest.TestCase):
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

    def test_action_reset(self):
        # Navigate to the Selenium Mouse Interaction page
        self.driver.get("https://www.selenium.dev/selenium/web/mouse_interaction.html")

        # Create an instance of ActionChains with the driver.
        self.actions = ActionChains(self.driver)

        # Find the element with ID "clickable"
        clickable_element = self.driver.find_element(By.ID, "clickable")

        # Define a sequence of actions: click and hold the element, press and hold the SHIFT key, and send "a" to the
        # element
        self.actions.click_and_hold(clickable_element).key_down(Keys.SHIFT).send_keys("a").perform()

        """
        Alternate option to reset / clear the actions
        
        ActionBuilder(self.driver).clear_actions()
        """

        # Reset the previously defined actions to start fresh with a clean actions chain
        self.actions.reset_actions()

        # Define a new set of actions: send "a" without holding the SHIFT key
        self.actions.send_keys("a").perform()

        # Assertions to check the value of the input field
        input_value = clickable_element.get_attribute("value")

        # Check the first character is 'A'
        self.assertEqual("A", input_value[0])

        # Check the second character is 'a'
        self.assertEqual("a", input_value[1])


if __name__ == "__main__":
    unittest.main()
