import base64
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestSetBasicAuth(unittest.TestCase):
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

    def test_set_basic_auth(self):
        # Enable the Network domain to allow the driver to modify network behavior
        self.driver.execute_cdp_cmd("Network.enable", {})

        # Encode the credentials in Base64 format for basic authentication
        credentials = base64.b64encode("admin:admin".encode()).decode()

        # Create headers with authorization using the encoded credentials
        headers = {'headers': {'authorization': 'Basic ' + credentials}}

        # Set the extra HTTP headers for the network requests using the Chrome DevTools Protocol
        # command 'Network.setExtraHTTPHeaders'
        self.driver.execute_cdp_cmd("Network.setExtraHTTPHeaders", headers)

        # Access the specified URL using the WebDriver instance
        self.driver.get('https://the-internet.herokuapp.com/basic_auth')

        # Find the element containing the success message
        success = self.driver.find_element(By.TAG_NAME, "p")

        # Assert that the text of the success element matches the expected success message
        assert success.text == 'Congratulations! You must have the proper credentials.'


if __name__ == "__main__":
    unittest.main()
