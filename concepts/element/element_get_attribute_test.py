import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestElementGetAttribute(unittest.TestCase):
    # Initialize the driver variable
    driver = None

    @classmethod
    def setUpClass(cls):
        # Initialize the Chrome WebDriver
        cls.driver = webdriver.Chrome()

        # Maximize the browser windows
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        # Close the driver
        cls.driver.quit()

    def test_get_element_attribute(self):
        # Navigate to the inputs page
        self.driver.get("https://www.selenium.dev/selenium/web/inputs.html")

        # Find the element using a CSS selector
        element = self.driver.find_element(By.CSS_SELECTOR, "input[name='no_type']")

        # Get the "value" and "name" attributes of the element
        element_value = element.get_attribute("value")
        element_name = element.get_attribute("name")

        # Assert that the retrieved attributes match the expected values
        self.assertEqual(element_value, "input with no type")
        self.assertEqual(element_name, "no_type")


if __name__ == "__main__":
    unittest.main()
