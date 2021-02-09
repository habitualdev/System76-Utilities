schema = {
    "mode": {
        "type": "string",
        "required": False,
        "allowed": ['breath', 'static'],
    },
    "brightness_max_value": {
        "type": "number",
        "min": 1,
        "max": 255,
        "dependencies": ["brightness_min_value"],
        "required": False,
    },
    "brightness_min_value": {
        "type": "number",
        "min": 0,
        "max": 254,
        "dependencies": ["brightness_max_value"],
        "required": False,
    },
    "red_threshold": {
        "type": "number",
        "min": 0,
        "max": 98,
        "dependencies": ["yellow_threshold"],
        "required": False,
    },
    "yellow_threshold": {
        "type": "number",
        "min": 1,
        "max": 99,
        "dependencies": ["red_threshold"],
        "required": False,
    },
}
