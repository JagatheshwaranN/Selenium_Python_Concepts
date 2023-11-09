import unittest
from selenium import webdriver

"""
Print Statements will not print

The reason why the print statements are not being printed in the PyCharm IDE is because the code 
is using asynchronous programming with the `async` and `await` keywords. When you run the code in
the IDE, the print statements are executed before the asynchronous code has a chance to finish, 
so the output is not displayed.

To see the output of the print statements, you can run the code using an asynchronous framework
like asyncio. For example, you can save the code as a standalone script (e.g., `performance.py`)
and then run it using the following command:

```
python -m asyncio performance.py
```
This will execute the code in an asynchronous environment and allow the print statements to be displayed.
"""


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
