import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestWindowHandles(unittest.TestCase):
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

    def test_get_window_handles(self):
        # Navigate to the website
        self.driver.get("https://the-internet.herokuapp.com/windows")

        # Click the link to open a new window
        self.driver.find_element(By.XPATH, "//a[text()='Click Here']").click()

        # Wait for a new window to appear
        WebDriverWait(self.driver, 10).until(EC.number_of_windows_to_be(2))

        # Get all window handles
        window_handles = self.driver.window_handles

        # Print all window handles
        for handle in window_handles:
            print(f"\n{handle}")

        # Assert that the number of window handles is equal to 2
        assert len(window_handles) == 2


if __name__ == "__main__":
    unittest.main()
