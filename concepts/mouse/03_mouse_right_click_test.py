import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class TestMouseRightClick(unittest.TestCase):
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

        # Find the web element with the specified XPath that represents the context menu element.
        context_menu_element = self.driver.find_element(By.XPATH, "//span[contains(@class,'context-menu-one')]")

        # Perform a context click action on the identified context menu element.
        self.actions.context_click(context_menu_element).perform()

        # Find the element representing the 'Copy' option in the context menu
        copy_element = self.driver.find_element(By.CSS_SELECTOR,
                                                ".context-menu-item.context-menu-icon.context-menu-icon-copy")

        # Get the text content of the 'Copy' option
        result = copy_element.text

        # Assert that the result matches the expected text "copy"
        self.assertEqual(result, "Copy")


if __name__ == "__main__":
    unittest.main()
