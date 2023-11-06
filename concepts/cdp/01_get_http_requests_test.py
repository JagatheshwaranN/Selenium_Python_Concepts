import unittest
from selenium import webdriver
from selenium.webdriver.common.devtools.v116.network import Headers
from selenium.webdriver.common.devtools.v116.network import PrivateNetworkRequestPolicy


class TestGetHttpRequest(unittest.TestCase):
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

    def test_get_http_request(self):
        self.driver.execute_cdp_cmd('Network.enable', {})
        self.driver.execute_cdp_cmd('Network.requestWillBeSent', {})

        self.driver.get("https://google.com/")
        self.driver.execute_cdp_cmd('Network.disable', {})



