import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class TestTooltip(unittest.TestCase):
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

    def test_tooltip(self):
        # Navigate to the jQuery UI tooltip page
        self.driver.get("https://jqueryui.com/tooltip/")

        # Find the iframe element that contains the tooltip
        frame_element = self.driver.find_element(By.XPATH, "//iframe[@class='demo-frame']")

        # Switch to the iframe to interact with elements inside it
        self.driver.switch_to.frame(frame_element)

        # Create an ActionChains object to perform actions on elements
        actions = ActionChains(self.driver)

        # Move the mouse cursor to the element with the ID 'age' (triggering the tooltip)
        actions.move_to_element(self.driver.find_element(By.ID, "age")).perform()

        # Find the tooltip element and retrieve its text content
        tooltip = self.driver.find_element(By.XPATH, "//div[@class='ui-tooltip-content']").text

        # Check if the tooltip text matches the expected text
        self.assertEqual(tooltip, "We ask for your age only for statistical purposes.")


if __name__ == "__main__":
    unittest.main()

