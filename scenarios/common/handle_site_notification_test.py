import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class TestHandleSiteNotification(unittest.TestCase):
    # Initialize the driver variable
    driver = None

    @classmethod
    def setUpClass(cls):
        # Create ChromeOptions object to configure Chrome WebDriver settings
        chrome_options = Options()

        # Add arguments to ChromeOptions (commented out for disabling notifications)
        # chrome_options.add_argument("--disable-notifications")

        # Create dictionary to store Chrome preferences
        preferences = {
            'profile.default_content_setting_values.notifications': 2
        }

        # Set preferences to disable notifications
        chrome_options.add_experimental_option('prefs', preferences)

        # Initialize ChromeDriver with configured options
        cls.driver = webdriver.Chrome(options=chrome_options)

        # Maximize the browser window
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        # Close the driver
        cls.driver.quit()

    def test_handle_site_notification(self):
        # Navigate to the Facebook website
        self.driver.get("https://www.facebook.com/")

        # Get the title of the current page
        title = self.driver.title

        # Check if the title matches the expected title
        self.assertEqual(title, "Facebook – log in or sign up")


if __name__ == "__main__":
    unittest.main()
