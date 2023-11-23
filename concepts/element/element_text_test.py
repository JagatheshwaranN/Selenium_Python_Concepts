import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestElementText(unittest.TestCase):
    # Initialize the driver variable
    driver = None

    @classmethod
    def setUpClass(cls):
        # Initialize the Chrome WebDriver
        cls.driver = webdriver.Chrome()

        # Maximize the browser windows
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        # Close the driver
        cls.driver.quit()

    def test_get_element_text(self):
        # Navigate to the inputs page
        self.driver.get("https://www.selenium.dev/selenium/web/inputs.html")

        # Find the element using a Tag Name
        element = self.driver.find_element(By.TAG_NAME, "h1")

        # Get the element text
        element_text = element.text

        # Assert that the retrieved text match the expected values
        self.assertEqual(element_text, "Testing Inputs")


if __name__ == "__main__":
    unittest.main()
