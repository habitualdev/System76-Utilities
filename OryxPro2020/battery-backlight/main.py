#!/usr/bin/env python3
import os

from battery import Battery
from colors import GREEN, YELLOW, RED
from keyboard_backlight import KeyboardBacklight


def main():
    battery = Battery()
    kb_backlight = KeyboardBacklight(mode='static', battery_handler=battery)
    kb_backlight.run()


if __name__ == '__main__':
    main()
