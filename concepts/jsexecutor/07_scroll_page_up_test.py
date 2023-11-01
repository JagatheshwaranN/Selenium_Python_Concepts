import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestScrollPageUp(unittest.TestCase):
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

    def test_scroll_page_up(self):
        # Navigate to the Selenium website
        self.driver.get("https://www.selenium.dev/")

        # Find the specific element for the Selenium sponsor by XPATH
        selenium_sponsor_element = self.driver.find_element(By.XPATH, "//h2[@class='selenium text-center']")

        # Use the JavaScript executor
        js_executor = self.driver.execute_script

        # Scrolls the selenium_sponsor_element into view using JavaScript executor
        js_executor("arguments[0].scrollIntoView()", selenium_sponsor_element)

        # Scrolls to the top of the page using JavaScript executor
        js_executor("window.scrollTo(0, -document.body.scrollHeight)")

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
