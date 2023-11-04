import unittest
from selenium import webdriver


class TestGetElements(unittest.TestCase):
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

    def test_get_elements(self):
        # Navigate to the DemoQA site
        self.driver.get("https://demoqa.com/broken")

        # Get the JavaScript executor for the current driver
        js_executor = self.driver.execute_script

        # Retrieve the image elements by its TagName using JavaScript executor
        images = js_executor("return document.getElementsByTagName('img');")

        # Assert whether the length of the 'images' list is equal to 4
        self.assertEqual(len(images), 4)


if __name__ == "__main__":
    unittest.main()
