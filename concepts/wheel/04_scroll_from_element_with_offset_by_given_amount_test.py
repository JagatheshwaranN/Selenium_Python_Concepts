import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin


class TestScrollFromElementWithOffsetByGivenAmount(unittest.TestCase):
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

    def test_scroll_from_element_with_offset_by_given_amount(self):
        # Navigate to the Selenium website
        self.driver.get("https://www.selenium.dev/")

        # Initializing the ActionChains object
        self.actions = ActionChains(self.driver)

        # Find the element for the Selenium donation
        selenium_donation_element = self.driver.find_element(By.XPATH, "//input[@type='image']")

        # Define the scroll origin based on the specified element with offset values
        self.scroll_origin = ScrollOrigin.from_element(selenium_donation_element, 0, -50)

        # Perform a scroll action from the determined scroll origin
        self.actions.scroll_from_origin(self.scroll_origin, 0, 200).perform()

        # Find the element representing the copyright content
        copyright_content_element = self.driver.find_element(By.XPATH, "//small[@class='text-white']")

        # Asserting whether the copyright content is in the viewport
        assert self.in_viewport(copyright_content_element)

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
