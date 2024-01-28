import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DataFromPropertyFileTest(unittest.TestCase):
    # Class variable to hold the WebDriver instance
    driver = None

    # Class variable to hold the properties instance
    properties = None

    @classmethod
    def setUpClass(cls):
        # Create a Chrome WebDriver instance
        cls.driver = webdriver.Chrome()

        # Maximize the browser window for better visibility
        cls.driver.maximize_window()

        # Create a WebDriverWait instance with a timeout of 10 seconds
        cls.wait = WebDriverWait(cls.driver, 10)

        # Initialize a dictionary to store properties
        cls.properties = {}

        # Load properties from the property file using the 'load_property_file' method
        cls.load_property_file()

    @classmethod
    def tearDownClass(cls):
        # Quit the WebDriver instance after all tests are executed
        cls.driver.quit()

    def test_data_from_property_file(self):
        # Open the specified URL in the browser
        self.driver.get("https://admin-demo.nopcommerce.com/login")

        # Locate the email input element by its ID using Selenium's find_element method
        email = self.driver.find_element(By.ID, 'Email')

        # Locate the password input element by its ID using Selenium's find_element method
        password = self.driver.find_element(By.ID, 'Password')

        # Clear any existing content in the email input field
        email.clear()

        # Retrieve email value from the property file using the 'get_data_from_prop_file' method
        # and input it into the email input field using Selenium's 'send_keys' method
        email.send_keys(self.get_data_from_prop_file("email"))

        # Clear any existing content in the password input field
        password.clear()

        # Retrieve password value from the property file using the 'get_data_from_prop_file' method
        # and input it into the password input field using Selenium's 'send_keys' method
        password.send_keys(self.get_data_from_prop_file("password"))

        # Click on the login button
        self.driver.find_element(By.CSS_SELECTOR, '.button-1.login-button').click()

        # Wait for the title to change after successful login
        self.wait.until(EC.title_is('Dashboard / nopCommerce administration'))

        # Assert the title of the resulting page after login
        self.assertEqual(self.driver.title, 'Dashboard / nopCommerce administration')

    @classmethod
    def load_property_file(cls):
        # Specify the path to the properties file
        file_path = "D:\\Environment_Collection\\Python_Env\\SeleniumPythonConcepts\\scenarios\\" \
                    "files\\data\\user.properties"

        # Open the properties file in read mode using 'with' statement
        with open(file_path, 'r') as file:

            # Iterate through each line in the file
            for line in file:

                # Check if the line contains the equal sign, indicating a key-value pair
                if "=" in line:

                    # Split the line into key and value using the equal sign
                    key, value = line.strip().split("=")

                    # Store the key-value pair in the properties dictionary
                    cls.properties[key] = value
                else:
                    # Print a warning if the line does not contain a valid key-value pair
                    print(f"Warning: Line skipped as it does not contain a valid key-value pair: {line}")

    def get_data_from_prop_file(self, key):
        # Retrieve the value associated with the specified key from the properties dictionary
        # If the key is not found, return an empty string
        value = self.properties.get(key, "")

        # Remove any leading or trailing whitespaces from the retrieved value
        return value.strip()


# Run the tests if the script is executed directly
if __name__ == "__main__":
    unittest.main()
