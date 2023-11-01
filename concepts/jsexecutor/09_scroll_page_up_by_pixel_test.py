import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestScrollPageUpByPixel(unittest.TestCase):
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

    def test_scroll_page_up_by_pixel(self):
        # Convert the integer value to a string
        pixel = str(1000)

        # Navigate to the Selenium website
        self.driver.get("https://www.selenium.dev/")

        # Use the JavaScript executor
        js_executor = self.driver.execute_script

        # Scrolls the window by the specified pixel amount in the y-axis direction
        js_executor("window.scrollBy(0, '" + pixel + "')")

        # Scrolls the window in the opposite direction by the specified pixel amount in the y-axis
        js_executor("window.scrollBy(0, -'" + pixel + "')")

        # Find the specific element for the Selenium Logo by XPATH
        selenium_logo = self.driver.find_element(By.XPATH, "//span[@class='navbar-logo']")

        # Check if the element is in the viewport
        assert self.in_viewport(selenium_logo)

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
