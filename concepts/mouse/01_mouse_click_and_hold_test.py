import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class TestMouseClickAndHold(unittest.TestCase):
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

    def test_mouse_click_and_hold(self):
        # Navigate to the specified URL using the WebDriver.
        self.driver.get("https://letcode.in/buttons")

        # Create an instance of ActionChains
        actions = ActionChains(self.driver)

        # Find the button element using its XPath and store it in the 'button_element' variable.
        button_element = self.driver.find_element(By.XPATH, "(//button[@class='button is-primary'])[2]")

        # Perform a click and hold action on the 'button_element' using the 'actions' object.
        actions.click_and_hold(button_element).perform()

        # Wait for a moment
        self.wait_for_some_time(3)

        # Find the result element (a h2 element with the specified text) using its XPath and store it in
        # 'result_element'.
        result_element = self.driver.find_element(By.XPATH, "//h2[text()='Button has been long pressed']")

        # Get the text content of the 'result_element' and store it in 'result_text'.
        result_text = result_element.text

        # Assert that the 'result_text' matches the expected text "Button has been long pressed."
        self.assertEqual(result_text, "Button has been long pressed")

    def wait_for_some_time(self, seconds):
        # Helper method to wait for a specified number of seconds
        import time
        time.sleep(seconds)


if __name__ == "__main__":
    unittest.main()
