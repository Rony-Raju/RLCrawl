import logging
from constants import SelectorType, KeyCode
from appium.webdriver.common.touch_action import TouchAction
from exceptions import UnknownAction

logger = logging.getLogger(__name__)


class Action:
    def __init__(self, target, action_type, value=None):
        self.target = target
        self.action_type = action_type
        self.value = value

    def find_element(self, driver):
        selector = self.target["selector"]
        selector_value = self.target["selectorValue"]
        if selector == SelectorType.ID:
            element = driver.find_element_by_id(selector_value)
        elif selector == SelectorType.XPATH:
            element = driver.find_element_by_xpath(selector_value)
        else:
            element = None

        return element

    def execute(self, driver):
        raise UnknownAction("Unknown action.")

    def to_dict(self):
        action_as_dict = {
            "target": self.target,
            "type": self.action_type,
            "value": self.value
        }
        return action_as_dict

    def __eq__(self, other_action):
        if self.action_type == other_action.action_type and self.target == other_action.target \
                and self.value == other_action.value:
            return True

        return False


class Click(Action):
    def __init__(self, target, action_type, value=None):
        super().__init__(target, action_type, value)

    def execute(self, driver):
        element = self.find_element(driver)
        element.click()


class TextEntry(Action):
    def __init__(self, target, action_type, value=None):
        super().__init__(target, action_type, value)

    def execute(self, driver):
        logger.info("Filling in text field: {}".format(self.target["description"]))
        logger.info("Typing text: {}".format(self.value))
        text_field_element = self.find_element(driver)
        text_field_element.send_keys(self.value)


class Home(Action):
    def __init__(self, target, action_type, value=None):
        super().__init__(target, action_type, value)

    def execute(self, driver):
        logger.info("Pressing HOME navigation button.")
        driver.press_keycode(KeyCode.HOME)


class Back(Action):
    def __init__(self, target, action_type, value=None):
        super().__init__(target, action_type, value)

    def execute(self, driver):
        logger.info("Pressing BACK navigation button.")
        driver.press_keycode(KeyCode.BACK)


class ReturnKey(Action):
    def __init__(self, target, action_type, value=None):
        super().__init__(target, action_type, value)

    def execute(self, driver):
        logger.info("Pressing RETURN key.")
        driver.press_keycode(KeyCode.RETURN)


class RunInBackground(Action):
    def __init__(self, target, action_type, value=None):
        super().__init__(target, action_type, value)

    def execute(self, driver):
        logger.info("Running app in background for 1 second.")
        driver.background_app(1)


class LongClick(Action):
    def __init__(self, target, action_type, value=None):
        super().__init__(target, action_type, value)

    def execute(self, driver):
        logger.info("Executing long-click event.")
        element = self.find_element(driver)
        action = TouchAction(driver)
        action.long_press(element).perform()


class SwipeUp(Action):
    def __init__(self, target, action_type, value=None):
        super().__init__(target, action_type, value)

    def execute(self, driver):
        logger.info("Executing long-click event.")
        screen_size = driver.get_window_size()
        start_y = int(screen_size["height"] * 0.80)
        end_y = int(screen_size["width"] * 0.20)
        start_x = int(screen_size["width"] / 2)
        driver.swipe(start_x, start_y, start_x, end_y, 200)


class SwipeDown(Action):
    def __init__(self, target, action_type, value=None):
        super().__init__(target, action_type, value)

    def execute(self, driver):
        logger.info("Executing swipe down event.")
        screen_size = driver.get_window_size()
        start_y = int(screen_size["height"] * 0.20)
        end_y = int(screen_size["height"] * 0.80)
        start_x = int(screen_size["width"] / 2)
        driver.swipe(start_x, start_y, start_x, end_y, 200)


class SwipeRight(Action):
    def __init__(self, target, action_type, value=None):
        super().__init__(target, action_type, value)

    def execute(self, driver):
        logger.info("Executing swipe right event.")
        screen_size = driver.get_window_size()
        start_x = int(screen_size["width"] * 0.20)
        end_x = int(screen_size["width"] * 0.80)
        start_y = int(screen_size["height"] / 2)
        driver.swipe(start_x, start_y, end_x, start_y, 200)


class SwipeLeft(Action):
    def __init__(self, target, action_type, value=None):
        super().__init__(target, action_type, value)

    def execute(self, driver):
        logger.info("Executing swipe left event.")
        screen_size = driver.get_window_size()
        start_x = int(screen_size["width"] * 0.80)
        end_x = int(screen_size["width"] * 0.20)
        start_y = int(screen_size["height"] / 2.0)
        driver.swipe(start_x, start_y, end_x, start_y, 200)

class LaunchApp(Action):
    def __init__(self, target, action_type, value=None):
        super().__init__(target, action_type, value)

    def execute(self, driver):
        pass




