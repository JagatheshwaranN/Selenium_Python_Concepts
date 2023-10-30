import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestEnableElement(unittest.TestCase):
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

    def test_enable_element(self):
        # Navigate to a local HTML file using the 'file://' protocol
        self.driver.get("file:///D:/Environment_Collection/Eclipse_Env/"
                        "Workspace/Selenium_Concepts/src/main/resources/supportFiles/DisabledElement.html")

        # Find the input element by its ID and assign it to the variable 'input_element'
        input_element = self.driver.find_element(By.ID, "myText")

        # Enter the text "Python" into the input field
        input_element.send_keys("Python")

        # Locate and click the button element using the XPath expression
        self.driver.find_element(By.XPATH, "//button").click()

        # Assign the 'execute_script' method of the driver to the variable 'js_executor'
        js_executor = self.driver.execute_script

        # Execute a JavaScript script to remove the 'disabled' attribute from the input element
        js_executor("arguments[0].removeAttribute('disabled');", input_element)

        # Retrieve the value of the input field when it's enabled and assign it to the variable
        # 'get_text_when_input_enabled'
        get_text_when_input_enabled = input_element.get_attribute("value")

        # Verify that the retrieved text matches the expected text "Python" using the
        # 'assertEqual' method
        self.assertEqual(get_text_when_input_enabled, "Python")


if __name__ == "__main__":
    unittest.main()
