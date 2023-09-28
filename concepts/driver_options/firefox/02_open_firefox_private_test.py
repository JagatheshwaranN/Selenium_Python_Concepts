from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service as FirefoxService


def test_open_firefox_private():
    # Create an instance of FirefoxOptions to customize Firefox WebDriver's behavior.
    firefox_options = Options()

    # Add an argument to FirefoxOptions to start Firefox in private (incognito) mode.
    firefox_options.add_argument("--private")

    # Specify the path for geckodriver log file
    geckodriver_log_path = "geckodriver.log"

    # Create a Firefox service with the log_output option
    service = FirefoxService(log_output=geckodriver_log_path)

    # Create a Firefox WebDriver instance with the configured options and service
    driver = webdriver.Firefox(options=firefox_options, service=service)

    try:
        # Open the Google homepage in the Firefox browser
        driver.get("https://www.google.com/")

        # Assert that the title of the webpage is equal to "Google"
        assert driver.title == "Google"

    finally:
        # Close the Firefox browser
        driver.quit()
