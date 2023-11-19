import time
import unittest
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


class TestSyncUpIssueByCustomApproach(unittest.TestCase):
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

    def test_sync_up_issue_by_custom_approach(self):
        # Load the web page from a local file
        self.driver.get("file:///D:/Environment_Collection/Eclipse_Env/Workspace/Selenium_Concepts/"
                        "src/main/resources/supportFiles/SiteLoadDelay.html")

        # Click on the button with the specified onclick attribute
        self.driver.find_element(By.XPATH, "//button[@onclick='load()']").click()

        # Handle synchronization issue for the specified element
        element = self.handle_element_sync_up(By.XPATH, "//ul[@class='nav__list']//a[@href='/market/login.jsp']")
        element.click()

        # Assert the title of the current web page
        self.assertEqual(self.driver.title, "Login - Video Courses, eBooks, Certifications | Tutorialspoint")

    # A method to handle synchronization issues by waiting for an element to be present in the DOM
    def handle_element_sync_up(self, locator_type, locator):
        # Declare an element
        element = None

        # Try finding the element up to 10 times
        for i in range(10):
            try:
                # Attempt to find the element
                element = self.driver.find_element(locator_type, locator)

                # Break the loop if the element is found
                break
            except NoSuchElementException:
                # Print the message while waiting for the element to appear
                print("Waiting for element to show up on the DOM")

                # Sleep for 1 second before the next attempt
                time.sleep(1)

        # Return the element after it is found
        return element


if __name__ == "__main__":
    unittest.main()
