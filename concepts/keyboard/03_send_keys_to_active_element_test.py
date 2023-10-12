import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class TestSendKeys(unittest.TestCase):
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

    def test_send_keys_to_active_element(self):
        # Navigate to the Selenium Text Input page
        self.driver.get("https://www.selenium.dev/selenium/web/single_text_input.html")

        # Create an ActionChains object for performing actions on the driver
        self.actions = ActionChains(self.driver)

        # Simulate typing "Chrome" into the active element
        self.actions.send_keys("Chrome").perform()

        # Find the input element by its ID
        input_element = self.driver.find_element(By.ID, "textInput")

        # Get the current value of the input element
        input_element_value = input_element.get_attribute("value")

        # Assert that the input element's value is equal to "Chrome"
        self.assertEqual(input_element_value, "Chrome")


if __name__ == "__main__":
    unittest.main()

