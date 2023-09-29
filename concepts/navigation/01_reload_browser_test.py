import time
from selenium import webdriver


def test_reload_browser():
    # Initialize the Chrome WebDriver
    driver = webdriver.Chrome()

    try:
        # Maximize the browser window
        driver.maximize_window()

        # Navigate to the GitHub homepage
        driver.get("https://github.com/")

        # Wait for some time
        wait_some_time()

        # Refresh the page
        driver.refresh()

        # Wait for some time
        wait_some_time()

        # Assert that the title of the webpage is "GitHub: Let’s build from here · GitHub"
        assert driver.title == 'GitHub: Let’s build from here · GitHub'

    finally:
        # Close the Chrome browser
        driver.quit()


# Define wait_some_time() function here
def wait_some_time():
    # Example: Wait for 5 seconds
    time.sleep(5)
