import unittest
import urllib.request
from urllib.error import HTTPError, URLError
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

    def test_broken_links(self):
        # Navigate to the newtours website
        self.driver.get("http://demo.guru99.com/test/newtours/")

        # Find all the anchor (<a>) elements on the web page and store them in a list named 'links'
        links = self.driver.find_elements(By.TAG_NAME, "a")

        # Iterate through each 'link' WebElement in the 'links' list
        for link in links:

            # Get the value of the "href" attribute for the current 'link' WebElement
            href = link.get_attribute("href")

            # Call the 'verify_link' method to verify the validity of the 'href' attribute value
            self.verify_link(href)

    def verify_link(self, link):
        try:
            # Open the URL and create an HTTP connection
            connection = urllib.request.urlopen(link)

            # Get the HTTP response code
            response_code = connection.getcode()

            # Print the link
            print(link)

            # Check the response code to determine if the link is broken or active
            if response_code != 200:

                # If the response code is not 200, it indicates a broken link
                print(f"Broken Link Http Request Status => {response_code}")
                print(f"Broken Link Http Request Body ===> {connection.msg}")

            else:
                # If the response code is 200, it indicates an active link
                print(f"Active Link Http Request Status => {response_code}")
                print(f"Active Link Http Request Body ===> {connection.msg}")

        except HTTPError as e:
            # Handle HTTPError by printing the status code and message
            print(f"Broken Link Http Request Status => {e.code}")
            print(f"Broken Link Http Request Body ===> {e.reason}")

        except URLError as e:
            # Handle URLError by printing the reason
            print(f"URL Error: {e.reason}")


if __name__ == "__main__":
    unittest.main()
