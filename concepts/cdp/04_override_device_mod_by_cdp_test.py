import unittest
from selenium import webdriver


class TestOverrideDeviceMod(unittest.TestCase):
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

    def test_override_device_mod(self):
        # Define the device metrics to be overridden
        metrics_override = {
            "width": 400,
            "height": 900,
            "deviceScaleFactor": 70,
            "mobile": True
        }

        # Execute the CDP command to set the device metrics override
        self.driver.execute_cdp_cmd('Emulation.setDeviceMetricsOverride', metrics_override)

        # Navigate to the specified URL
        self.driver.get("https://www.google.com/")


if __name__ == "__main__":
    unittest.main()
