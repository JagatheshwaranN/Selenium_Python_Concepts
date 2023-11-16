import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestHandleWebsiteLoadFastWithoutImages(unittest.TestCase):
    # Initialize the driver variable
    driver = None

    @classmethod
    def setUpClass(cls):
        # Create ChromeOptions object to configure Chrome WebDriver settings
        chrome_options = Options()

        # Set image loading configuration settings to 2 (2 - Do not load images)
        image_config = {'images': 2}

        # Create dictionary to store Chrome preferences
        preferences = {
            'profile.default_content_setting_values': image_config
        }

        # Set preferences to disable images
        chrome_options.add_experimental_option('prefs', preferences)

        # Initialize ChromeDriver with configured options
        cls.driver = webdriver.Chrome(options=chrome_options)

        # Maximize the browser window
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        # Close the driver
        cls.driver.quit()

    def test_handle_website_load_fast_without_images(self):
        # Load the Amazon India website
        self.driver.get("https://www.amazon.in/")

        # Wait for the "Orders" element to be present on the page
        orders_element = WebDriverWait(self.driver, 5)\
            .until(EC.presence_of_element_located((By.ID, "nav-orders")))

        # Check if the "Orders" element is displayed
        self.assertTrue(orders_element.is_displayed())


if __name__ == "__main__":
    unittest.main()
