import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestScrollPageRight(unittest.TestCase):
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

    def test_scroll_page_right(self):
        # Load a local HTML file with a horizontal scroll
        self.driver.get("file:///D:/Environment_Collection/Intellij_Env/Selenium_Concepts/"
                        "src/main/resources/supportFiles/HorizontalScroll.html")

        # Create a JavaScript Executor instance
        js_executor = self.driver.execute_script

        '''
        Another way to achieve page right scrolling
        ==========================================
        # js_executor("window.scrollTo({ right: document.body.scrollWidth, behavior: 'auto' })")
        '''

        # Scroll the window to the extreme right of the page
        js_executor("window.scrollTo(document.body.scrollWidth, 0)")

        # Wait for a while to ensure the scroll action completes (optional)
        time.sleep(2)

        # Locate the desired element, "Item 5", within the horizontal scrolling content
        item_section = self.driver.find_element(By.XPATH, "//div[@class='scroll-item'][text()='Item 5']")

        # Verify that the element is visible within the viewport after scrolling
        assert self.in_viewport(item_section)

    def in_viewport(self, element):
        # JavaScript code to determine if the element is within the viewport
        script = (
            "for(var e=arguments[0],f=e.offsetTop,t=e.offsetLeft,o=e.offsetWidth,n=e.offsetHeight;\n"
            "e.offsetParent;)f+=(e=e.offsetParent).offsetTop,t+=e.offsetLeft;\n"
            "return f<window.pageYOffset+window.innerHeight&&t<window.pageXOffset+window.innerWidth&&f+n>\n"
            "window.pageYOffset&&t+o>window.pageXOffset"
        )
        # Executing the JavaScript script to determine if the element is within the viewport
        return self.driver.execute_script(script, element)


if __name__ == "__main__":
    unittest.main()
