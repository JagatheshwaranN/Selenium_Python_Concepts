from selenium import webdriver
from selenium.webdriver.edge.options import Options


def test_open_edge_private():
    # Create an instance of EdgeOptions to customize Edge WebDriver's behavior.
    edge_options = Options()

    # Add an argument to EdgeOptions to start the Edge browser in InPrivate mode.
    edge_options.use_chromium = True  # Use Chromium-based Edge
    edge_options.add_argument("--inprivate")

    # Create a new instance of the Edge WebDriver with the specified options.
    driver = webdriver.Edge(options=edge_options)

    try:
        # Maximize the browser window
        driver.maximize_window()

        # Open the Google homepage in the Edge browser
        driver.get("https://www.google.com/")

        # Assert that the title of the webpage is equal to "Google"
        assert driver.title == "Google"

    finally:
        # Close the Edge browser
        driver.quit()
