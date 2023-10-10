import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class TestMouseMoveToElement(unittest.TestCase):
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

    def test_move_to_element(self):
        # Navigate to the Selenium Mouse Interaction page
        self.driver.get("https://www.selenium.dev/selenium/web/mouse_interaction.html")

        # Create an instance of ActionChains
        self.actions = ActionChains(self.driver)

        # Locate the element to hover over using its XPath and ID attribute
        hover_element = self.driver.find_element(By.XPATH, "//input[@id='hover']")

        # Perform mouse interactions and move the cursor to the hover element
        self.actions.move_to_element(hover_element).perform()

        # Locate the result element (where the status text is displayed) using its XPath and ID attribute
        result = self.driver.find_element(By.XPATH, "//strong[@id='move-status']")

        # Get the text content of the located result element
        result_text = result.text

        # Use the `assertEqual` method to check if the text matches the expected value
        self.assertEqual(result_text, "hovered")


if __name__ == "__main__":
    unittest.main()
