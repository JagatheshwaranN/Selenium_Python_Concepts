import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestXpathLocatorTypes(unittest.TestCase):
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

    def test_xpath_locator_types(self):
        # Open the Facebook login page
        self.driver.get("https://www.facebook.com/")

        # xpath=//tag[contains(@attribute, value)]
        self.assertTrue(
            self.driver.find_element(By.XPATH, "//input[contains(@data-testid,'royal_email')]").is_displayed())

        # xpath=//tag[@attribute=value or @attribute=value]
        self.assertTrue(self.driver.find_element(By.XPATH, "//input[@type='password' or @name='pass']").is_displayed())

        # xpath=//tag[@attribute=value and @attribute=value]
        self.assertTrue(self.driver.find_element(By.XPATH, "//input[@type='password' and @name='pass']").is_displayed())

        # xpath=//tag[starts-with(@attribute, value)]
        self.assertTrue(self.driver.find_element(By.XPATH, "//input[starts-with(@data-testid,'royal')]").is_displayed())

        # xpath=//tag[text()=value]
        self.assertTrue(self.driver.find_element(By.XPATH,
                                                 "//h2[text()='Facebook helps you connect and share with the people "
                                                 "in your life.']").is_displayed())

        # xpath=//tag[@attribute=value]//following::tag
        self.assertTrue(
            self.driver.find_element(By.XPATH, "//div[@id='passContainer']//following::button").is_displayed())

        # xpath=//tag[@attribute=value]//ancestor::tag
        self.assertTrue(self.driver.find_element(By.XPATH, "//button[@name='login']//ancestor::form").is_displayed())

        # xpath=//tag[@attribute=value]//child::tag[@attribute=value]
        self.assertTrue(self.driver.
                        find_element(By.XPATH,
                                     "//form[@data-testid='royal_login_form']//child::input[@name='email']")
                        .is_displayed())

        # xpath=//tag[@attribute=value]//preceding::tag[@attribute=value]
        self.assertTrue(self.driver.
                        find_element(By.XPATH,
                                     "//button[@name='login']//preceding::input[@name='email']").is_displayed())

        # xpath=//tag[@attribute=value]//following-sibling::tag
        self.assertTrue(
            self.driver.find_element(By.XPATH, "//div[@class='_8esl']//following-sibling::h2").is_displayed())

        # xpath=//tag[@attribute=value]//parent::tag
        self.assertTrue(self.driver.find_element(By.XPATH, "//input[@name='email']//parent::div").is_displayed())

        # xpath=//tag[@attribute=value]//self::same-tag
        self.assertTrue(self.driver.find_element(By.XPATH, "//input[@type='password']//self::input").is_displayed())

        # xpath=//tag[@attribute=value]//descendant::tag[@attribute=value]
        self.assertTrue(self.driver.find_element(By.XPATH,
                                                 "//form[@data-testid='royal_login_form']//descendant::input["
                                                 "@name='email']").is_displayed())


if __name__ == "__main__":
    unittest.main()
