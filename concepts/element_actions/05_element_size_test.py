import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestElementSize(unittest.TestCase):
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

    def test_get_element_size(self):
        # Navigate to the inputs page
        self.driver.get("https://www.selenium.dev/selenium/web/inputs.html")

        # Find the element using a CSS selector
        element = self.driver.find_element(By.CSS_SELECTOR, "input[name='no_type']")

        # Get the element's height and width
        element_height = element.size['height']
        element_width = element.size['width']

        # Get the element's rectangle and location
        rectangle = element.rect
        point = element.location

        # Assert that the retrieved sizes and coordinates match the expected values
        self.assertEqual(element_height, 21)
        self.assertEqual(element_width, 177)
        self.assertEqual(rectangle['height'], 21)
        self.assertEqual(rectangle['width'], 177)
        self.assertEqual(rectangle['x'], 8)
        self.assertEqual(rectangle['y'], 66.4375)
        self.assertEqual(point['x'], 8)
        self.assertEqual(point['y'], 66)


if __name__ == "__main__":
    unittest.main()
