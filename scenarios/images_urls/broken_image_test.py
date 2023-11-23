import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestBrokenImage(unittest.TestCase):
    # Initialize the driver variable
    driver = None

    @classmethod
    def setUpClass(cls):
        # Initialize Chrome WebDriver
        cls.driver = webdriver.Chrome()

        # Maximize the browser window
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        # Close the driver
        cls.driver.quit()

    def test_broken_image(self):
        # Navigate to the URL "https://demoqa.com/broken"
        self.driver.get("https://demoqa.com/broken")

        # Locate the 'img' element with the 'src' attribute set to '/images/Toolsqa_1.jpg' using XPath
        image = self.driver.find_element(By.XPATH, "//img[@src='/images/Toolsqa_1.jpg']")

        # Check if the 'naturalWidth' attribute of the 'image' WebElement is equal to "0"
        if image.get_attribute("naturalWidth") == "0":
            # If 'naturalWidth' is "0," it indicates that the image is not displayed,
            # so print "Image display Broken"
            print("\nImage display Broken")

        else:
            # If 'naturalWidth' is not "0," it indicates that the image is displayed,
            # so print "Image display Ok"
            print("\nImage display Ok")


if __name__ == "__main__":
    unittest.main()
