from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def test_open_chrome_incognito():
    # Create an instance of ChromeOptions to customize Chrome WebDriver's behavior.
    chrome_options = Options()

    # Add an argument to ChromeOptions to start the Chrome browser in incognito mode.
    chrome_options.add_argument("--incognito")

    # Create a new instance of the Chrome WebDriver with the specified options.
    driver = webdriver.Chrome(options=chrome_options)

    try:
        # Maximize the browser window
        driver.maximize_window()

        # Open the Google homepage in the Chrome browser
        driver.get("https://www.google.com/")

        # Assert that the title of the webpage is equal to "Google"
        assert driver.title == "Google"

    finally:
        # Close the Chrome browser
        driver.quit()
