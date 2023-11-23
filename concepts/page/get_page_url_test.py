import unittest
from selenium import webdriver


class TestPageUrl(unittest.TestCase):
    # Initialize the driver variable
    driver = None

    @classmethod
    def setUp(cls):
        # Initialize the Chrome WebDriver
        cls.driver = webdriver.Chrome()

        # Maximize the browser window
        cls.driver.maximize_window()

    @classmethod
    def tearDown(cls):
        # Close the driver
        cls.driver.quit()

    # @unittest.skip("Skip this test for now")
    def test_get_page_url(self):
        # Navigate to the example.com website
        self.driver.get("https://www.example.com/")

        # Get the current page URL
        page_url = self.driver.current_url

        # Assert that the URL matches the expected URL
        self.assertEqual(page_url, "https://www.example.com/")


if __name__ == "__main__":
    unittest.main()
