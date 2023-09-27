import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def test_open_maximized_browser():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=chrome_options)

    try:
        # Open the Google homepage in the Chrome browser
        driver.get("https://www.google.com/")

        # Assert that the title of the webpage is equal to "Google"
        assert driver.title == "Google"

        # Wait for some time
        wait_some_time()

    finally:
        # Close the Chrome browser
        driver.quit()


# Define your wait_some_dime() function here
def wait_some_time():
    # Example: Wait for 5 seconds
    time.sleep(5)
