import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestProxyAuthenticationByURL(unittest.TestCase):
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

    def test_proxy_authentication_by_url(self):
        # Navigate to the URL that includes basic authentication credentials
        self.driver.get("http://admin:admin@the-internet.herokuapp.com/basic_auth")

        # Locate an <h3> element with the text "Basic Auth" using XPath and retrieve its text content
        result = self.driver.find_element(By.XPATH, "//h3[text()='Basic Auth']").text

        # Assert that the retrieved text matches the expected value ("Basic Auth").
        self.assertEqual(result, "Basic Auth")


if __name__ == "__main__":
    unittest.main()
