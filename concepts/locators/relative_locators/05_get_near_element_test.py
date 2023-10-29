import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import relative_locator


class TestGetNearElement(unittest.TestCase):
    # Initialize the driver variable
    driver = None

    @classmethod
    def setUpClass(cls):
        # Initialize the Chrome WebDriver
        cls.driver = webdriver.Chrome()

        # Maximize the browser window
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        # Close the driver
        cls.driver.quit()

    def test_get_near_element(self):
        # Open the Google website
        self.driver.get("https://www.google.com/")

        # Find the input element near the element with the name "btnI"
        button_value = self.driver.find_element(
            relative_locator.with_tag_name("input").near({By.NAME: "btnI"})).get_attribute("value")

        # Assert that the value of the found input element is "Google Search"
        self.assertEqual(button_value, "Google Search")


if __name__ == "__main__":
    unittest.main()

