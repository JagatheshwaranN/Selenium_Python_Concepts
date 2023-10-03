import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestElementCSSValue(unittest.TestCase):
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

    def test_get_element_css_values(self):
        # Navigate to the inputs page
        self.driver.get("https://www.selenium.dev/selenium/web/inputs.html")

        # Find the element using a CSS selector
        element = self.driver.find_element(By.CSS_SELECTOR, "input[name='color_input']")

        # Get the CSS values for color and background-color properties
        element_color = element.value_of_css_property("color")
        element_bg_color = element.value_of_css_property("background-color")

        # Assert that the retrieved CSS values match the expected values
        self.assertEqual(element_color, "rgba(0, 0, 0, 1)")
        self.assertEqual(element_bg_color, "rgba(240, 240, 240, 1)")


if __name__ == "__main__":
    unittest.main()
