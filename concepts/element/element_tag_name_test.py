import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestElementTagName(unittest.TestCase):
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

    def test_element_tag_name(self):
        # Navigate to the inputs page
        self.driver.get("https://www.selenium.dev/selenium/web/inputs.html")

        # Find the element using a CSS selector and get its tag name
        element = self.driver.find_element(By.CSS_SELECTOR, "input[name='number_input']")
        element_tag = element.tag_name

        # Assert that the retrieved tag name matches the expected value
        self.assertTrue(element_tag, "input")


if __name__ == "__main__":
    unittest.main()
