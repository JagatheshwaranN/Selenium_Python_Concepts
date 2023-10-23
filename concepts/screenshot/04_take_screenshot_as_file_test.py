import os.path
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestTakeScreenshotAsFile(unittest.TestCase):
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

    def test_take_screenshot_as_file(self):
        # Navigate to the website
        self.driver.get("http://www.example.com")

        # Take a screenshot of the current page and save it to a file named "file.png"
        self.driver.get_screenshot_as_file("file.png")

        # Sleep for 2 seconds to ensure the screenshot is taken
        time.sleep(2)

        # Check if the screenshot file "file.png" exists in the current directory
        assert os.path.exists("file.png")


if __name__ == "__main__":
    unittest.main()
