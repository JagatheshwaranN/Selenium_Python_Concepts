from selenium import webdriver
from selenium.common.exceptions import WebDriverException

# List of browser names and their corresponding webdriver classes
browsers = {
    "Chrome": webdriver.Chrome,
    "Edge": webdriver.Edge,
    "Firefox": webdriver.Firefox
}

for browser_name, driver_class in browsers.items():
    # Initialize the driver variable outside the try block
    driver = None
    try:
        # Create a webdriver instance for the current browser
        driver = driver_class()

        # Maximize the browser window
        driver.maximize_window()

        # Open the Google homepage in the current browser
        driver.get("https://www.google.com/")

        # Get the title of the webpage and store it in the 'title' variable
        title = driver.title

        # Assert that the title of the webpage is equal to "Google"
        assert title == "Google"

    except WebDriverException as wde:
        # Handle exceptions related to the webdriver
        print(f"Error with {browser_name} : {wde}")

    except AssertionError as ae:
        # Handle assertion errors (title not equal to "Google")
        print(f"Title mismatch for {browser_name}")

    finally:
        # Close the current browser, even if an exception occurs
        driver.quit()
