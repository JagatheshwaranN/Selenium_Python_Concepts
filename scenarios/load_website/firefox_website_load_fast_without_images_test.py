import unittest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service as FirefoxService


class TestWebsiteLoadFastWithoutImages(unittest.TestCase):
    # Initialize the driver variable
    driver = None

    @classmethod
    def setUpClass(cls):
        # Create FirefoxOptions object to configure Firefox WebDriver settings
        firefox_options = Options()

        # Create a new Firefox profile
        firefox_profile = webdriver.FirefoxProfile()

        # Set the preference for image permissions to 2 (2 - Do not load images)
        firefox_profile.set_preference("permissions.default.image", 2)

        # Set the FirefoxOptions with the created profile
        firefox_options.profile = firefox_profile

        # Specify the path for geckodriver log file
        geckodriver_log_path = "geckodriver.log"

        # Create a Firefox service with the log_output option
        service = FirefoxService(log_output=geckodriver_log_path)

        # Initialize FirefoxDriver with configured options
        cls.driver = webdriver.Firefox(options=firefox_options, service=service)

    @classmethod
    def tearDownClass(cls):
        # Close the driver
        cls.driver.quit()

    def test_website_load_fast_without_images(self):
        # Load the Amazon India website
        self.driver.get("https://www.amazon.in/")

        # Wait for the "Orders" element to be present on the page
        orders_element = WebDriverWait(self.driver, 5)\
            .until(EC.presence_of_element_located((By.ID, "nav-orders")))

        # Check if the "Orders" element is displayed
        self.assertTrue(orders_element.is_displayed())


if __name__ == "__main__":
    unittest.main()
