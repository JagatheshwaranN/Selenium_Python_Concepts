import unittest
from selenium import webdriver


class TestWindowSize(unittest.TestCase):
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

    def test_window_size(self):
        # Navigate to the website
        self.driver.get("https://the-internet.herokuapp.com/windows")

        # Get the current window size and store it in the window_size1 dictionary
        window_size1 = self.driver.get_window_size()

        # Extract the 'height' and 'width' values from the window_size1 dictionary
        height1 = window_size1['height']
        width1 = window_size1['width']

        # Print the height and width of the window before setting a new size
        print("Window's Height before setting new size ==> " + str(height1))
        print("Window's Width before setting new size  ==> " + str(width1))

        # Set window size to 1024x768
        self.driver.set_window_size(1024, 768)

        # Get the current window size and store it in the window_size2 dictionary
        window_size2 = self.driver.get_window_size()

        # Extract the 'height' and 'width' values from the window_size2 dictionary
        height2 = window_size2['height']
        width2 = window_size2['width']

        # Print the height and width of the window after setting a new size
        print("Window's Height after setting new size ==> " + str(height2))
        print("Window's Width after setting new size  ==> " + str(width2))

        # Verify that the window size has been set correctly
        self.assertEqual(height2, 768)
        self.assertEqual(width2, 1024)


if __name__ == "__main__":
    unittest.main()
