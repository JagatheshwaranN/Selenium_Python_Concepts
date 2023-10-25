import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class TestSelectDisabledOption(unittest.TestCase):
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

    def test_select_disabled_option(self):
        # Navigate to the website
        self.driver.get(
            "file:///D:/Environment_Collection/Eclipse_Env/Workspace/Selenium_Concepts"
            "/src/main/resources/supportFiles/disabledSelect.html")

        # Find the select element by name 'single_disabled'
        select_element = Select(self.driver.find_element(By.NAME, "single_disabled"))

        # Use assertRaises to check for the expected exception
        with self.assertRaises(NotImplementedError):
            select_element.select_by_value("disabled")

        # Wait for some time
        time.sleep(3)

        # Asserting that the text of the first selected option in the select_element is "Enabled"
        assert select_element.first_selected_option.text == "Enabled"


if __name__ == "__main__":
    unittest.main()
