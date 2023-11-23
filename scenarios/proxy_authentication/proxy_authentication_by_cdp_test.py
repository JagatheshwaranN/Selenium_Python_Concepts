import base64
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestProxyAuthenticationByCDP(unittest.TestCase):
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

    def test_proxy_authentication_by_cdp(self):
        # Enable Network domain in Chrome DevTools Protocol (CDP)
        self.driver.execute_cdp_cmd("Network.enable", {})

        # Define username and password for basic authentication
        username = "admin"
        password = "admin"

        # Concatenate username and password with a colon separator and encode it in Base64
        credentials = f"{username}:{password}"
        encoded_credentials = base64.b64encode(credentials.encode("utf-8")).decode("utf-8")

        # Print the encoded credentials (for debugging or verification)
        print(encoded_credentials)

        # Set the Authorization header with the encoded credentials for basic authentication
        headers = {
            "headers": {
                "Authorization": "Basic " + encoded_credentials
            }
        }

        # Set extra HTTP headers using Chrome DevTools Protocol (CDP)
        self.driver.execute_cdp_cmd("Network.setExtraHTTPHeaders", headers)

        # Navigate to the URL
        self.driver.get("http://the-internet.herokuapp.com/basic_auth")

        # Locate an <h3> element with the text "Basic Auth" using XPath and retrieve its text content
        result = self.driver.find_element(By.XPATH, "//h3[text()='Basic Auth']").text

        # Assert that the retrieved text matches the expected value ("Basic Auth").
        self.assertEqual(result, "Basic Auth")


if __name__ == "__main__":
    unittest.main()
