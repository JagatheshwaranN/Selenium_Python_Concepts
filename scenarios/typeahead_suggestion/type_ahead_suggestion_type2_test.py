import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestTypeAheadSuggestionType2(unittest.TestCase):
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

    def test_type_ahead_suggestion_type2(self):
        # Define input text and suggestion to select
        input_text = 'sca'
        suggestion_to_select = "Scala"

        # Navigate to the webpage
        self.driver.get("http://jqueryui.com/autocomplete/")

        # Switch to the frame containing the autocomplete input
        frame_element = self.driver.find_element(By.CLASS_NAME, "demo-frame")
        self.driver.switch_to.frame(frame_element)

        # Find the search bar element with ID
        search_bar = self.driver.find_element(By.ID, "tags")

        # Iterate through each character in 'input_text'
        for i in range(len(input_text)):
            # Get the current character
            current_char = input_text[i]

            # Send the current character to the search bar
            search_bar.send_keys(str(current_char))

            # Add a delay for UI responsiveness (adjust as needed)
            time.sleep(0.5)  # Waits for 0.5 seconds between each character input

        # Wait for the type-ahead suggestion list to appear
        type_ahead_suggestion = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.ID, "ui-id-1"))
        )

        # Call the method to select a suggestion
        self.select_suggestion(type_ahead_suggestion, suggestion_to_select)

    def select_suggestion(self, element, text):

        # Loop through each suggestion element in the typeAheadSuggestion list.
        for suggestion in element.find_elements(By.TAG_NAME, "li"):

            # Check if the text of the suggestion matches the expected suggestion_to_select.
            if suggestion.text == text:

                # If a match is found, click on the suggestion and exit the loop.
                suggestion.click()

                # Break the loop
                break


if __name__ == "__main__":
    unittest.main()
