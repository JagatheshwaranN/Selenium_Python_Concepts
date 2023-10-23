import base64
import os.path
import time
import unittest
from selenium import webdriver


class TestTakeScreenshotAsBase64(unittest.TestCase):
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

    def test_take_screenshot_as_base64(self):
        # Navigate to the website
        self.driver.get("http://www.example.com")

        # Capture the screenshot of the current page as a base64 encoded format
        image_base64 = self.driver.get_screenshot_as_base64()

        # Write the base64 encoded content as bytes to a file named 'base64.png'
        with open("base64.png", "wb") as file:
            # Decode the base64 encoded content and write it to the file
            file.write(base64.b64decode(image_base64))

        # Sleep for 2 seconds to ensure the screenshot is taken
        time.sleep(2)

        # Check if the screenshot file "base64.png" exists in the current directory
        assert os.path.exists("base64.png")


if __name__ == "__main__":
    unittest.main()
