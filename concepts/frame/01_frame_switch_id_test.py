import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestFrame(unittest.TestCase):
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

    def test_switch_inside_frame_using_id(self):
        # Navigate to the webpage
        self.driver.get("https://demo.automationtesting.in/Frames.html")

        # Switch to the iframe by ID
        self.driver.switch_to.frame("singleframe")

        # Find the input element within the iframe using its tag name ("input")
        input_element = self.driver.find_element(By.TAG_NAME, "input")

        # Send the keys "Python" to the input element, simulating user input
        input_element.send_keys("Python")

        # Wait for 5 seconds - For demo purpose
        time.sleep(5)


if __name__ == "__main__":
    unittest.main()
