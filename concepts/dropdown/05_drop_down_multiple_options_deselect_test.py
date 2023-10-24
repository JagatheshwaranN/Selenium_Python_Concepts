import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class TestDeselectDropDownMultipleOptions(unittest.TestCase):
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

    def test_deselect_drop_down_multiple_options(self):
        # Navigate to the website
        self.driver.get("https://letcode.in/dropdowns")

        # Find the dropdown element by CSS selector
        dropdown_element = self.driver.find_element(By.CSS_SELECTOR, "#superheros")

        # Find the dropdown element by CSS selector
        select_object = Select(dropdown_element)

        # Check if the dropdown allows multiple selection
        is_multi_select = select_object.is_multiple

        # Print whether the dropdown has multiple selection option
        print(f"Dropdown has Multi Select option : {is_multi_select}")

        # Select option by index (index 0)
        select_object.select_by_index(0)

        # Select option by value ("aq")
        select_object.select_by_value("aq")

        # Select option by visible text ("The Avengers")
        select_object.select_by_visible_text("The Avengers")

        # Deselect option by index (index 0)
        select_object.deselect_by_index(0)

        # Deselect option by value ("aq")
        select_object.deselect_by_value("aq")

        # Deselect option by visible text ("The Avengers")
        select_object.deselect_by_visible_text("The Avengers")


if __name__ == "__main__":
    unittest.main()
