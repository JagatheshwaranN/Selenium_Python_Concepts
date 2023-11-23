import unittest
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestBrokenLinksTest(unittest.TestCase):
    # Initialize the driver variable
    driver = None

    @classmethod
    def setUpClass(cls):
        # Initialize Chrome WebDriver
        cls.driver = webdriver.Chrome()

        # Maximize the browser window
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        # Close the driver
        cls.driver.quit()

    def test_broken_links_type2(self):
        # Navigate to the newtours website
        self.driver.get("http://demo.guru99.com/test/newtours/")

        # Find all the anchor (<a>) elements on the web page and store them in a list named 'links'
        links = self.driver.find_elements(By.TAG_NAME, "a")

        # Iterate through each 'link' WebElement in the 'links' list
        for link in links:

            # Get the value of the "href" attribute for the current 'link' WebElement
            href = link.get_attribute("href")

            # Check if the link is valid
            if self.is_valid_link(href):
                print(href + " - Active Link")

            else:
                print(href + " - Broken Link")

    def is_valid_link(self, link):
        try:
            # Send a HEAD request to the URL to check if it's valid
            response = requests.head(link, timeout=30)

            # If the status code is 200, the link is valid
            if response.status_code == 200:
                return True

            # If the status code is not 200, the link is broken
            else:
                print("Broken Link Status Code:", response.status_code)
                return False

        except requests.exceptions.RequestException:
            # Handle exceptions by printing the error message
            print("Error checking link:", link)
            return False


if __name__ == "__main__":
    unittest.main()
