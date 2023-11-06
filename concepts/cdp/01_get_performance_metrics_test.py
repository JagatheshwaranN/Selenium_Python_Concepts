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

    def test_get_performance_metrics(self):
        # Navigate to the Google website
        self.driver.get("https://google.com/")

        # Enable the Performance domain in Chrome DevTools Protocol
        self.driver.execute_cdp_cmd('Performance.enable', {})

        # Get performance metrics from the Performance domain
        metrics_list = self.driver.execute_cdp_cmd('Performance.getMetrics', {})["metrics"]

        # Create a dictionary of metric names and their corresponding values
        metrics = {metric["name"]: metric["value"] for metric in metrics_list}

        # Print each metric name and its value
        for metric_name, metric_value in metrics.items():
            print(f"{metric_name} : {metric_value}")

        # Assert that the 'DevToolsCommandDuration' metric value is greater than 0
        assert metrics["DevToolsCommandDuration"] > 0


if __name__ == "__main__":
    unittest.main()
