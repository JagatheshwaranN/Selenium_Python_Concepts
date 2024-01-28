import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import xml.etree.ElementTree as ET


class DataFromXmlFileTest(unittest.TestCase):
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

    def test_data_from_xml_file(self):
        # Load user data from the XML file using the load_data_from_xml_file method
        user_data_list = self.load_data_from_xml_file()

        # Iterate through user data obtained from the XML file
        for user_data in user_data_list:

            # Open the specified URL in the browser
            self.driver.get("https://admin-demo.nopcommerce.com/login")

            # Locate the email input element by its ID using Selenium's find_element method
            email = self.driver.find_element(By.ID, 'Email')

            # Locate the password input element by its ID using Selenium's find_element method
            password = self.driver.find_element(By.ID, 'Password')

            # Clear any existing content in the email input field
            email.clear()

            # Input the value from the first element of the user_data tuple into the email input field
            email.send_keys(user_data[0])

            # Clear any existing content in the password input field
            password.clear()

            # Input the value from the second element of the user_data tuple into the password input field
            password.send_keys(user_data[1])

            # Click on the login button
            self.driver.find_element(By.CSS_SELECTOR, '.button-1.login-button').click()

            # Wait for the title to change after successful login
            self.wait.until(EC.title_is('Dashboard / nopCommerce administration'))

            # Assert the title of the resulting page after login
            self.assertEqual(self.driver.title, 'Dashboard / nopCommerce administration')

    def load_data_from_xml_file(self):
        # Specify the path to the properties file
        file_path = "D:\\Environment_Collection\\Python_Env\\SeleniumPythonConcepts\\scenarios\\" \
                    "files\\data\\user.xml"

        # Parse the XML file using ElementTree
        tree = ET.parse(file_path)

        # Get the root element of the XML file
        root = tree.getroot()

        # Initialize an empty list to store user data
        user_data = []

        # Iterate through 'userlogin' elements in the XML file
        for user_login in root.findall('userlogin'):

            # Extract email value from 'email' tag inside the current 'userlogin' element
            email = user_login.find('email').text

            # Extract password value from 'password' tag inside the current 'userlogin' element
            password = user_login.find('password').text

            # Append a tuple containing email and password to the user_data list
            user_data.append((email, password))

        # Return the list containing user data extracted from the XML file
        return user_data


# Run the tests if the script is executed directly
if __name__ == "__main__":
    unittest.main()



