import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestClearElementText(unittest.TestCase):
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

    def test_clear_element_text(self):
        # Navigate to a local HTML file using the 'file://' protocol
        self.driver.get("file:///D:/Environment_Collection/Eclipse_Env/"
                        "Workspace/Selenium_Concepts/src/main/resources/supportFiles/DisabledElement.html")

        # Find the input element by its ID and assign it to the variable 'input_element'
        input_element = self.driver.find_element(By.ID, "myText")

        # Enter the text "Python" into the input field
        input_element.send_keys("Python")

        # Assign the 'execute_script' method of the driver to the variable 'js_executor'
        js_executor = self.driver.execute_script

        # Using JavaScript to set the value of the input element to an empty string
        js_executor("arguments[0].value='';", input_element)

        # Get the value of the input element
        result = input_element.get_attribute("value")

        # Check if the result matches the expected value
        assert result == ""


if __name__ == "__main__":
    unittest.main()
