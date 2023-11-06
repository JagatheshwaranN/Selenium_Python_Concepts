import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener


class WebDriverEventListener(AbstractEventListener):
    def before_navigate_to(self, url: str, driver):
        # Print before navigating to a new URL
        print(f"Before performing the BeforeNavigateTo with driver {url}")

    def after_navigate_to(self, url: str, driver):
        # Print after navigating to a new URL
        print(f"After performing the AfterNavigateTo with driver {url}")

    def before_find(self, by, value, driver):
        # Print before finding an element
        print(f"Before performing the BeforeFind with driver {by}, {value}")

    def after_find(self, by, value, driver):
        # Print after finding an element
        print(f"After performing the AfterFind with driver {by}, {value}")

    def before_click(self, element, driver):
        # Print before clicking an element
        print(f"Before performing the BeforeClick with driver {element}")

    def after_click(self, element, driver):
        # Print after clicking an element
        print(f"After performing the AfterClick with driver {element}")

    def before_close(self, driver):
        # Print before closing the driver
        print(f"Before performing the BeforeClose with driver {driver}")

    def after_close(self, driver):
        # Print after closing the driver
        print(f"After performing the AfterClose with driver {driver}")


class TestWebDriverEvents(unittest.TestCase):
    # Initialize the driver variable
    driver = None

    @classmethod
    def setUpClass(cls):
        # Initialize the Chrome WebDriver
        original = webdriver.Chrome()

        # Create an instance of the custom event listener
        listener = WebDriverEventListener()

        # Create an EventFiringWebDriver with the original driver and the custom event listener
        cls.driver = EventFiringWebDriver(original, listener)

        # Maximize the window
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        # Close the driver
        cls.driver.close()

    def test_browser_events(self):
        # Access the specified URL
        self.driver.get("https://admin-demo.nopcommerce.com/login")

        # Retrieve and print the current URL
        url = self.driver.current_url
        print(f"Current Url : ", url)

        # Find the email field and perform clearing and sending keys operations
        email_field = self.driver.find_element(By.ID, "Email")
        email_field.clear()
        email_field.send_keys("admin@yourstore.com")

        # Find the password field and perform clearing and sending keys operations
        password_field = self.driver.find_element(By.ID, "Password")
        password_field.clear()
        password_field.send_keys("admin")

        # Find and click the login button
        self.driver.find_element(By.XPATH, "//button[text()='Log in']").click()

        # Retrieve and print the current title of the page
        title = self.driver.title
        print(f"Title : ", title)


if __name__ == "__main__":
    unittest.main()
