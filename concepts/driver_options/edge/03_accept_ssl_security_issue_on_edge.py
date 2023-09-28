import time
from selenium import webdriver
from selenium.webdriver.edge.options import Options


def test_accept_ssl_security_issue_on_edge():
    # Create an EdgeOptions object to configure Edge driver options
    edge_options = Options()

    # Set the 'accept_insecure_certs' option to True to accept insecure SSL certificates
    edge_options.use_chromium = True  # Use Chromium-based Edge
    edge_options.accept_insecure_certs = True

    # Create an Edge WebDriver instance with the configured options
    driver = webdriver.Edge(options=edge_options)

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

