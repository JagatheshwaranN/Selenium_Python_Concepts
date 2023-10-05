import time
import unittest
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

    def test_switch_to_parent_frame(self):
        # Navigate to the web page
        self.driver.get("https://letcode.in/frame")

        # Switch to the first frame with name "firstFr"
        self.driver.switch_to.frame("firstFr")

        # Find the child frame using an XPath selector with the 'src' attribute value
        child_frame = self.driver.find_element(By.XPATH, "//iframe[@src='innerFrame']")

        # Switch the WebDriver's focus to the found child frame
        self.driver.switch_to.frame(child_frame)

        # Find the email input element by its 'name' attribute
        email_input = self.driver.find_element(By.NAME, "email")

        # Enter the text "abc@test.com" into the found email input element
        email_input.send_keys("abc@test.com")

        # Wait for some time - For demo purpose
        time.sleep(3)

        # Switch back to the parent frame
        self.driver.switch_to.parent_frame()

        # Find the firstname input element by its 'name' attribute
        email_input = self.driver.find_element(By.NAME, "fname")

        # Enter the text "Test" into the found firstname input element
        email_input.send_keys("Test")

        # Wait for some time - For demo purpose
        time.sleep(3)

        # Switch back to the default content
        self.driver.switch_to.default_content()

        # Find the header element with XPath selector
        header_element = self.driver.find_element(By.XPATH, "(//div[@class='hero-body'])[1]")

        # Check that the found element is displayed on the page
        self.assertTrue(header_element.is_displayed())


if __name__ == "__main__":
    unittest.main()
