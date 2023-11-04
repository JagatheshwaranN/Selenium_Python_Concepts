import unittest
from selenium import webdriver


class TestNavigateToPage(unittest.TestCase):
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

    def test_navigate_to_page(self):
        # Navigate to the Google website
        self.driver.get("https://www.google.com/")

        # Get the JavaScript executor for the driver
        js_executor = self.driver.execute_script

        # Change the current window location to 'https://www.selenium.dev/' using JavaScript executor
        js_executor("window.location='https://www.selenium.dev/'")

        # Assert whether the current page title matches the expected title 'Selenium'
        self.assertEqual(self.driver.title, "Selenium")


if __name__ == "__main__":
    unittest.main()
