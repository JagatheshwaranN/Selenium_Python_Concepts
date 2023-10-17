import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestScrollByGivenAmount(unittest.TestCase):
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

    def test_scroll_by_given_amount(self):
        # Navigate to the Selenium website
        self.driver.get("https://www.selenium.dev/")

        # Initializing the ActionChains object
        self.actions = ActionChains(self.driver)

        # Locating the 'Learn More' button
        selenium_learn_more_button = self.driver.find_element(By.XPATH,
                                                              "//a[contains(@class,'selenium-button "
                                                              "selenium-white-cyan')]")

        """
        Another way to get the y_axis
        y_axis = int(selenium_learn_more_button.rect['y'])
        """
        # Obtaining the y-axis coordinate of the button element
        y_axis = int(selenium_learn_more_button.rect.get('y'))

        # Scrolling by the specified y-axis amount
        self.actions.scroll_by_amount(0, y_axis).perform()

        # Waiting until the button is present in the viewport
        WebDriverWait(self.driver, 2).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(@class,'selenium-button selenium-white-cyan')]")))

        # Asserting whether the button is in the viewport
        assert self.in_viewport(selenium_learn_more_button)

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
