from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import unittest


class TestClearElement(unittest.TestCase):
    # Initialize the driver variable
    driver = None

    @classmethod
    def setUp(cls):
        # Initialize the Chrome WebDriver
        cls.driver = webdriver.Chrome()

        # Maximize the browser windows
        cls.driver.maximize_window()

    @classmethod
    def tearDown(cls):
        # Close the driver
        cls.driver.quit()

    def test_clear_element(self):
        # Open the specified URL in Chrome
        self.driver.get("https://admin-demo.nopcommerce.com/login")

        # Find the email input field using CSS selector
        email = self.driver.find_element(By.CSS_SELECTOR, "input[name='Email']")

        # Clear the input field
        email.clear()

        # Click on the input field
        email.click()

        # Create an ActionChains object to simulate pressing the Enter key
        action = ActionChains(self.driver)
        action.key_down(Keys.ENTER).perform()

        # Find the error text using XPath
        error_text = self.driver.find_element(By.XPATH, "//span[@id='Email-error']").text

        # Check if the error text matches the expected value
        self.assertEqual(error_text, "Please enter your email")


# Run the tests if this script is executed directly
if __name__ == "__main__":
    unittest.main()
