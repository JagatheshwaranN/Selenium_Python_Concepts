import unittest
from selenium import webdriver


class TestGetCookies(unittest.TestCase):
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

    def test_get_cookies(self):
        # Navigate to the website
        self.driver.get("http://www.example.com/")

        # Add the cookies to the browser
        self.driver.add_cookie({'name': 'Test', 'value': '12345'})
        self.driver.add_cookie({'name': 'User', 'value': '54321'})

        # Get all the cookies
        cookies = self.driver.get_cookies()

        # Print the cookies details
        print(cookies)

        # Initialize an empty list to store the cookie names
        cookie_list = []

        # The for loop iterates through the cookies list and prints various details related to each
        # cookie, including its name, value, domain, path, expiry, security, and HTTP status.
        for cookie in cookies:
            print(f"Name     : {cookie['name']}")
            print(f"Value    : {cookie['value']}")
            print(f"Domain   : {cookie['domain']}")
            print(f"Path     : {cookie['path']}")
            print(f"SameSite : {cookie['sameSite']}")
            print(f"Secure   : {cookie['secure']}")
            print(f"Http     : {cookie['httpOnly']}")

            # Add the name of the current cookie to the list
            cookie_list.append(cookie['name'])

        # Asserting the cookie names in the list
        assert cookie_list[0] == "User"
        assert cookie_list[1] == "Test"


if __name__ == "__main__":
    unittest.main()
