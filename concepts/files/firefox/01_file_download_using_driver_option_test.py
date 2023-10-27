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
        # Create a Firefox profile
        firefox_profile = webdriver.FirefoxProfile()

        # Creating Firefox options for customizing the behavior of the Firefox WebDriver
        firefox_options = webdriver.FirefoxOptions()

        # Set preferences for the browser download settings
        # 2 indicates the desktop
        firefox_profile.set_preference("browser.download.folderList", 2)

        # Set the download directory to the current directory
        firefox_profile.set_preference("browser.download.dir",
                                       os.getcwd())
        # Set MIME types to save directly without asking
        firefox_profile.set_preference("browser.helperApps.neverAsk.saveToDisk",
                                       "text/csv,application/zip")

        # Assign the profile to the options
        firefox_options.profile = firefox_profile

        # Launch the Firefox browser with the configured options
        cls.driver = webdriver.Firefox(options=firefox_options)

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
