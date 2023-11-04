import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestGetElementAndScrollIntoView(unittest.TestCase):
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

    def test_get_element_and_scroll_into_view(self):
        # Navigate to the login page of the admin demo on nopCommerce
        self.driver.get("https://admin-demo.nopcommerce.com/login")

        # Get the JavaScript executor for the driver
        js_executor = self.driver.execute_script

        # Scroll to the bottom of the page
        js_executor("window.scrollTo(0, document.body.scrollHeight)")

        # Scroll the 'Email' element into view if it is not already visible
        js_executor("document.getElementById('Email').scrollIntoView(true);")

        # Find the 'Email' element by its ID
        email = self.driver.find_element(By.ID, "Email")

        # Assert whether the 'Email' element is displayed on the page
        self.assertTrue(email.is_displayed())


if __name__ == "__main__":
    unittest.main()
