import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestPageZoomByPercent(unittest.TestCase):
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

    def test_page_zoom_by_percent(self):
        # Set the zoom percentage to 50%
        percent = "50%"

        # Navigate to the Selenium website
        self.driver.get("https://www.selenium.dev/")

        # Use the JavaScript executor
        js_executor = self.driver.execute_script

        # Execute JavaScript to set the zoom level to the specified percentage
        js_executor("document.body.style.zoom='" + percent + "'")

        # Find the element with the specified XPath
        result = self.driver.find_element(By.XPATH, "//h2[text()='Getting Started']")

        # Check if the element is in the viewport
        assert self.in_viewport(result)

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
