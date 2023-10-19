import math
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionBuilder
from selenium.webdriver.common.actions.interaction import POINTER_PEN
from selenium.webdriver.common.actions.pointer_input import PointerInput


class TestSimulatePenSetPointerEvent(unittest.TestCase):
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

    def test_simulate_pen_set_pointer_event(self):
        # Navigating to the specified URL
        self.driver.get("https://www.selenium.dev/selenium/web/pointerActionsPage.html")

        # Locating the pointer area element on the webpage
        pointer_area = self.driver.find_element(By.ID, "pointerArea")

        # Creating a new pointer input of type pen
        pen_input = PointerInput(POINTER_PEN, "default pen")

        # Initializing the action builder with the pen input
        self.actions = ActionBuilder(self.driver, mouse=pen_input)

        # Pausing the execution for 2 seconds to allow time for actions
        time.sleep(2)

        # Simulates pointer actions by moving to the specified pointer_area, then performing
        # a pointer_down action.
        # It further moves by 2 pixels in both x and y directions, with specified tilt and
        # twist values, and finally performs a pointer_up action with 0 duration.
        self.actions.pointer_action.move_to(pointer_area) \
            .pointer_down().move_by(2, 2, tilt_x=-72, tilt_y=9, twist=86) \
            .pointer_up(0)

        # Performing the actions on the webpage
        self.actions.perform()

        # Pausing the execution for 2 seconds
        time.sleep(2)

        # Retrieving all the pointer move elements from the webpage
        moves = self.driver.find_elements(By.CLASS_NAME, "pointermove")

        # Extracting properties from the pointer move elements
        move_to = self.properties(moves[0])

        # Retrieving the pointer down element from the webpage
        pointer_down = self.driver.find_element(By.CLASS_NAME, "pointerdown")

        # Extracting properties from the pointer down element
        down = self.properties(pointer_down)

        # Extracting properties from the pointer move by element
        move_by = self.properties(moves[1])

        # Retrieving the pointer up element from the webpage
        pointer_up = self.driver.find_element(By.CLASS_NAME, "pointerup")

        # Extracting properties from the pointer up element
        up = self.properties(pointer_up)

        # Retrieving the dimensions of the pointer area
        rect = pointer_area.rect

        # Calculating the center coordinates of the pointer area
        center_x = rect["x"] + rect["width"] / 2
        center_y = rect["y"] + rect["height"] / 2

        # Assertion to check if the 'button' property of the move_to action is equal to -1
        assert move_to["button"] == "-1"

        # Assertion to check if the 'pointerType' property of the move_to action is equal to 'pen'
        assert move_to["pointerType"] == "pen"

        # Assertion to check if the 'pageX' property of the move_to action is equal to the
        # floor value of the center x-coordinate
        assert move_to["pageX"] == str(math.floor(center_x))

        # Assertion to check if the 'pageY' property of the move_to action is equal to the
        # floor value of the center y-coordinate
        assert move_to["pageY"] == str(math.floor(center_y))

        # Assertion to check if the 'button' property of the down action is equal to 0
        assert down["button"] == "0"

        # Assertion to check if the 'pointerType' property of the down action is equal to 'pen'
        assert down["pointerType"] == "pen"

        # Assertion to check if the 'pageX' property of the down action is equal to the floor
        # value of the center x-coordinate
        assert down["pageX"] == str(math.floor(center_x))

        # Assertion to check if the 'pageY' property of the down action is equal to the floor
        # value of the center y-coordinate
        assert down["pageY"] == str(math.floor(center_y))

        # Assertion to check if the 'button' property of the move_by action is equal to -1
        assert move_by["button"] == "-1"

        # Assertion to check if the 'pointerType' property of the move_by action is equal to 'pen'
        assert move_by["pointerType"] == "pen"

        # Assertion to check if the 'pageX' property of the move_by action is equal to the floor
        # value of the center x-coordinate plus 2
        assert move_by["pageX"] == str(math.floor(center_x + 2))

        # Assertion to check if the 'pageY' property of the move_by action is equal to the floor
        # value of the center y-coordinate plus 2
        assert move_by["pageY"] == str(math.floor(center_y + 2))

        # Assertion to check if the 'tiltX' property of the move_by action is equal to -72
        assert move_by["tiltX"] == "-72"

        # Assertion to check if the 'tiltY' property of the move_by action is equal to 9
        assert move_by["tiltY"] == "9"

        # Assertion to check if the 'twist' property of the move_by action is equal to 86
        assert move_by["twist"] == "86"

        # Assertion to check if the 'button' property of the 'up' action is equal to 0
        assert up["button"] == "0"

        # Assertion to check if the 'pointerType' property of the 'up' action is equal to 'pen'
        assert up["pointerType"] == "pen"

        # Assertion to check if the 'pageX' property of the 'up' action is equal to the floor
        # value of the center x-coordinate plus 2
        assert up["pageX"] == str(math.floor(center_x + 2))

        # Assertion to check if the 'pageY' property of the 'up' action is equal to the floor
        # value of the center y-coordinate plus 2
        assert up["pageY"] == str(math.floor(center_y + 2))

    def properties(self, element):
        # Splitting the text content of the element at the first space and selecting the
        # second part
        key_value = element.text.split(' ', 1)[1].split(', ')

        # Creating a dictionary comprehension that splits each item at the colon and creates
        # key-value pairs
        # The 'lambda' function is used to split each item at the colon
        # The 'map' function applies the lambda function to each item in the list
        # The result is a dictionary with keys and corresponding values extracted from the
        # text content
        return {x[0]: x[1] for x in list(map(lambda item: item.split(': '), key_value))}


if __name__ == "__main__":
    unittest.main()
