from selenium import webdriver
from selenium.webdriver.edge.options import Options


def test_headless_browser_launch():
    # Create an instance of EdgeOptions to customize Edge WebDriver's behavior.
    edge_options = Options()

    # Add arguments to enable headless mode
    edge_options.add_argument("--headless")

    # Initialize the Edge WebDriver with the specified options
    driver = webdriver.Chrome(options=edge_options)

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
