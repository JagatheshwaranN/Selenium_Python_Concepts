import unittest
import time
from selenium import webdriver


class TestFullScreenWindow(unittest.TestCase):
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

    def test_fullscreen_window(self):
        # Navigate to the test page
        self.driver.get("https://the-internet.herokuapp.com/windows")

        # Maximize the browser window (full-screen)
        self.driver.fullscreen_window()

        # Wait for some time - For demo purpose
        self.wait_for_some_time()

    def wait_for_some_time(self):
        # Wait for some time
        time.sleep(2)


if __name__ == "__main__":
    unittest.main()
