import unittest
from selenium import webdriver


class TestWindowSize(unittest.TestCase):
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

    def test_get_window_size(self):
        # Navigate to the Google website
        self.driver.get("https://www.google.com/")

        # Get the JavaScript executor for the driver
        js_executor = self.driver.execute_script

        # Get the height of the window using JavaScript executor
        height = js_executor("return window.innerHeight;")

        # Get the width of the window using JavaScript executor
        width = js_executor("return window.innerWidth;")

        # Assert whether the height of the window matches the expected value
        self.assertEqual(height, 607)

        # Assert whether the width of the window matches the expected value
        self.assertEqual(width, 1366)


if __name__ == "__main__":
    unittest.main()
