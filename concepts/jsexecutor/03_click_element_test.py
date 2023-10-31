import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestClickElement(unittest.TestCase):
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

    def test_click_element(self):
        # Navigate to a local HTML file using the 'file://' protocol
        self.driver.get("file:///D:/Environment_Collection/Eclipse_Env/"
                        "Workspace/Selenium_Concepts/src/main/resources/supportFiles/DisabledElement.html")

        # Find the input element by its ID and assign it to the variable 'input_element'
        input_element = self.driver.find_element(By.ID, "myText")

        # Enter the text "Python" into the input field
        input_element.send_keys("Python")

        # Locate the button element using the XPath expression
        button = self.driver.find_element(By.XPATH, "//button")

        # Assign the 'execute_script' method of the driver to the variable 'js_executor'
        js_executor = self.driver.execute_script

        # Use JavaScript executor to set the value of the input element
        js_executor("arguments[0].click()", button)

        # Checks if the 'disabled' attribute is present for the input element
        flag = input_element.get_attribute("disabled") is not None

        # Assertion to confirm that the flag is set to True
        assert flag is True


if __name__ == "__main__":
    unittest.main()
