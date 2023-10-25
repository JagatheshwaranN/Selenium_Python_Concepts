import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class TestSelectDropDownMultipleOptions(unittest.TestCase):
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

    def test_select_drop_down_multiple_options(self):
        # Navigate to the website
        self.driver.get("https://letcode.in/dropdowns")

        # Find the dropdown element by CSS Selector with ID 'superheros'
        dropdown_element = self.driver.find_element(By.CSS_SELECTOR, "#superheros")

        # Create a Select object for the dropdown element
        select_object = Select(dropdown_element)

        # Check if the dropdown allows multiple selection
        is_multi_select = select_object.is_multiple

        # Print whether the dropdown has multiple selection option
        print(f"Dropdown has Multi Select option : {is_multi_select}")

        # Select multiple options 'am' and 'aq' by their values
        select_object.select_by_value("am")
        select_object.select_by_value("aq")


if __name__ == "__main__":
    unittest.main()
