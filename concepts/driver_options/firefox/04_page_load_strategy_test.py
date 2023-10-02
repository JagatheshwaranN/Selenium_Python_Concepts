import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service as FirefoxService


def test_page_load_strategy_firefox():
    # Create an instance of FirefoxOptions to customize Firefox WebDriver's behavior.
    firefox_options = Options()

    # Set the page load strategy to "eager"
    firefox_options.page_load_strategy = "eager"

    # Specify the path for geckodriver log file
    geckodriver_log_path = "geckodriver.log"

    # Create a Firefox service with the log_output option
    service = FirefoxService(log_output=geckodriver_log_path)

    # Create a Firefox WebDriver instance with the specified options
    driver = webdriver.Firefox(options=firefox_options, service=service)

    try:
        # Open the Unsplash website with a specific page
        driver.get("https://unsplash.com/t/people")

        # Assert that the title of the webpage matches the expected title
        assert driver.title == "People | Unsplash"

        # Wait for some time
        wait_some_time()  # This method is used for demo purpose

    finally:
        # Close the Firefox browser
        driver.quit()

        # Close the FirefoxService to release resources and close the log file
        service.stop()


# Define wait_some_time() function here
def wait_some_time():
    # Example: Wait for 5 seconds
    time.sleep(10)
