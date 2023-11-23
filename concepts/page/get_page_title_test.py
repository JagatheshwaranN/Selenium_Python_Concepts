import unittest
from selenium import webdriver


class TestPageTitle(unittest.TestCase):
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

    def test_get_page_title(self):
        # Navigate to the example.com website
        self.driver.get("https://www.example.com/")

        # Get the page title
        page_title = self.driver.title

        # Assert that the page title matches the expected title
        self.assertEqual(page_title, "Example Domain")


if __name__ == "__main__":
    unittest.main()
