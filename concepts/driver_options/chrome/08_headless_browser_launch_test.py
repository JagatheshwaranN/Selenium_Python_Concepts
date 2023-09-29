from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def test_headless_browser_launch():
    # Create an instance of ChromeOptions to customize Chrome WebDriver's behavior.
    chrome_options = Options()

    # Add arguments to enable headless mode
    chrome_options.add_argument("--headless")

    # Initialize the Chrome WebDriver with the specified options
    driver = webdriver.Chrome(options=chrome_options)

    try:
        # Maximize the browser window (note that this may not work in headless mode)
        driver.maximize_window()
        print('Browser window maximized')

        # Navigate to the Google homepage
        driver.get("https://www.google.com/")
        print('Navigate to the Google homepage')

        # Assert that the title of the webpage is "Google"
        assert "Google" in driver.title

    finally:
        # Close the Chrome browser
        driver.quit()
