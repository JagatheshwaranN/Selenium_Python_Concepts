import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestWebTable(unittest.TestCase):
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

    def test_webtable_type1(self):
        # Navigate to the web page
        self.driver.get("file:///D:/Environment_Collection/Eclipse_Env/Workspace/Selenium_Concepts"
                        "/src/main/resources/supportFiles/WebTable.html")

        # Find the table element by its ID
        table = self.driver.find_element(By.ID, "data-table")

        # Find all the table rows and table cells in the HTML table
        table_rows = table.find_elements(By.TAG_NAME, "tr")
        table_cells = table.find_elements(By.TAG_NAME, "td")

        # Print the number of table rows and table cells
        print(f"\nNumber of table rows: ", len(table_rows))
        print(f"\nNumber of table cells: ", len(table_cells))

        # Iterate through each table row
        for row in table_rows:

            # Check if the row is not None
            if row is not None:

                # Find all the cells within the current row
                row_cells = row.find_elements(By.TAG_NAME, "td")

                # Iterate through each cell in the current row
                for cell in row_cells:

                    # Check if the cell is not None
                    if cell is not None:

                        # Check if the cell text is 'UK'
                        if cell.text == 'UK':

                            # Print the table row data if the cell contains 'UK'
                            print(f"\nTable row data: ", row.text)

                            # Assert that the row text contains 'UK'
                            self.assertIn('UK', row.text, "Text 'UK' not found in row")


if __name__ == "__main__":
    unittest.main()
