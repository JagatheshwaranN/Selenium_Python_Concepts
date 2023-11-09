import base64
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v119.network import Headers


class TestBasicAuth(unittest.TestCase):
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

    async def test_basic_auth(self):
        # Establishes a bidirectional connection with the 'async with' block
        async with self.driver.bidi_connection as connection:

            # Enables the network domain within the Chrome DevTools Protocol using the established connection
            await connection.session.execute(connection.devtools.network.enable())

            # Encodes the "admin:admin" string in base64
            credentials = base64.b64encode("admin:admin".encode()).decode()

            # Sets up the authorization header for the request using the base64-encoded credentials
            auth = {'authorization': 'Basic ' + credentials}

            # Sets extra HTTP headers, including the authorization header, using the established connection
            await connection.session.execute(connection.devtools.network.set_extra_http_headers(Headers(auth)))

        # Access the specified URL using the WebDriver instance
        self.driver.get('https://the-internet.herokuapp.com/basic_auth')

        # Find the element containing the success message
        success = self.driver.find_element(By.TAG_NAME, "p")

        # Assert that the text of the success element matches the expected success message
        assert success.text == 'Congratulations! You must have the proper credentials.'


if __name__ == "__main__":
    unittest.main()
