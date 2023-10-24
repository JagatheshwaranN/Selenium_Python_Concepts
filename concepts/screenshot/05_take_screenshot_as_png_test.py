import os.path
import time
import unittest
from selenium import webdriver


class TestTakeScreenshotAsPng(unittest.TestCase):
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

    def test_take_screenshot_as_png(self):
        # Navigate to the website
        self.driver.get("http://www.example.com")

        # Capture the screenshot of the current page as a PNG file
        png_file = self.driver.get_screenshot_as_png()

        # Write the screenshot data to a file named "png.png" in binary mode
        with open("png.png", "wb") as file:
            # write the png_file content to the file
            file.write(png_file)

            # Close the file
            file.close()

        # Sleep for 2 seconds to ensure the screenshot is taken
        time.sleep(2)

        # Check if the screenshot file "png.png" exists in the current directory
        assert os.path.exists("png.png")


if __name__ == "__main__":
    unittest.main()
