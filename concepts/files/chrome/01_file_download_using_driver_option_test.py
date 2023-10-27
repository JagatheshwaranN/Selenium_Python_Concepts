import os
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestFileDownloadUsingDriverOption(unittest.TestCase):
    # Initialize the driver variable
    driver = None

    @classmethod
    def setUpClass(cls):
        # Creating Chrome options for customizing the behavior of the Chrome WebDriver
        chrome_options = webdriver.ChromeOptions()

        # Setting preferences for the Chrome WebDriver
        # Here, the "download.default_directory" preference is set to the current working directory
        preferences = {"download.default_directory": os.getcwd()}

        # Adding the preferences to the experimental options of the Chrome WebDriver
        chrome_options.add_experimental_option("prefs", preferences)

        # Initialize the Chrome WebDriver
        cls.driver = webdriver.Chrome(options=chrome_options)

        # Maximize the browser window
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        # Close the driver
        cls.driver.quit()

    def test_file_download_using_driver_option(self):
        # Navigate to the specified URL
        self.driver.get("https://chromedriver.storage.googleapis.com/index.html?path=114.0.5735.90/")

        # Waiting for the download link to be present using WebDriverWait
        download_link = WebDriverWait(self.driver, 3) \
            .until(EC.presence_of_element_located((By.XPATH, "//a[text()='chromedriver_win32.zip']")))

        # Clicking on the download link
        download_link.click()

        # Wait for 5 seconds for file to download
        time.sleep(5)

        # Get the current working directory
        folder = os.getcwd()

        # Get the list of files in the current working directory
        files = os.listdir(folder)

        # Initialize a boolean variable for tracking if the file was found
        found = False

        # Initialize a variable for the downloaded file path
        download_file = None

        # Loop through the files in the directory
        for file in files:
            if os.path.isfile(file):
                # Print the name of the file
                print(f"FIle : {file}")

                # Check if the target file name is contained in the file name
                if "chromedriver_win32.zip" in file:
                    # Set the download file path if the file is found
                    download_file = os.path.join(folder, file)
                    found = True

        # Assert that the file was found, otherwise print the specified message
        self.assertTrue(found, "Downloaded file is not found")

        # Remove the downloaded file
        os.remove(download_file)


if __name__ == "__main__":
    unittest.main()
