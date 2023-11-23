import unittest
from selenium import webdriver


class TestWindowPosition(unittest.TestCase):
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

    def test_window_position(self):
        # Navigate to the website
        self.driver.get("https://the-internet.herokuapp.com/windows")

        # Get the initial window position
        window_initial_position = self.driver.get_window_position()

        # Print the initial window position
        print("Initial Window Position (X, Y): ", window_initial_position)

        # Assert that the window position X and Y are less than or equal to 0
        self.assertGreaterEqual(window_initial_position['x'], -8)
        self.assertGreaterEqual(window_initial_position['y'], -8)

        # Set the window position to a specific X and Y coordinates (e.g., X=5, Y=5)
        self.driver.set_window_position(5, 5)

        # Get the new window position
        window_new_position = self.driver.get_window_position()

        # Print the new window position
        print("New Window Position (X, Y): ", window_new_position)

        # Assert that the window position has been set to the specified coordinates
        self.assertGreaterEqual(window_new_position['x'], 5)
        self.assertGreaterEqual(window_new_position['y'], 5)


if __name__ == "__main__":
    unittest.main()
