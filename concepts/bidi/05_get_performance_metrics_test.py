import unittest
from selenium import webdriver


class TestGetPerformanceMetrics(unittest.TestCase):
    # Initialize the driver variable
    driver = None

    @classmethod
    def setUpClass(cls):
        # Initialize the Chrome WebDriver
        cls.driver = webdriver.Chrome()

        # Maximize the browser window
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        # Close the driver
        cls.driver.quit()

    async def test_get_performance_metrics(self):
        # Loads the specified URL in the Selenium WebDriver instance to open a web page
        self.driver.get("https://google.com/")

        # Establishes a bidirectional communication channel between the Selenium WebDriver instance
        # and the Chrome DevTools using the 'async with' block
        async with self.driver.bidi_connection() as connection:

            # Enables the performance domain within the Chrome DevTools Protocol using the established
            # connection to access performance-related information
            await connection.session.execute(connection.devtools.performance.enable())

            # Retrieves a list of performance metrics using the established connection to gather
            # performance data
            metrics_list = await connection.session.execute(connection.devtools.performance.get_metrics())

        # Creates a dictionary by mapping each metric name to its corresponding value
        # from the retrieved metrics list to organize the performance data
        metrics = {metric["name"]: metric["value"] for metric in metrics_list}

        # Prints each metric name and its corresponding value to display the performance data
        for metric_name, metric_value in metrics.items():
            print(f"{metric_name}: {metric_value}")

        # Asserts that the 'DevToolsCommandDuration' metric value is greater than 0 to verify
        # that performance measurements were taken
        assert metrics['DevToolsCommandDuration'] > 0


if __name__ == "__main__":
    unittest.main()
