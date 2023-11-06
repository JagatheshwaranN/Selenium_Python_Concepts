import unittest
from selenium import webdriver


class TestSetCookies(unittest.TestCase):
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

    def test_set_cookies(self):
        # Define the details of the cookie to be set
        cookie = {
            'name': 'test',  # Name of the cookie
            'value': 'automation',  # Value of the cookie
            'domain': 'www.selenium.dev',  # Domain for which the cookie is set
            'secure': True  # Boolean value indicating whether the cookie is secure
        }

        # Set the cookie using the Chrome DevTools Protocol command 'Network.setCookie'
        self.driver.execute_cdp_cmd('Network.setCookie', cookie)

        # Access the specified URL using the WebDriver instance
        self.driver.get("https://www.selenium.dev")

        # Get the cookie named 'test' from the current page's cookies
        test_cookie = self.driver.get_cookie(cookie['name'])

        # Print the retrieved cookie
        print(test_cookie)

        # Assert that the value of the retrieved cookie matches the expected value 'automation'
        assert test_cookie['value'] == 'automation'


if __name__ == "__main__":
    unittest.main()

