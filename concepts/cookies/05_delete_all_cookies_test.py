import unittest
from selenium import webdriver


class TestDeleteAllCookie(unittest.TestCase):
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

    def test_delete_all_cookies(self):
        # Navigate to the website
        self.driver.get("http://www.example.com/")

        # Add the cookies to the browser
        self.driver.add_cookie({'name': 'Test', 'value': '12345'})
        self.driver.add_cookie({'name': 'User', 'value': '54321'})

        # Get all the cookies
        cookies = self.driver.get_cookies()

        # Print the cookies details
        print(cookies)

        # Deletes all the cookies in the current browsing session
        self.driver.delete_all_cookies()

        # Retrieves the remaining cookies in the current browsing session
        cookies = self.driver.get_cookies()

        # Asserts that no cookies are present
        assert cookies == []


if __name__ == "__main__":
    unittest.main()
