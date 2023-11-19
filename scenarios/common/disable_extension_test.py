import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class TestDisableExtension(unittest.TestCase):
    # Initialize the driver variable
    driver = None

    @classmethod
    def setUpClass(cls):
        # Create ChromeOptions object to configure Chrome WebDriver settings
        chrome_options = Options()

        # Add arguments to ChromeOptions (For disabling extension)
        chrome_options.add_argument("--disable-extensions")

        # Initialize ChromeDriver with configured options
        cls.driver = webdriver.Chrome(options=chrome_options)

        # Maximize the browser window
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        # Close the driver
        cls.driver.quit()

    def test_disable_extension(self):
        # Navigate to the Google website
        self.driver.get("https://www.google.com/")

        # Get the title of the current page
        title = self.driver.title

        # Verify if the title matches the expected title ('Google')
        self.assertEqual(title, "Google")


if __name__ == "__main__":
    unittest.main()
