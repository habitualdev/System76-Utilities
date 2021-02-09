#!/usr/bin/env python3
import os

import yaml
from cerberus import Validator

from battery_backlight.battery import Battery
from battery_backlight.common import read_file
from battery_backlight.keyboard_backlight import KeyboardBacklight
from battery_backlight.schema.configurations import schema as configurations_schema

CONFIGURATION_PATH = '/etc/battery-backlight.conf'


def validate_configs(configurations):
    validator = Validator(configurations_schema)
    if not validator.validate(configurations):
        raise RuntimeError(validator.errors)

    if max_value := configurations.get('brightness_max_value'):
        if max_value <= configurations.get('brightness_min_value'):
            raise RuntimeError(
                "Expect brightness_min_value to be greater than brightness_max_value"
            )

    if yellow_threshold := configurations.get('yellow_threshold'):
        if yellow_threshold <= configurations.get('red_threshold'):
            raise RuntimeError(
                "Expect yellow_threshold to be greater than red_threshold"
            )


def read_configurations():
    if os.path.exists(CONFIGURATION_PATH):
        confs = yaml.load(
            read_file(CONFIGURATION_PATH),
            Loader=yaml.FullLoader
        )
        validate_configs(confs)
        return confs

    return {}


def main():
    config = read_configurations()

    battery = Battery()
    kb_backlight = KeyboardBacklight(
        context=config,
        battery_handler=battery
    )
    print("Starting Service")
    kb_backlight.run()


if __name__ == '__main__':
    main()
