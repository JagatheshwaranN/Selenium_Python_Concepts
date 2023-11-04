import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys


class TestGetElement(unittest.TestCase):
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

    def test_get_element(self):
        # Navigate to the Google homepage
        self.driver.get("https://www.google.com/")

        # Get the JavaScript executor for the current driver
        js_executor = self.driver.execute_script

        # Retrieve the search bar element by its ID using JavaScript executor
        search_bar = js_executor("return document.getElementById('APjFqb');")

        # Enter the search query 'javascript' in the search bar
        search_bar.send_keys("javascript")

        # Simulate the Enter key press using ActionChains to submit the search query
        ActionChains(self.driver).send_keys(Keys.ENTER).perform()

        # Assert whether the title of the current page is 'javascript - Google Search'
        self.assertEqual(self.driver.title, "javascript - Google Search")


if __name__ == "__main__":
    unittest.main()
