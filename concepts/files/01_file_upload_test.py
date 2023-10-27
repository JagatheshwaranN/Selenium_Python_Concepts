import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestFileUpload(unittest.TestCase):
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

    def test_file_upload(self):
        # Navigate to the Guru99 test page
        self.driver.get("https://demo.guru99.com/test/upload/")

        # Find the file input element by ID
        file_input = self.driver.find_element(By.ID, "uploadfile_0")

        # Send the file path to the file input element
        file_input.send_keys(
            "D:\\Environment_Collection\\Python_Env\\SeleniumPythonConcepts\\concepts\\files\\sample.txt")

        # Find the submit button by ID
        submit_button = self.driver.find_element(By.ID, "submitbutton")

        # Click on the submit button
        submit_button.click()

        # Find the file upload message by XPath
        file_upload_message = self.driver.find_element(By.XPATH, "(//center)[2]")

        # Assert whether the file upload message is displayed
        self.assertTrue(file_upload_message.is_displayed())


if __name__ == "__main__":
    unittest.main()
