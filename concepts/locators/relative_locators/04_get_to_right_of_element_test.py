import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import relative_locator


class TestGetToRightOfElement(unittest.TestCase):
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

    def test_get_to_right_of_element(self):
        # Open the website in the browser
        self.driver.get("https://automationbookstore.dev/")

        # Locate the element to the right of the specified element using the relative locator
        relative_locator.locate_with(By.ID, "pid6").to_right_of({By.ID: "pid5"})

        # Finding the element to the right of the specified element using relative_locator
        book_id = self.driver.find_element(relative_locator.with_tag_name("li")
                                           .to_right_of({By.ID: "pid5"})).get_attribute("id")

        # Asserting that the retrieved element's ID matches the expected value
        self.assertEqual(book_id, "pid6")


if __name__ == "__main__":
    unittest.main()
