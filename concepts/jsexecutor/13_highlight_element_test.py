import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestHighLightElement(unittest.TestCase):
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

    def test_highlight_element(self):
        # Navigate to a local HTML file using the 'file://' protocol
        self.driver.get("file:///D:/Environment_Collection/Eclipse_Env/"
                        "Workspace/Selenium_Concepts/src/main/resources/supportFiles/DisabledElement.html")

        # Find the input element by its ID and assign it to the variable 'input_element'
        input_element = self.driver.find_element(By.ID, "myText")

        # Assign the 'execute_script' method of the driver to the variable 'js_executor'
        js_executor = self.driver.execute_script

        # Executing JavaScript to set the style of the element
        js_executor("arguments[0].setAttribute('style', 'background: yellow; border: 2px solid green;')", input_element)

        # Getting the CSS property value for the background color
        result = input_element.value_of_css_property("background")

        # Verifying if the CSS property value matches the highlighted color
        self.assertTrue("rgb(255, 255, 0)" in result)


if __name__ == '__main__':
    unittest.main()
