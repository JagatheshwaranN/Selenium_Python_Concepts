import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestCSSLocatorTypes(unittest.TestCase):
    # Initialize the driver variable
    driver = None

    @classmethod
    def setUpClass(cls):
        # Initialize the Chrome WebDriver
        cls.driver = webdriver.Chrome()

        # Maximize the browser window
        cls.driver.maximize_window()

    def test_css_locator_types(self):
        # Open the Facebook login page
        self.driver.get("https://www.facebook.com/")

        # css=tag#id
        self.assertTrue(self.driver.find_element(By.CSS_SELECTOR, "input#email").is_displayed())

        # css=tag.class[attribute=value]
        self.assertTrue(self.driver.find_element(By.CSS_SELECTOR, "input.inputtext[name=email]").is_displayed())

        # css=tag[attribute=value]
        self.assertTrue(self.driver.find_element(By.CSS_SELECTOR, "button[name='login']").is_displayed())

        # css=tag.class
        self.assertTrue(self.driver.find_element(By.CSS_SELECTOR, "img.fb_logo._8ilh.img").is_displayed())

        # css=tag[attribute^=value]
        self.assertTrue(self.driver.find_element(By.CSS_SELECTOR, "input[type^='pass']").is_displayed())

        # css=tag[attribute$=value]
        self.assertTrue(self.driver.find_element(By.CSS_SELECTOR, "input[type$='word']").is_displayed())

        # css=tag[attribute*=value]
        self.assertTrue(self.driver.find_element(By.CSS_SELECTOR, "input[type*='swo']").is_displayed())

        # css=parentTag > childTag[attribute=value]
        self.assertTrue(self.driver.find_element(By.CSS_SELECTOR, "div > button[name='login']").is_displayed())

        # css=parentTag > childTag > subChildTag:nth-of-type(index)
        self.assertTrue(
            self.driver.find_element(By.CSS_SELECTOR, "div[id='pageFooter'] > ul > li:nth-of-type(2)").is_displayed())

    @classmethod
    def tearDownClass(cls):
        # Close the driver
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
