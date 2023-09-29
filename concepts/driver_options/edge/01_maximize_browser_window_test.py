import time
from selenium import webdriver
from selenium.webdriver.edge.options import Options


def test_open_maximized_browser():
    # Create an instance of EdgeOptions to customize Edge WebDriver's behavior.
    chrome_options = Options()

    # Add an argument to EdgeOptions to start the Edge browser in maximized mode.
    chrome_options.add_argument("--start-maximized")

    # Create a new instance of the Edge WebDriver with the specified options.
    driver = webdriver.Chrome(options=chrome_options)

    try:
        # Open the Google homepage in the Edge browser
        driver.get("https://www.google.com/")

        # Assert that the title of the webpage is equal to "Google"
        assert driver.title == "Google"

        # Wait for some time
        wait_some_time()

    finally:
        # Close the Edge browser
        driver.quit()


# Define wait_some_time() function here
def wait_some_time():
    # Example: Wait for 5 seconds
    time.sleep(5)
