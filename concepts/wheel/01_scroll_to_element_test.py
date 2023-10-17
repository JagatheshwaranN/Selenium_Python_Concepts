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
        self.driver.get("https://www.selenium.dev/")

        self.actions = ActionChains(self.driver)

        selenium_sponsors_element = self.driver.find_element(By.CSS_SELECTOR, ".selenium.text-center")

        self.actions.scroll_to_element(selenium_sponsors_element).perform()

        assert in_viewport(self.driver, selenium_sponsors_element)


if __name__ == "__main__":
    unittest.main()

    def in_viewport(driver, element):
        script = """
            var rect = arguments[0].getBoundingClientRect();
            return (
                rect.top >= 0 &&
                rect.left >= 0 &&
                rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
                rect.right <= (window.innerWidth || document.documentElement.clientWidth)
            );
        """
        return driver.execute_script(script, element)

