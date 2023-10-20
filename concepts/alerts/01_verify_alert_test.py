import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestVerifyAlert(unittest.TestCase):
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

    def test_verify_alert(self):
        # Navigate to the specified URL
        self.driver.get("https://the-internet.herokuapp.com/javascript_alerts")

        # Set up a wait with a timeout of 5 seconds
        wait = WebDriverWait(self.driver, 5)

        # Find the button element with the specified XPath and click on it
        alert_button = self.driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']")
        alert_button.click()

        # Wait until an alert is present and store the alert
        alert = wait.until(EC.alert_is_present())

        # Get the text content of the alert
        alert_content = alert.text

        # Print the text content of the alert
        print(alert_content)

        # Accept the alert
        alert.accept()

        # Assert that the alert_content is equal to "I am a JS Alert"
        assert alert_content == "I am a JS Alert"


if __name__ == "__main__":
    unittest.main()
