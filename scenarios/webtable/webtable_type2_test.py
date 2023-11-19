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

    def test_webtable_type2(self):
        # Navigate to the web page
        self.driver.get("file:///D:/Environment_Collection/Eclipse_Env/Workspace/Selenium_Concepts"
                        "/src/main/resources/supportFiles/WebTable.html")

        # Find the table element by ID
        table = self.driver.find_element(By.ID, "data-table")

        # Get all the rows from the table
        table_rows = table.find_elements(By.TAG_NAME, "tr")

        # Calculate the number of rows (excluding the header)
        rows = len(table_rows) - 1

        # Print the number of table rows
        print(f"\n Number of table rows: ", rows)

        # Iterate through each row (excluding the header)
        for row in range(rows):

            # Find all the cells within the current row
            row_cells = table_rows[row].find_elements(By.TAG_NAME, "td")

            # Calculate the number of cells in the current row
            cells = len(row_cells)

            # Iterate through each cell in the current row
            for cell in range(cells):

                # Get the text content of the cell
                cell_data = row_cells[cell].text

                # Check if the cell contains "UK"
                if "UK" in cell_data:

                    # Print the cell details if it contains "UK"
                    print(f"Table cell with '{cell_data}' found in row {row} and column {cell}")

                    # Assert that the cell data contains 'UK'
                    self.assertTrue("UK" in cell_data, "Cell data does not contain 'UK'")


if __name__ == "__main__":
    unittest.main()
