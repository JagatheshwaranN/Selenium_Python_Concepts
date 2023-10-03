from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest


class TestTypeInElement(unittest.TestCase):
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

    def test_type_in_element(self):
        # Open the specified URL in Chrome
        self.driver.get("https://accounts.google.com/")

        # Find the input element on the web page by its name attribute
        input_element = self.driver.find_element(By.NAME, "identifier")

        # Type the text "google" into the found input element
        input_element.send_keys("google")

        # Get the value of the "data-initial-value" attribute of the input element
        user_name = input_element.get_attribute("data-initial-value")

        # Check if the value matches the expected value
        self.assertEqual(user_name, "google")


if __name__ == "__main__":
    unittest.main()
