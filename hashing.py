import json
import hashlib


def _get_hash_target(action):
    hash_target = {
        "selector": action.target["selector"],
        "selectorValue": action.target["selectorValue"],
        "state": action.target["state"],
        "type": action.target["type"]
    }
    return hash_target


def _get_hash_action(action, hash_target):
    hash_action = {
        "target": hash_target,
        "type": action.action_type,
    }
    return hash_action


def _get_hash_event(event):
    hash_event = {}
    actions = event["actions"]
    hash_actions = []
    for action in actions:
        hash_target = _get_hash_target(action)
        hash_action = _get_hash_action(action, hash_target)
        hash_actions.append(hash_action)

    hash_event["actions"] = hash_actions
    hash_event["precondition"] = event["precondition"]

    return hash_event


def generate_state_hash(actions):
    # the order of the actions does not matter
    hash_source = []
    for action in actions:
        hash_target = _get_hash_target(action)
        hash_action = _get_hash_action(action, hash_target)
        hash_source.append(hash_action)

    hash_source.sort(key=lambda the_action: the_action["type"] + "@" + the_action["target"]["selector"] +
                     "=" + the_action["target"]["selectorValue"])
    json_hash_source = json.dumps(hash_source, sort_keys=True)
    return hashlib.sha1(json_hash_source.encode("utf-8")).hexdigest()


def generate_test_case_hash(events):
    hash_source = []
    for event in events:
        hash_event = _get_hash_event(event)
        hash_source.append(hash_event)

    json_hash_source = json.dumps(hash_source, sort_keys=True)
    return hashlib.sha1(json_hash_source.encode("utf-8")).hexdigest()


def generate_event_hash(event):
    # the order of the actions matters
    hash_event = _get_hash_event(event)
    json_hash_source = json.dumps(hash_event, sort_keys=True)
    return hashlib.sha1(json_hash_source.encode("utf-8")).hexdigest()
