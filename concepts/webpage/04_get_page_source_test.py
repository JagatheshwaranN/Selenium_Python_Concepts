import unittest
from selenium import webdriver


class TestGetPageSource(unittest.TestCase):
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

    def test_get_page_source(self):
        # Navigate to the example.com website
        self.driver.get("https://www.example.com/")

        # Get the page source
        page_source = self.driver.page_source

        # Assert that the page source contains the specified title
        self.assertTrue(
                "<title>Example Domain</title>" in page_source)


if __name__ == "__main__":
    unittest.main()
