#!/usr/bin/env python3
from configparser import ConfigParser
import os

from battery import Battery
from keyboard_backlight import KeyboardBacklight

CONFIGURATION_PATH = '/etc/battery-backlight.conf'


def read_configurations():
    if os.path.exists(CONFIGURATION_PATH):
        config_parser = ConfigParser()
        config_parser.read_file(CONFIGURATION_PATH)
        return config_parser
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
