from selenium import webdriver
from selenium.webdriver.edge.options import Options


def test_browser_details():
    # Create an instance of EdgeOptions to customize Edge WebDriver's behavior.
    edge_options = Options()
    
    """
    No direct programmatic confirmation of detachment of the Webdriver instance from Browser
    """
    # Add the "detach" experimental option
    edge_options.add_experimental_option("detach", True)

    # Initialize the Edge WebDriver with the specified options
    driver = webdriver.Chrome(options=edge_options)

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
