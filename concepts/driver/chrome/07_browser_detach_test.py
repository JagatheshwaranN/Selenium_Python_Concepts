from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def test_browser_details():
    # Create an instance of ChromeOptions to customize Chrome WebDriver's behavior.
    chrome_options = Options()

    """
    No direct programmatic confirmation of detachment of the Webdriver instance from Browser
    """
    # Add the "detach" experimental option
    chrome_options.add_experimental_option("detach", True)

    # Initialize the Chrome WebDriver with the specified options
    driver = webdriver.Chrome(options=chrome_options)

    try:
        # Maximize the browser window
        driver.maximize_window()

        # Navigate to the Google homepage
        driver.get("https://www.google.com/")

        # Assert that the title of the webpage is "Google"
        assert "Google" in driver.title

    finally:
        # Close the browser
        driver.quit()
