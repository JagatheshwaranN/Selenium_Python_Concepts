from selenium import webdriver
from selenium.webdriver.edge.options import Options


def test_browser_details():
    # Create an instance of EdgeOptions to customize Edge WebDriver's behavior.
    edge_options = Options()

    # Initialize the Edge WebDriver with the specified options
    driver = webdriver.Edge(options=edge_options)

    try:
        # Maximize the browser window
        driver.maximize_window()

        # Navigate to the Google homepage
        driver.get("https://www.google.com/")

        # Obtain browser details using Capabilities
        capabilities = driver.capabilities

        # Obtain the browser name
        browser_name = capabilities['browserName']
        print("Browser Name: ", browser_name)

        # Obtain the browser version
        browser_version = capabilities['browserVersion']
        print("Browser Version: ", browser_version)

        # Assert that the title of the webpage is "Google"
        assert "Google" in driver.title

    finally:
        # Close the browser
        driver.quit()
