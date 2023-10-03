from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest


class TestClickOnElement(unittest.TestCase):
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

    def test_click_on_element(self):
        # Open the specified URL in Chrome
        self.driver.get("https://admin-demo.nopcommerce.com/login")

        # Find the button element using XPath and click on it
        self.driver.find_element(By.XPATH, "//button[@class='button-1 login-button']").click()

        # Check if the title of the page matches the expected value
        self.assertEqual(self.driver.title, "Dashboard / nopCommerce administration")


if __name__ == "__main__":
    unittest.main()
