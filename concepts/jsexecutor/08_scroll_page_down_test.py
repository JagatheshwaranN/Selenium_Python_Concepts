import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestScrollPageDown(unittest.TestCase):
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

    def test_scroll_page_down(self):
        # Navigate to the Selenium website
        self.driver.get("https://www.selenium.dev/")

        # Use the JavaScript executor
        js_executor = self.driver.execute_script

        # Scrolls to the bottom of the page using JavaScript executor
        js_executor("window.scrollTo(0, document.body.scrollHeight)")

        # Finds the element containing copyright information using XPath
        selenium_copyright = self.driver.find_element(By.XPATH, "//small[@class='text-white']")

        # Check if the element is in the viewport
        assert self.in_viewport(selenium_copyright)

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
