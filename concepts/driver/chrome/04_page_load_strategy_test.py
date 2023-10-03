import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def test_page_load_strategy():
    # Create an instance of ChromeOptions to customize Chrome WebDriver's behavior.
    chrome_options = Options()

    # Set the page load strategy to "eager" (PageLoadStrategy.EAGER)
    chrome_options.add_argument("--pageLoadStrategy=eager")

    # Create a Chrome WebDriver instance with the specified options
    driver = webdriver.Chrome(options=chrome_options)

    try:
        # Maximize the browser window
        driver.maximize_window()

        # Open the Unsplash website with a specific page
        driver.get("https://unsplash.com/t/people")

        # Assert that the title of the webpage matches the expected title
        assert driver.title == "People | Unsplash"

        # Wait for some time
        wait_some_time()  # This method is used for demo purpose

    finally:
        driver.quit()


# Define wait_some_time() function here
def wait_some_time():
    # Example: Wait for 5 seconds
    time.sleep(10)
