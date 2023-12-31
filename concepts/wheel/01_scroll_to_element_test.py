import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class TestScrollToElement(unittest.TestCase):
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

    def test_scroll_to_element(self):
        # Navigating to the Selenium website
        self.driver.get("https://www.selenium.dev/")

        # Creating an ActionChains instance for performing actions
        self.actions = ActionChains(self.driver)

        # Locating the element with the CSS selector '.selenium.text-center'
        selenium_sponsors_element = self.driver.find_element(By.CSS_SELECTOR, ".selenium.text-center")

        # Scrolling to the element using ActionChains and performing the action
        self.actions.scroll_to_element(selenium_sponsors_element).perform()

        # Verifying if the element is within the viewport
        assert self.in_viewport(selenium_sponsors_element)

        # Wait for a specified number of seconds
        time.sleep(1)

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
