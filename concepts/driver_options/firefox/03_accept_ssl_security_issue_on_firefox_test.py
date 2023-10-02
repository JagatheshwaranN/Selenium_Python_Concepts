import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service as FirefoxService


def test_accept_ssl_security_issue_on_firefox():
    # Create a FirefoxOptions object to configure Firefox driver options
    firefox_options = Options()

    # Set the 'accept_insecure_certs' option to True to accept insecure SSL certificates
    firefox_options.accept_insecure_certs = True
    """
     Warning: DeprecationWarning: Firefox will soon stop logging to geckodriver.log by default;
     Specify desired logs with log_output
     self.service = service if service else Service()
    """
    # Specify the path for geckodriver log file
    geckodriver_log_path = "geckodriver.log"

    # Create a Firefox service with the log_output option
    service = FirefoxService(log_output=geckodriver_log_path)

    # Create a Firefox WebDriver instance with the configured options and service
    driver = webdriver.Firefox(options=firefox_options, service=service)

    try:
        # Maximize the browser window
        # driver.maximize_window() - By default Firefox open in maximized mode

        # Open a website with an untrusted SSL certificate
        driver.get("https://untrusted-root.badssl.com/")

        # Assert that the title of the webpage matches the expected title
        assert driver.title == "untrusted-root.badssl.com"

        # Wait for some time
        wait_some_time()

    finally:
        # Close the Firefox browser
        driver.quit()

        # Close the FirefoxService to release resources and close the log file
        service.stop()


# Define wait_some_time() function here
def wait_some_time():
    # Example: Wait for 5 seconds
    time.sleep(5)
