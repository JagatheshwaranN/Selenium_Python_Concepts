import base64
import os.path
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.print_page_options import PrintOptions


class TestPrintPage(unittest.TestCase):
    # Create an instance of ChromeOptions to customize Chrome WebDriver's behavior.
    chrome_options = Options()

    # Add arguments to enable headless mode
    chrome_options.add_argument("--headless")

    # Initialize the Chrome WebDriver with the specified options
    driver = webdriver.Chrome(options=chrome_options)

    # Maximize the browser window (note that this may not work in headless mode)
    driver.maximize_window()

    def test_print_page(self):
        # Navigate to the website
        self.driver.get("http://www.example.com")

        # Create an instance of PrintOptions
        print_options = PrintOptions()

        # Set the page ranges to be printed
        print_options.page_ranges = ['1']

        # Get the PDF content in base64 encoded format from the print_page method
        pdf_base64 = self.driver.print_page(print_options)

        # Write the base64 encoded content as bytes to a file named 'print.pdf'
        with open("print.pdf", "wb") as file:
            # Decode the base64 encoded content and write it to the file
            file.write(base64.b64decode(pdf_base64))

            # Close the file
            file.close()

        # Assert that the 'print.pdf' file exists
        assert os.path.exists("print.pdf")


if __name__ == "__main__":
    unittest.main()
