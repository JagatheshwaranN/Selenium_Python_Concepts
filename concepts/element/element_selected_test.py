import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestElementSelected(unittest.TestCase):
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

    def test_element_selected(self):
        # Navigate to the inputs page
        self.driver.get("https://www.selenium.dev/selenium/web/inputs.html")

        # Find the element using a CSS selector and verify if it's selected
        element = self.driver.find_element(By.CSS_SELECTOR, "input[name='checkbox_input']")

        # Assert that the element is selected on the page
        self.assertTrue(element.is_selected())


if __name__ == "__main__":
    unittest.main()
