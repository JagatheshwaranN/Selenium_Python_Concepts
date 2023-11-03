import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestGetPageText(unittest.TestCase):
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

    def test_get_page_text(self):
        # Navigate to the Google homepage
        self.driver.get("https://www.google.com/")

        # Execute JavaScript code to extract the entire text content of the web page
        value = self.driver.execute_script("return document.documentElement.innerText;")

        # Find the same element again for assertion purposes
        input_element = self.driver.find_element(By.XPATH, "(//a[@class='gb_E'])[1]")

        # Verify whether the extracted text contains the text of the targeted element
        # using the assertTrue method
        self.assertTrue(value.find(input_element.text) != -1)


if __name__ == "__main__":
    unittest.main()
