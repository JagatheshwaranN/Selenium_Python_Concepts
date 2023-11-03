import unittest
from selenium import webdriver


class TestGetPageTitle(unittest.TestCase):
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

    def test_get_page_title(self):
        # Navigate to the Google homepage
        self.driver.get("https://www.google.com/")

        # Use the JavaScript executor
        js_executor = self.driver.execute_script

        # Retrieve the title of the current web page using JavaScript
        title = js_executor("return document.title")

        # Assert whether the retrieved title is "Google" using the assertEquals method
        self.assertEqual(title, "Google")


if __name__ == "__main__":
    unittest.main()
