import logging
import actions
from constants import *


logger = logging.getLogger(__name__)


def create_target(selector, selector_value, description, target_type, state):
    target = {
        "selector": selector,
        "selectorValue": selector_value,
        "description": description,
        "type": target_type,
        "state": state
    }

    return target


def create_enter_target():
    enter_target = {
        "selector": "key_code",
        "selectorValue": "66",
        "description": "Return key",
        "type": "keyboard",
        "state": "enabled"
    }

    return enter_target


def create_launch_event():
    target = create_target(SelectorType.SYSTEM, "app", "launch", TargetType.APP, TargetState.ENABLED)
    action = create_action(SystemActionType.LAUNCH, target)
    precondition = create_state(None, None)
    partial_event = create_partial_event(precondition, [action])

    return partial_event


def create_partial_event(precondition, actions):
    partial_event = {
        "precondition": precondition,
        "actions": actions
    }
    return partial_event


def create_partial_text_events(current_state, text_entry_actions, non_text_entry_actions):
    if len(text_entry_actions) == 1:
        logger.debug("Only one text field in the current state. We may need to use the ENTER key since it may be a search field.")

        text_based_events = create_events_for_single_text_field(current_state,
                                                                text_entry_actions[0], non_text_entry_actions)
    else:
        logger.debug("Multiple text fields in current state. Creating events for multiple text fields.")

        text_based_events = create_events_for_multiple_text_fields(current_state,
                                                                   text_entry_actions, non_text_entry_actions)

    single_action_events = create_single_action_events(current_state, non_text_entry_actions)

    events = text_based_events + single_action_events

    logger.debug("{} text-based events generated for current state.".format(len(events)))

    return events


def create_events_for_single_text_field(current_state, text_entry_action, non_text_entry_actions):
    text_entry_action.value = "[random string]"  # -- test this

    text_entry_enter_key_event = pair_text_entry_with_enter_key(current_state, text_entry_action)
    text_and_act_events = pair_text_entry_with_non_text_entry_actions(current_state, text_entry_action,
                                                                      non_text_entry_actions)
    text_and_act_events.append(text_entry_enter_key_event)

    return text_and_act_events


def pair_text_entry_with_enter_key(current_state, text_entry_action):
    enter_target = create_enter_target()
    enter_key_action = create_action(GUIActionType.ENTER_KEY, enter_target)

    text_entry_enter_key_event = create_partial_event(current_state, [text_entry_action, enter_key_action])

    return text_entry_enter_key_event


def pair_text_entry_with_non_text_entry_actions(current_state, text_entry_action, non_text_entry_actions):
    text_and_act_events = []
    for non_text_entry_action in non_text_entry_actions:
        action_pairs_with_text_entry = does_action_pair_with_text_entry(non_text_entry_action)
        if action_pairs_with_text_entry:
            text_and_act_event = create_partial_event(current_state, [text_entry_action, non_text_entry_action])
            text_and_act_events.append(text_and_act_event)

    return text_and_act_events


def create_events_for_multiple_text_fields(current_state, text_entry_actions, non_text_entry_actions):
    text_based_events = []
    text_based_actions = []
    for text_entry_action in text_entry_actions:
        text_entry_action.value = "[random string]"
        text_based_actions.append(text_entry_action)

    for non_text_entry_action in non_text_entry_actions:
        action_pairs_with_text_entry = does_action_pair_with_text_entry(non_text_entry_action)
        if action_pairs_with_text_entry:
            multiple_text_entry_event = create_partial_event(current_state, text_entry_actions + [non_text_entry_action])
            text_based_events.append(multiple_text_entry_event)

    return text_based_events


def create_single_action_events(current_state, non_text_entry_actions):
    single_action_events = []
    for non_text_entry_action in non_text_entry_actions:
        single_action_event = create_partial_event(current_state, [non_text_entry_action])
        single_action_events.append(single_action_event)

    return single_action_events


def does_action_pair_with_text_entry(non_text_entry_action):
    invalid_targets = {"spinner", "checkbox", "edittext", "radiobutton", "togglebutton"}
    return non_text_entry_action.action_type == GUIActionType.CLICK and \
        non_text_entry_action.target["type"].lower() not in invalid_targets


def create_partial_events(current_state, possible_actions):
    events = []
    for action in possible_actions:
        event = create_partial_event(current_state, [action])
        events.append(event)

    return events


def create_back_event(precondition):
    target = create_target("key_code", KeyCode.BACK, "back", TargetType.NAV, TargetState.ENABLED)
    action = create_action(GUIActionType.BACK_NAV, target)
    back_event = create_partial_event(precondition, [action])
    return back_event


def create_home_event(precondition):
    target = create_target("key_code", KeyCode.HOME, "home", TargetType.NAV, TargetState.ENABLED)
    action = create_action(GUIActionType.HOME_NAV, target)
    home_event = create_partial_event(precondition, [action])
    return home_event


def create_background_event(precondition):
    target = create_target(SelectorType.SYSTEM, "app", "run in background", TargetType.APP, TargetState.ENABLED)
    action = create_action(SystemActionType.RUN_IN_BACKGROUND, target)
    background_event = create_partial_event(precondition, [action])
    return background_event


def create_action(action_type, widget):
    action_types = {
        GUIActionType.CLICK: actions.Click,
        GUIActionType.LONG_CLICK: actions.LongClick,
        GUIActionType.BACK_NAV: actions.Back,
        GUIActionType.HOME_NAV: actions.Home,
        GUIActionType.LAUNCH: actions.LaunchApp,
        GUIActionType.CHECK: actions.Click,
        GUIActionType.UNCHECK: actions.Click,
        GUIActionType.ENTER_KEY: actions.ReturnKey,
        GUIActionType.SWIPE_DOWN: actions.SwipeDown,
        GUIActionType.SWIPE_LEFT: actions.SwipeLeft,
        GUIActionType.SWIPE_RIGHT: actions.SwipeRight,
        GUIActionType.SWIPE_UP: actions.SwipeUp,
        GUIActionType.TEXT_ENTRY: actions.TextEntry,
        SystemActionType.RUN_IN_BACKGROUND: actions.RunInBackground,
        SystemActionType.LAUNCH: actions.LaunchApp
    }
    action_class = action_types[action_type]
    action = action_class(widget, action_type, None)
    return action


def create_ui_widget(xml_tree, element):
    selection_mechanism = _get_widget_selector(xml_tree, element)
    widget_description = _get_widget_description(element)
    widget_type = _get_widget_type(element)
    widget_state = _get_widget_state(element)
    target = {
        "selector": selection_mechanism[0],
        "selectorValue": selection_mechanism[1],
        "description": widget_description,
        "type": widget_type,
        "state": widget_state
    }

    return target


def _get_widget_state(element):
    element_attributes = element.attrib
    if element_attributes.get(TargetState.ENABLED, "") == "true":
        return TargetState.ENABLED

    return TargetState.DISABLED


def _get_widget_type(element):
    element_attributes = element.attrib
    class_value = element_attributes.get("class", "")
    return class_value.split(".")[-1]


def _get_widget_selector(xml_tree, element):
    element_attributes = element.attrib
    resource_id = element_attributes.get("resource-id", "")
    id_not_unique = len(_get_elements_with_id(resource_id, xml_tree)) > 1
    if resource_id.strip() == "" or id_not_unique:
        return "xpath", xml_tree.getpath(element)

    return "id", resource_id


def _get_elements_with_id(resource_id, xml_tree):
    return xml_tree.getroot().findall(".//*[@resource-id='" + resource_id + "']".format(resource_id))


def _get_widget_description(element):
    element_attributes = element.attrib
    text_value = element_attributes.get("text", "").strip()
    content_desc_value = element_attributes.get("content-desc", "").strip()
    if text_value == "":
        if content_desc_value == "":
            description = ""
        else:
            description = content_desc_value
    else:
        description = text_value

    return description


def synthesize(partial_event, current_state):
    postcondition = {
        "activityName": current_state["activityName"],
        "stateId": current_state["stateId"]
    }
    partial_event["postcondition"] = postcondition
    return partial_event


def create_state(current_activity, state_id):
    state = {
        "activityName": current_activity,
        "stateId": state_id
    }

    return state


def create_crash_state():
    state= {
        "activityName": "crash",
        "stateId": "crash"
    }

    return state


def make_event_serializable(event):
    non_serializable_actions = event["actions"]
    actions_as_dicts = []
    for action in non_serializable_actions:
        actions_as_dicts.append(action.to_dict())

    event["actions"] = actions_as_dicts

    return event

