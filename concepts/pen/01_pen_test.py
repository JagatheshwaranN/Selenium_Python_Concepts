import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.action_chains import ActionBuilder
from selenium.webdriver.common.actions.interaction import POINTER_PEN
from selenium.webdriver.common.actions.pointer_input import PointerInput


class TestSimulatePenAction(unittest.TestCase):
    # Initialize the driver variable
    driver = None

    @classmethod
    def setUp(cls):
        # Initialize the Chrome WebDriver
        cls.driver = webdriver.Chrome()

        # Maximize the browser window
        cls.driver.maximize_window()

    @classmethod
    def tearDown(cls):
        # Close the driver
        cls.driver.quit()

    def test_simulate_pen_action(self):
        self.driver.get("https://www.selenium.dev/selenium/web/pointerActionsPage.html")

        pointer_area = self.driver.find_element(By.ID, "pointerArea")

        pen_input = PointerInput(POINTER_PEN, "default pen")

        self.actions = ActionBuilder(self.driver, mouse=pen_input)

        self.actions.pointer_action.move_to(pointer_area) \
            .pointer_down().move_by(2, 2).pointer_up()

        self.actions.perform()

        moves = self.driver.find_elements(By.CLASS_NAME, "pointerMove")

        move_to = self.properties(moves[0])

        pointer_down = self.driver.find_element(By.CLASS_NAME, "pointerdown")

        down = self.properties(pointer_down)

        move_by = self.properties(moves[1])

        pointer_up = self.driver.find_element(By.CLASS_NAME, "pointerup")

        up = self.properties(pointer_up)

    def properties(self, element):
        key_value = element.text.split(' ', 1)[1].split(',')
        return {x[0]: x[1] for x in list(map(lambda item: item.split(":"), key_value))}


if __name__ == "__main__":
    unittest.main()
