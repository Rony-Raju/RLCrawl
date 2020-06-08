import logging
import random
import time
from constants import *

logger = logging.getLogger(__name__)


def create_executor(driver, event_interval, text_values):
    return Executor(driver, event_interval, text_values)


class Executor(object):
    def __init__(self, driver, event_interval, text_values):
        self.driver = driver
        self.event_interval = event_interval
        self.text_values = text_values

    def execute(self, event):
        actions = event["actions"]
        for action in actions:
            if action.action_type == GUIActionType.TEXT_ENTRY:
                selected_text_value = random.choice(self.text_values)
                action.value = selected_text_value

            action.execute(self.driver)

        time.sleep(self.event_interval)




