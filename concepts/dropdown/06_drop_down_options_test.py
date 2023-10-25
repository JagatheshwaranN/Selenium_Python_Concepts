import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class TestDropDownOptions(unittest.TestCase):
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

    def test_drop_down_options(self):
        # Navigate to the website
        self.driver.get("https://letcode.in/dropdowns")

        # Find the dropdown element by CSS selector
        dropdown_element = self.driver.find_element(By.CSS_SELECTOR, "#superheros")

        # Get all dropdown options
        drop_down_options = Select(dropdown_element).options

        # Print all the dropdown options
        for option in drop_down_options:
            print(option.text)


if __name__ == "__main__":
    unittest.main()
