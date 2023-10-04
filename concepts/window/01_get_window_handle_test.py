import unittest
from selenium import webdriver


class TestWindowHandle(unittest.TestCase):
    # Initialize the driver variable
    driver = None

    @classmethod
    def setUp(cls):
        # Initialize the Chrome WebDriver
        cls.driver = webdriver.Chrome()

        # Maximize the browser window
        cls.driver.maximize_window()

    @classmethod
    def tearDown(cls):
        # Close the driver
        cls.driver.quit()

    def test_get_window_handle(self):
        # Navigate to the website
        self.driver.get("https://letcode.in/frame")

        # Get the current window handle
        window_handle = self.driver.current_window_handle

        # Print the window handle
        print(window_handle)


if __name__ == "__main__":
    unittest.main()
