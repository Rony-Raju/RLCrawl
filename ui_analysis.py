import lxml.etree as etree
import logging
import abstraction
from hashing import generate_state_hash
from constants import *

logger = logging.getLogger(__name__)


def get_available_events(driver):
    current_state = get_current_state(driver)
    page_source = driver.page_source
    possible_actions = get_possible_actions(page_source)
    text_entry_actions, non_text_entry_actions = classify_actions(possible_actions)
    if text_entry_actions:
        available_events = abstraction.create_partial_text_events(current_state, text_entry_actions, non_text_entry_actions)
    else:
        available_events = abstraction.create_partial_events(current_state, possible_actions)

    available_events.append(abstraction.create_back_event(current_state))
    available_events.append(abstraction.create_background_event(current_state))

    return available_events


def classify_actions(possible_actions):
    text_entry_actions = []
    non_text_entry_actions = []
    for action in possible_actions:
        if action.action_type == GUIActionType.TEXT_ENTRY:
            text_entry_actions.append(action)
        else:
            non_text_entry_actions.append(action)

    return text_entry_actions, non_text_entry_actions


def get_possible_actions(page_source):
    possible_actions = []
    actionable_widgets = _get_actionable_widgets(page_source)
    for action_type, widgets in actionable_widgets.items():
        for widget in widgets:
            action = abstraction.create_action(action_type, widget)
            possible_actions.append(action)

    logger.debug("Found {} possible actions.".format(len(possible_actions)))
    return possible_actions


def _get_actionable_widgets(page_source):
    actionable_widgets = {
        GUIActionType.CLICK: [],
        GUIActionType.LONG_CLICK: [],
        GUIActionType.CHECK: [],
        GUIActionType.UNCHECK: [],
        GUIActionType.SWIPE_UP: [],
        GUIActionType.SWIPE_DOWN: [],
        GUIActionType.SWIPE_RIGHT: [],
        GUIActionType.SWIPE_LEFT: [],
        GUIActionType.TEXT_ENTRY: []
    }

    xml_element = etree.fromstring(page_source.encode())
    xml_tree = etree.ElementTree(xml_element)
    for element in xml_tree.iter():
        element_attributes = element.attrib
        element_is_text_field = "EditText" in element_attributes.get("class", "")
        element_is_enabled = element_attributes.get("enabled", "") == "true"
        actionable_widget = abstraction.create_ui_widget(xml_tree, element)
        if element_is_text_field and element_is_enabled:
            actionable_widgets[GUIActionType.TEXT_ENTRY].append(actionable_widget)
        else:
            if _element_is_clickable(element):
                actionable_widgets[GUIActionType.CLICK].append(actionable_widget)
            if _element_is_long_clickable(element):
                actionable_widgets[GUIActionType.LONG_CLICK].append(actionable_widget)
            if _element_is_checkable(element):
                if _element_is_checked(element):
                    actionable_widgets[GUIActionType.UNCHECK].append(actionable_widget)
                else:
                    actionable_widgets[GUIActionType.CHECK].append(actionable_widget)
            if _element_is_scrollable(element):
                actionable_widgets[GUIActionType.SWIPE_UP].append(actionable_widget)
                actionable_widgets[GUIActionType.SWIPE_DOWN].append(actionable_widget)
                actionable_widgets[GUIActionType.SWIPE_RIGHT].append(actionable_widget)
                actionable_widgets[GUIActionType.SWIPE_LEFT].append(actionable_widget)

    logger.debug("Found actionable widgets: {}".format(actionable_widgets))
    return actionable_widgets


def _element_is_clickable(element):
    return element.attrib.get("clickable", "false") == "true"


def _element_is_scrollable(element):
    return element.attrib.get("scrollable", "false") == "true"


def _element_is_long_clickable(element):
    return element.attrib.get("long-clickable", "false") == "true"


def _element_is_checkable(element):
    return element.attrib.get("checkable", "false") == "true"


def _element_is_checked(element):
    return element.attrib.get("checked", "false") == "true"


def get_current_state(driver):
    try:
        page_source = driver.page_source
        possible_actions = get_possible_actions(page_source)
        current_activity = driver.current_activity
        state_id = generate_state_hash(possible_actions)
        current_state = abstraction.create_state(current_activity, state_id)
    except Exception as e:
        logger.error("Could not retrieve current state: %s".format(e))
        current_state = abstraction.create_crash_state()

    logger.debug("Current state: {}".format(current_state))
    return current_state

