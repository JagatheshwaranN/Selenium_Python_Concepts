import unittest
from selenium import webdriver


class TestMockGeoLocation(unittest.TestCase):
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

    def test_mock_geolocation(self):
        location = {
            "latitude": 36.778259,
            "longitude": -119.417931,
            "accuracy": 1
        }

        self.driver.execute_cdp_cmd('Emulation.setGeolocationOverride', location)

        self.driver.get("https://my-location.org/")


if __name__ == "__main__":
    unittest.main()
