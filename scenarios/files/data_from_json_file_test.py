import json
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DataFromJsonFileTest(unittest.TestCase):
    # Class variable to hold the WebDriver instance
    driver = None

    @classmethod
    def setUpClass(cls):
        # Create a Chrome WebDriver instance
        cls.driver = webdriver.Chrome()

        # Maximize the browser window for better visibility
        cls.driver.maximize_window()

        # Create a WebDriverWait instance with a timeout of 10 seconds
        cls.wait = WebDriverWait(cls.driver, 10)

    @classmethod
    def tearDownClass(cls):
        # Quit the WebDriver instance after all tests are executed
        cls.driver.quit()

    def test_data_from_json_file(self):
        # Open the specified URL in the browser
        self.driver.get("https://admin-demo.nopcommerce.com/login")

        # Specify the relative path to the JSON file
        file_path = "D:\\Environment_Collection\\Python_Env\\SeleniumPythonConcepts\\scenarios\\files\\data\\user.json"

        # Open and load data from the JSON file
        with open(file_path) as json_file:
            data = json.load(json_file)

        # Iterate through user data obtained from the JSON file
        for user_data in data['userlogin']:
            # Locate the email input element by its ID using Selenium's find_element method
            email = self.driver.find_element(By.ID, 'Email')

            # Locate the password input element by its ID using Selenium's find_element method
            password = self.driver.find_element(By.ID, 'Password')

            # Clear any existing content in the email input field
            email.clear()

            # Enter the email value obtained from the 'user_data' dictionary into the email input field
            email.send_keys(user_data['email'])

            # Clear any existing content in the password input field
            password.clear()

            # Enter the password value obtained from the 'user_data' dictionary into the password input field
            password.send_keys(user_data['password'])

            # Click on the login button
            self.driver.find_element(By.CSS_SELECTOR, '.button-1.login-button').click()

            # Wait for the title to change after successful login
            self.wait.until(EC.title_is('Dashboard / nopCommerce administration'))

            # Assert the title of the resulting page after login
            self.assertEqual(self.driver.title, 'Dashboard / nopCommerce administration')


# Run the tests if the script is executed directly
if __name__ == "__main__":
    unittest.main()
