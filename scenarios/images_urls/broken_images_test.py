import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestBrokenImages(unittest.TestCase):
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

    def test_broken_images(self):
        # Navigate to the URL "https://demoqa.com/broken"
        self.driver.get("https://demoqa.com/broken")

        # Find all the 'img' elements on the web page and store them in a list named 'images'
        images = self.driver.find_elements(By.TAG_NAME, "img")

        # Iterate through a list of WebElements named 'images'
        for image in images:

            try:
                # Use JavaScriptExecutor to check if an image is displayed
                image_display = self.driver.execute_script(
                    '''
                    return (typeof arguments[0].naturalWidth !== 'undefined' && arguments[0].naturalWidth > 0);
                    ''', image)

                # Check the result of the JavaScript execution
                if image_display:
                    # If the image is displayed (naturalWidth > 0), print "Image display Ok"
                    print("Image display Ok")

                else:
                    # If the image is not displayed (naturalWidth <= 0), print "Image display Broken"
                    print("Image display Broken")

            except Exception as ex:
                # Catch and print any exceptions that may occur during the process
                print(ex)


if __name__ == "__main__":
    unittest.main()
