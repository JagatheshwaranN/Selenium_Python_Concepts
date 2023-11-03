import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class TestRefreshPage(unittest.TestCase):
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

    def test_refresh_page(self):
        # Navigates to the specified URL
        self.driver.get("https://www.selenium.dev/selenium/web/single_text_input.html")

        # Finds the input element by its ID
        input_element = self.driver.find_element(By.ID, "textInput")

        # Initializes an ActionChains object to perform actions on the webpage
        self.actions = ActionChains(self.driver)

        # Sends the keys "Automation!" to the input element and performs the action
        self.actions.send_keys_to_element(input_element, "Automation!").perform()

        # Executes a JavaScript script to reload the current page
        self.driver.execute_script("document.location.reload()")

        # Finds the input element by its ID after the page reloads
        input_element = self.driver.find_element(By.ID, "textInput")

        # Asserts that the value of the input element is an empty string
        assert input_element.get_attribute("value") == ""


if __name__ == "__main__":
    unittest.main()
