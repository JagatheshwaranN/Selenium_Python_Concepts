import subprocess
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestFileDownloadUsingWget(unittest.TestCase):
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

    def test_file_download_using_wget(self):
        # Navigate to the Guru99 test page
        self.driver.get("https://demo.guru99.com/test/yahoo.html")

        # Find the download button by its ID
        download_button = self.driver.find_element(By.ID, "messenger-download")

        # Get the source URL of the file to download
        download_file_source = download_button.get_attribute("href")

        # Define the wget command to execute for downloading the file
        wget_command = f'cmd /c C:\\Wget\\wget.exe -P D:\\Environment_Collection\\Python_Env' \
                       f'\\SeleniumPythonConcepts --no-check-certificate {download_file_source}'

        try:
            # Execute the wget command using subprocess
            process = subprocess.Popen(wget_command, shell=True)
            process.communicate()

            # Get the exit value of the process
            exit_value = process.returncode

            # Print the exit value of the process
            print(f"Exit Value {exit_value}")
        except (subprocess.CalledProcessError, FileNotFoundError) as ex:

            # Catch any exceptions that might occur during the execution
            print(ex)


if __name__ == "__main__":
    unittest.main()
