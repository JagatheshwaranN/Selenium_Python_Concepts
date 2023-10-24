import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class TestSelectDropDownSingleOptionByIndex(unittest.TestCase):
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

    def test_select_drop_down_single_option_by_index(self):
        # Navigate to the website
        self.driver.get("https://letcode.in/dropdowns")

        # Find the dropdown element by CSS selector
        drop_down = self.driver.find_element(By.CSS_SELECTOR, "#fruits")

        # Select the option 'Mango' by its value using the Select class
        Select(drop_down).select_by_index(2)

        # Assert whether the dropdown text contains 'Mango'
        assert "Mango" in drop_down.text


if __name__ == "__main__":
    unittest.main()
