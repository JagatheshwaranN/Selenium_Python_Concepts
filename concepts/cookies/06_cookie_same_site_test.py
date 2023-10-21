import unittest
from selenium import webdriver


class TestCookieSameSite(unittest.TestCase):
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

    def test_cookie_same_site(self):
        # Navigate to the website
        self.driver.get("http://www.example.com/")

        # Create cookies with same-site attribute
        cookie1 = {'name': 'Test', 'value': '12345', 'same_site': 'Strict'}
        cookie2 = {'name': 'User', 'value': '54321', 'same_site': 'Lax'}

        # Add the cookies to the browser
        self.driver.add_cookie(cookie1)
        self.driver.add_cookie(cookie2)

        # Get all the cookies
        cookies = self.driver.get_cookies()

        # Initialize an empty list to store the cookie names
        cookie_list = []

        # The for loop iterates through the cookies list
        for cookie in cookies:
            # Print the expiry details of the cookie
            print(f"SameSite: {cookie['sameSite']}")

            # Add the name of the current cookie to the list
            cookie_list.append(cookie['sameSite'])

        # Asserting the cookie names in the list
        assert cookie_list[0] == "Lax"
        assert cookie_list[1] == "Lax"


if __name__ == "__main__":
    unittest.main()
