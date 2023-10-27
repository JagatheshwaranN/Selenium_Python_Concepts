import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pynput.keyboard import Key, Controller


class TestFileUploadByBrowse(unittest.TestCase):
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

    def test_file_upload_by_browse(self):
        # Navigate to the Plupload Examples page
        self.driver.get("https://www.plupload.com/examples/")

        # Find the file input element by ID
        file_input = self.driver.find_element(By.ID, "uploader_browse")

        # Simulate a click action on the file input
        file_input.click()

        # Introduce a delay to ensure the file dialog has appeared
        time.sleep(3)

        # Initialize a keyboard controller
        self.keyboard = Controller()

        # Type the file path into the file dialog
        self.keyboard.type(
            "D:\\Environment_Collection\\Python_Env\\SeleniumPythonConcepts\\concepts\\files\\python.png")

        # Simulate the press and release of the Enter key to confirm the file selection
        self.keyboard.press(Key.enter)
        self.keyboard.release(Key.enter)

        # Wait for 2 seconds to allow the file upload process to complete
        time.sleep(2)

        # Find the uploaded file by XPath
        uploaded_file = self.driver.find_element(By.XPATH, "//div[@class='plupload_file_thumb "
                                                           "plupload_thumb_embedded']")

        # Assert whether the uploaded file is displayed
        self.assertTrue(uploaded_file.is_displayed())


if __name__ == "__main__":
    unittest.main()
