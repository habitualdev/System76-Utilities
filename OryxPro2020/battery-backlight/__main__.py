#!/usr/bin/env python3
import json
import os

from battery import Battery
from common import read_file
from keyboard_backlight import KeyboardBacklight

CONFIGURATION_PATH = '/etc/battery-backlight.conf'


def read_configurations():
    if os.path.exists(CONFIGURATION_PATH):
        return json.loads(read_file(CONFIGURATION_PATH))
    return {}


def main():
    config = read_configurations()

    battery = Battery()
    kb_backlight = KeyboardBacklight(
        mode=config.get('mode', 'breath'),
        battery_handler=battery
    )
    kb_backlight.run()


if __name__ == '__main__':
    main()
