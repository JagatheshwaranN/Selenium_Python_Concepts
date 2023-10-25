import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class TestDropDownSelectedOption(unittest.TestCase):
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

    def test_drop_down_selected_option(self):
        # Navigate to the website
        self.driver.get("https://letcode.in/dropdowns")

        # Find the dropdown element by CSS Selector with ID 'superheros'
        dropdown_element = self.driver.find_element(By.CSS_SELECTOR, "#superheros")

        # Create a Select object for the dropdown element
        select_object = Select(dropdown_element)

        # Select option by value
        select_object.select_by_value("am")

        # Get the first selected dropdown option
        drop_down_selected_option = select_object.first_selected_option

        # Print the first selected dropdown option
        print(drop_down_selected_option.text)

        # Select option by value
        select_object.select_by_value("aq")

        # Get all selected dropdown options
        drop_down_options = select_object.all_selected_options

        # Print all selected dropdown options
        for option in drop_down_options:
            print(option.text)


if __name__ == "__main__":
    unittest.main()
