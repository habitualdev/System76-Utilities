#!/usr/bin/env python3
import json
import os

from battery_backlight.battery import Battery
from battery_backlight.common import read_file
from battery_backlight.keyboard_backlight import KeyboardBacklight

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
    print("Starting Service")
    kb_backlight.run()


if __name__ == '__main__':
    main()
