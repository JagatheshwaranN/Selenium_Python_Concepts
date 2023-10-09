import unittest
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class TestMouseDoubleClick(unittest.TestCase):
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

    def test_mouse_right_click(self):
        # Navigate to the webpage where the mouse interaction test will be performed
        self.driver.get("https://demo.guru99.com/test/simple_context_menu.html")

        # Create an instance of ActionChains
        self.actions = ActionChains(self.driver)

        # Find the web element with the specified XPath that represents the button element.
        button_element = self.driver.find_element(By.XPATH, "//button[contains(text(),'Double-Click Me To See Alert')]")

        # Perform a double click action on the identified button element.
        self.actions.double_click(button_element).perform()

        # Switch to the alert and get its text
        alert = Alert(self.driver)
        alert_text = alert.text

        # Assert that the alert text matches the expected message
        self.assertEqual(alert_text, "You double clicked me.. Thank You..")

        # Accept the alert
        alert.accept()


if __name__ == "__main__":
    unittest.main()
