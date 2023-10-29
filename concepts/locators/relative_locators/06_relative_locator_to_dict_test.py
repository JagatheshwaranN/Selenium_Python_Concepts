from selenium.webdriver.support import relative_locator as RL
from selenium.webdriver.common.by import By
from selenium import webdriver

"""
Not sure about the exact use-case of the below to_dict() method
"""

# Instantiate a web driver (in this case, Chrome)
driver = webdriver.Chrome()

# Open the Google website
driver.get("https://www.google.com")

# Find the search bar as the base element
base_element = driver.find_element(By.NAME, "q")

# Create a relative locator targeting elements with the tag name 'input'
relative_locator = RL.with_tag_name("input")

# Use the relative locator to find elements relative to the base element
relative_elements = base_element.find_elements(By.NAME, relative_locator)

# Convert the relative locator to a dictionary format
relative_locator_dict = relative_locator.to_dict()

# Display the dictionary format of the relative locator
print(relative_locator_dict)

# Close the web driver
driver.quit()
