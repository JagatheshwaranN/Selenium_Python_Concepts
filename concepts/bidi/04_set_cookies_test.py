import unittest
from selenium import webdriver


class TestSetCookies(unittest.TestCase):
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

    async def test_set_cookies(self):
        # Establishes a bidirectional connection using the 'async with' block
        async with self.driver.bidi_connection() as connection:

            # Sets the cookie using the established connection
            execution = connection.devtools.network.set_cookie(
                name="Test",  # Sets the name of the cookie as "Test"
                value="Automate",  # Assigns the value "Automate" to the cookie
                domain="www.selenium.dev",  # Sets the domain for the cookie as "www.selenium.dev"
                secure=True  # Ensures that the cookie is transmitted securely
            )

        # Executes the defined cookie-setting operation within the established connection session
        await connection.session.execute(execution)

        # Loads the specified URL in the Selenium WebDriver instance
        self.driver.get("https://www.selenium.dev")

        # Retrieves the value of the cookie named "Test" from the current session
        test_cookie = self.driver.get_cookie("Test")

        # Asserts whether the value of the retrieved cookie is "Automate"
        assert test_cookie["value"] == "Automate"


if __name__ == "__main__":
    unittest.main()
