import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class TestKeyUp(unittest.TestCase):
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

    def test_key_up(self):
        # Navigate to the Selenium Text Input page
        self.driver.get("https://www.selenium.dev/selenium/web/single_text_input.html")

        # Create an ActionChains object for performing actions on the driver
        self.actions = ActionChains(self.driver)

        # Simulate the key-down action by holding the SHIFT key and typing "app"
        self.actions.key_down(Keys.SHIFT).send_keys("app")

        # Simulate the key-up action by releasing the SHIFT key and typing "url"
        self.actions.key_up(Keys.SHIFT).send_keys("url")

        # Perform the series of key actions
        self.actions.perform()

        # Find the input element by its ID
        input_element = self.driver.find_element(By.ID, "textInput")

        # Get the current value of the input element
        input_element_value = input_element.get_attribute("value")

        # Assert that the input element's value is equal to "APPurl"
        self.assertEqual(input_element_value, "APPurl")


if __name__ == "__main__":
    unittest.main()
