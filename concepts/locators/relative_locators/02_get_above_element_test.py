import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import relative_locator


class TestGetAboveElement(unittest.TestCase):
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

    def test_get_above_element(self):
        # Open the website in the browser
        self.driver.get("https://automationbookstore.dev/")

        # Locate the element above the specified element using the relative locator
        relative_locator.locate_with(By.ID, "pid4").above({By.ID: "pid8"})

        # Find the element using the relative locator and get its attribute "id"
        book_id = self.driver.find_element(relative_locator.with_tag_name("li")
                                           .above({By.ID: "pid8"})).get_attribute("id")

        # Assert whether the retrieved "id" matches the expected value "pid4"
        self.assertEqual(book_id, "pid4")


if __name__ == "__main__":
    unittest.main()
