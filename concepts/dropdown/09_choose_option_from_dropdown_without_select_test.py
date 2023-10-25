import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestDropdownWithoutSelectClass(unittest.TestCase):
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

    def test_choose_option_from_dropdown(self):
        # Navigate to the website
        self.driver.get(
            "file:///D:/Environment_Collection/Eclipse_Env/Workspace/"
            "Selenium_Concepts/src/main/resources/supportFiles/Dropdown.html")

        # Find the dropdown element by XPath
        drop_down = self.driver.find_element(By.XPATH, "//div[@class='select-selected']")

        # Click the dropdown
        drop_down.click()

        # Find all the dropdown options by XPath
        drop_down_options = self.driver.find_elements(By.XPATH, "//ul[@class='select-items']//li")

        # Initialize a flag variable as False
        flag = False

        # Iterate through each option and check if the text matches "Google Chrome"
        for option in drop_down_options:
            if option.text.lower() == "google chrome":
                # Set the flag to True if the option is found and click it
                flag = True
                option.click()
                break

        # Print a message if the option is not found in the dropdown list
        if not flag:
            print("The option is not in the dropdown list")

        # Find the element with the class name "select-selected" and assign it to selected_option
        selected_option = self.driver.find_element(By.CLASS_NAME, "select-selected")

        # Assert that the text of the selected_option is "Google Chrome"
        assert selected_option.text == "Google Chrome"


if __name__ == "__main__":
    unittest.main()
