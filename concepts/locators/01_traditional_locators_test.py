import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestTraditionalLocators(unittest.TestCase):
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

    def test_traditional_locators(self):
        # Navigate to the inputs page
        self.driver.get("https://www.selenium.dev/selenium/web/inputs.html")

        # 1. Name
        self.assertTrue(self.driver.find_element(By.NAME, "no_type").is_displayed())

        # 2. XPath
        self.assertTrue(self.driver.find_element(By.XPATH, "//input[@type='checkbox']").is_displayed())

        # Navigate to the mouse interaction page
        self.driver.get("https://www.selenium.dev/selenium/web/mouse_interaction.html")

        # 3. Id
        self.assertTrue(self.driver.find_element(By.ID, "click").is_displayed())

        # 4. LinkText
        self.assertTrue(self.driver.find_element(By.LINK_TEXT, "Click for Results Page").is_displayed())

        # 5. PartialLinkText
        self.assertTrue(self.driver.find_element(By.PARTIAL_LINK_TEXT, "Click for Result").is_displayed())

        # 6. Class
        self.assertTrue(self.driver.find_element(By.CLASS_NAME, "ui-droppable").is_displayed())

        # 7. CSS
        self.assertTrue(self.driver.find_element(By.CSS_SELECTOR, ".ui-widget-header.ui-droppable").is_displayed())

        # 8. Tag
        self.assertTrue(self.driver.find_element(By.TAG_NAME, "a").is_displayed())


if __name__ == "__main__":
    unittest.main()
