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
        self.driver.get("https://google.com/")

        async with self.driver.bidi_connection() as connection:
            await connection.session.execute(connection.devtools.performance.enable())
            metrics_list = await connection.session.execute(connection.devtools.performance.get_metrics())

        metrics = {metric["name"]: metric["value"] for metric in metrics_list}

        for metric_name, metric_value in metrics.items():
            print(f"{metric_name}: {metric_value}")

        assert metrics['DevToolsCommandDuration'] > 0


if __name__ == "__main__":
    unittest.main()
