from selenium import webdriver


def test_script_wait():
    # Initialize the Chrome WebDriver
    driver = webdriver.Chrome()

    try:
        # Maximize the browser window
        driver.maximize_window()

        # Set the script timeout to 10 seconds
        driver.set_script_timeout(10)

        # Execute a synchronous JavaScript alert
        driver.execute_script("alert('hello world!');")

        # Switch to the alert and accept it
        alert = driver.switch_to.alert
        alert.accept()

        # Execute an asynchronous JavaScript script to delay
        driver.execute_async_script("window.setTimeout(arguments[arguments.length - 1], 500);")

    finally:
        # Close the driver
        driver.close()
