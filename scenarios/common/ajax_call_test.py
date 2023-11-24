import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestAjaxCall(unittest.TestCase):
    # Initialize the driver variable
    driver = None

    # Initialize the wait timeout
    WAIT_TIMEOUT = 10

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

    def test_ajax_call(self):
        # Navigate to the specified URL
        self.driver.get("https://omayo.blogspot.com/")

        # Wait for the page to load completely
        self.until_page_load_complete()

        # Scroll to the bottom of the page using JavaScriptExecutor
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

        # Find and click a dropdown button
        drop_down = self.driver.find_element(By.CSS_SELECTOR, "button.dropbtn")
        drop_down.click()

        # Wait for Ajax calls to complete
        self.until_jquery_is_done()

        # Find the 'Flipkart' link within an element using XPath
        flipkart = self.driver.find_element(By.XPATH, "//div[@id='myDropdown']//a[text()='Flipkart']")

        # Wait for the 'flipkart' element to be clickable and click it
        WebDriverWait(self.driver, self.WAIT_TIMEOUT).until(
            EC.element_to_be_clickable(flipkart)).click()

        # Get the current URL and check if it matches the expected URL
        result = self.driver.current_url
        assert result == "https://www.flipkart.com/"

    def until_jquery_is_done(self):
        # Custom wait condition to check for no active jQuery AJAX requests
        self.until(lambda driver: self.driver.execute_script("return jQuery.active==0"))

    def until_page_load_complete(self):
        # Custom wait condition to wait for document.readyState to be "complete"
        self.until(lambda driver: self.driver.execute_script("return document.readyState") == "complete")

    def until(self, wait_condition):
        # Create a WebDriverWait instance with a specified timeout
        wait = WebDriverWait(self.driver, self.WAIT_TIMEOUT)

        try:
            # Wait until the specified condition is met
            wait.until(wait_condition)

        except Exception as e:
            # Print the error message if an exception occurs during the waiting period
            print(e)


if __name__ == "__main__":
    unittest.main()
