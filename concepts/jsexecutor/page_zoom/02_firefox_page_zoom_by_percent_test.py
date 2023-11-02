import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service as FirefoxService


class TestPageZoomByPercent(unittest.TestCase):
    # Initialize the driver variable
    driver = None

    # Initialize the service variable
    service = None

    @classmethod
    def setUpClass(cls):
        # Create an instance of FirefoxOptions to customize Firefox WebDriver's behavior.
        firefox_options = Options()

        # Specify the path for geckodriver log file
        geckodriver_log_path = "geckodriver.log"

        # Create a Firefox service with the log_output option
        cls.service = FirefoxService(log_output=geckodriver_log_path)

        # Create a Firefox WebDriver instance with the configured options and service
        cls.driver = webdriver.Firefox(options=firefox_options, service=cls.service)

        # Maximize the browser window
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        # Close the driver
        cls.driver.quit()

    def test_page_zoom_by_percent(self):
        # Set the zoom percentage to 75%
        percent = "0.75"

        # Navigate to the Selenium website
        self.driver.get("https://www.selenium.dev/")

        # Use the JavaScript executor
        js_executor = self.driver.execute_script

        # Execute JavaScript to set the zoom level to the specified percentage
        js_executor("document.body.style.MozTransform='scale(" + percent + ")'")

        # Find the element with the specified XPath
        result = self.driver.find_element(By.XPATH, "//h2[text()='Getting Started']")

        # Check if the element is in the viewport
        assert self.in_viewport(result)

        time.sleep(5)

    def in_viewport(self, element):
        # JavaScript code to determine if the element is within the viewport
        script = (
            "for(var e=arguments[0],f=e.offsetTop,t=e.offsetLeft,o=e.offsetWidth,n=e.offsetHeight;\n"
            "e.offsetParent;)f+=(e=e.offsetParent).offsetTop,t+=e.offsetLeft;\n"
            "return f<window.pageYOffset+window.innerHeight&&t<window.pageXOffset+window.innerWidth&&f+n>\n"
            "window.pageYOffset&&t+o>window.pageXOffset"
        )
        # Executing the JavaScript script to determine if the element is within the viewport
        return self.driver.execute_script(script, element)


if __name__ == "__main__":
    unittest.main()
