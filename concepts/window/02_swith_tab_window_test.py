import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class TestSwitchTabOrWindow(unittest.TestCase):
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

    def test_switch_tab_or_window(self):
        # Navigate to the website
        self.driver.get("https://the-internet.herokuapp.com/windows")

        # Get the handle of the parent window
        parent_window = self.driver.current_window_handle
        print(parent_window)

        # Assert that there's only one window handle initially
        self.assertEqual(len(self.driver.window_handles), 1)

        # Click the link to open a new window
        self.driver.find_element(By.XPATH, "//a[text()='Click Here']").click()

        try:
            # Wait for a new window to appear
            WebDriverWait(self.driver, 10).until(EC.number_of_windows_to_be(2))

            # Iterate through all available window handles
            for handle in self.driver.window_handles:

                # Check if the current handle is not the parent window's handle
                if handle != parent_window:

                    # Switch the WebDriver's focus to the new window
                    self.driver.switch_to.window(handle)

                    # Print the handle of the new window
                    print(handle)

                    # Break out of the loop since we've switched to the new window
                    break

            # Wait for the title of the new window
            WebDriverWait(self.driver, 10).until(EC.title_is("New Window"))

            # Close the current window/tab
            self.driver.close()

            # Switch back to the parent window/tab
            self.driver.switch_to.window(parent_window)

            # Print the current window/tab handle (which should now be the parent window)
            print(self.driver.current_window_handle)

        # Handle a TimeoutException if a new window does not open within the expected time
        except TimeoutException:
            print("New window did not open within the expected time.")


if __name__ == "__main__":
    unittest.main()
