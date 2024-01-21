import unittest

import pytesseract
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PIL import Image
import sys
sys.stdout = sys.__stdout__
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Adjust path as needed


class TestTextCaptcha(unittest.TestCase):
    driver = None

    WAIT_TIMEOUT = 10

    @classmethod
    def setUpClass(cls):
        # Create ChromeOptions object to configure Chrome WebDriver settings
        chrome_options = Options()

        # Add arguments to ChromeOptions (commented out for disabling notifications)
        # chrome_options.add_argument("--disable-notifications")

        # Create dictionary to store Chrome preferences
        preferences = {
            'profile.default_content_setting_values.notifications': 2
        }

        # Set preferences to disable notifications
        chrome_options.add_experimental_option('prefs', preferences)

        # Initialize ChromeDriver with configured options
        cls.driver = webdriver.Chrome(options=chrome_options)

        # Maximize the browser window
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        # Close the driver
        cls.driver.quit()

    def test_text_captcha(self):
        # Create a WebDriverWait instance with a timeout of 10 seconds
        wait = WebDriverWait(self.driver, self.WAIT_TIMEOUT)

        # Navigate to the IRCTC website
        self.driver.get("https://www.irctc.co.in/nget/train-search")

        # Wait for the login link to be visible and click it
        login_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[normalize-space()='LOGIN']")))
        login_link.click()

        # Wait for the login modal to be visible
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='modal-content']")))

        # Locate the CAPTCHA image and wait for it to be visible
        captcha_img = wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@class='captcha-img']")))

        # Take a screenshot of the CAPTCHA image
        captcha_img.screenshot("captcha_screenshot.png")

        try:
            # Extract text from the CAPTCHA image using Tesseract
            captcha_text = pytesseract.image_to_string(Image.open("captcha_screenshot.png")).strip()

            # Print the extracted CAPTCHA text
            print("Extracted CAPTCHA text: ", captcha_text)

            # Flush the stdout to ensure the print statement is immediately visible in the console
            sys.stdout.flush()

            # Find the input field for captcha by its ID using WebDriver
            captcha_input = self.driver.find_element(By.ID, "captcha")

            # Enter the extracted captcha content into the input field
            captcha_input.send_keys(captcha_text)

            # Retrieve the entered captcha text from the input field
            entered_captcha = captcha_input.get_attribute("value")

            # Assert if the entered captcha matches the extracted captcha content
            self.assertEqual(entered_captcha, captcha_text)

        except Exception as e:
            # If an exception occurs during OCR or input, raise a RuntimeError
            raise RuntimeError(e)


if __name__ == "__main__":
    unittest.main()
