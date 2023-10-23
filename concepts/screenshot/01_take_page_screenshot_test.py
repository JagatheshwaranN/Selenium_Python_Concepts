import os.path
import time
import unittest
from selenium import webdriver


class TestTakePageScreenshot(unittest.TestCase):
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

    def test_take_page_screenshot(self):
        # Navigate to the website
        self.driver.get("http://www.example.com")

        # Take a screenshot
        self.driver.save_screenshot("page_screen.png")

        # Sleep for 2 seconds to ensure the screenshot is taken
        time.sleep(2)

        # Check if the screenshot file "screenshot.png" exists in the current directory
        assert os.path.exists("screenshot.png")


if __name__ == "__main__":
    unittest.main()
