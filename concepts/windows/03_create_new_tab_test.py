import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestCreateNewTab(unittest.TestCase):
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

    def test_create_new_tab(self):
        # Navigate to the website
        self.driver.get("https://the-internet.herokuapp.com/windows")

        # Store the handle of the parent window
        parent_window = self.driver.current_window_handle

        # Print the Parent Window Handle
        print("Parent Window Handle : ", parent_window)

        """
        Alternate option to switch to new TAB
        =====================================
         # Open a new tab using Selenium
        driver.execute_script("window.open('', '_blank');")
        
        # Switch to the new tab
        driver.switch_to.window(driver.window_handles[-1])
        """

        # Switch to the new tab
        self.driver.switch_to.new_window('tab')

        # Navigate to the new URL
        self.driver.get("https://the-internet.herokuapp.com/windows/new")

        # Store the handle of the child window
        child_window = self.driver.current_window_handle

        # Print the Child Window Handle
        print("Child Window Handle : ", child_window)

        # Wait for the title of the child window to be "New Window"
        WebDriverWait(self.driver, 10).until(EC.title_is("New Window"))

        # Close the child window
        self.driver.close()

        # Switch back to the parent window
        self.driver.switch_to.window(parent_window)


if __name__ == "__main__":
    unittest.main()
