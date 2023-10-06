import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class TestMouseClickAndRelease(unittest.TestCase):
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

    def test_mouse_click_and_release(self):
        # Navigate to the Selenium Mouse Interaction page
        self.driver.get("https://www.selenium.dev/selenium/web/mouse_interaction.html")

        # Create an instance of ActionChains
        self.actions = ActionChains(self.driver)

        # Find the web element with the specified XPath that represents the clickable element.
        clickable_element = self.driver.find_element(By.XPATH, "//input[@id='clickable']")

        # Perform a click action on the identified clickable element.
        self.actions.click(clickable_element).perform()

        # Find the result element (a strong element with the specified ID)
        result_element = self.driver.find_element(By.XPATH, "//strong[@id='click-status']")

        # Get the text content of the 'result_element' and store it in 'result_text'.
        result_text = result_element.text

        # Assert that the result text matches the expected text "focused."
        self.assertEqual(result_text, "focused")


if __name__ == "__main__":
    unittest.main()
