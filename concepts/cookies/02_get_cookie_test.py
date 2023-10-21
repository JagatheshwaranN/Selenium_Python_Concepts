import unittest
from selenium import webdriver


class TestGetCookie(unittest.TestCase):
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

    def test_get_cookie(self):
        # Navigate to the website
        self.driver.get("http://www.example.com/")

        # Add the cookie to the browser
        self.driver.add_cookie({'name': 'Test', 'value': '12345'})

        # Get the cookie by name
        cookie = self.driver.get_cookie("Test")

        # Print the cookie details
        print(cookie)

        # Asserting the cookie name is equal to "User"
        assert cookie['name'] == "Test"


if __name__ == "__main__":
    unittest.main()
