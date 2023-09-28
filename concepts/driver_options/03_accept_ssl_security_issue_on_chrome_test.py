import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def test_accept_ssl_security_issue_on_chrome():
    # Create a ChromeOptions object to configure Chrome driver options
    chrome_options = Options()

    # Set the 'accept_insecure_certs' option to True to accept insecure SSL certificates
    chrome_options.accept_insecure_certs = True

    # Create a Chrome WebDriver instance with the configured options
    driver = webdriver.Chrome(options=chrome_options)

    try:
        # Maximize the browser window
        driver.maximize_window()

        # Open a website with an untrusted SSL certificate
        driver.get("https://untrusted-root.badssl.com/")

        # Assert that the title of the webpage matches the expected title
        assert driver.title == "untrusted-root.badssl.com"

        # Wait for some time
        wait_some_time()

    finally:
        # Close the Chrome browser
        driver.quit()


# Define wait_some_time() function here
def wait_some_time():
    # Example: Wait for 5 seconds
    time.sleep(5)