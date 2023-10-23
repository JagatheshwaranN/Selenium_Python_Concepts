import os.path
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestElementScreenShot(unittest.TestCase):
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

    def test_take_element_screenshot(self):
        # Navigate to the website
        self.driver.get("http://www.example.com")

        # Find the header element
        header_element = self.driver.find_element(By.TAG_NAME, "h1")

        # Take a screenshot of the header element
        header_element.screenshot("element_screen.png")

        # Sleep for 2 seconds to ensure the screenshot is taken
        time.sleep(2)

        # Check if the screenshot file "screenshot.png" exists in the current directory
        assert os.path.exists("element_screen.png")


if __name__ == "__main__":
    unittest.main()
