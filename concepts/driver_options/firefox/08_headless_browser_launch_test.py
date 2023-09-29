from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service as FirefoxService


def test_headless_browser_launch():
    # Create an instance of FirefoxOptions to customize Firefox WebDriver's behavior.
    firefox_options = Options()

    # Add arguments to enable headless mode
    firefox_options.add_argument("--headless")

    # Specify the path for geckodriver log file
    geckodriver_log_path = "geckodriver.log"

    # Create a Firefox service with the log_output option
    service = FirefoxService(log_output=geckodriver_log_path)

    # Initialize the Firefox WebDriver with the specified options
    driver = webdriver.Chrome(options=firefox_options, service=service)

    try:
        # Navigate to the Google homepage
        driver.get("https://www.google.com/")
        print('\n', 'Navigate to the Google homepage')

        # Assert that the title of the webpage is "Google"
        assert "Google" in driver.title

    finally:
        # Close the Firefox browser
        driver.quit()
