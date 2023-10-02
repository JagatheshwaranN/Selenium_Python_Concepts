import time
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service as FirefoxService


def test_wait_timeout():
    # Create an instance of FirefoxOptions to customize Firefox WebDriver's behavior.
    firefox_options = Options()

    # Set the implicit wait timeout and script timeout using FirefoxOptions
    firefox_options.add_argument("--implicit-wait=10")
    firefox_options.add_argument("--script-timeout=10")

    # Specify the path for geckodriver log file
    geckodriver_log_path = "geckodriver.log"

    # Create a Firefox service with the log_output option
    service = FirefoxService(log_output=geckodriver_log_path)

    # Create a Firefox WebDriver instance with the specified options
    driver = webdriver.Firefox(options=firefox_options, service=service)

    try:
        # Set the page load timeout to 10 seconds
        driver.set_page_load_timeout(10)

        # Open a local HTML file with a button to load content dynamically
        driver.get("file:///D:/Environment_Collection/Eclipse_Env/Workspace/Selenium_Concepts/src/main/resources"
                   "/supportFiles/SiteLoadDelay.html")

        # Click the button to load content dynamically
        load_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@onclick='load()']")))
        load_button.click()

        # Wait for an element with the specified CSS selector to be displayed
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".light-mode-item.navbar-brand-item")))

        # Wait for some time
        wait_some_time()

        # Assert that the title of the webpage matches the expected title
        assert driver.title == "Online Courses and eBooks Library | Tutorialspoint"

    except TimeoutException as te:
        # Handle the TimeoutException if the page load exceeds the specified timeout
        print("Page load timed out:", te)

    finally:
        # Close the Firefox browser
        driver.quit()

        # Close the FirefoxService to release resources and close the log file
        service.stop()

# Define wait_some_time() function here
def wait_some_time():
    # Example: Wait for 5 seconds
    time.sleep(5)
