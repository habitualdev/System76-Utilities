import subprocess
from time import sleep
from typing import Dict

from battery_backlight.battery import Battery
from battery_backlight.colors import GREEN, YELLOW, RED
from battery_backlight.common import read_file, write_file


def get_laptop_model() -> str:
    return subprocess.check_output(['sudo', 'dmidecode', '-s', 'system-product-name']).decode('utf-8').strip()


class KeyboardBacklight:
    BACKLIGHT_DEVICE_PATH = "/sys/class/leds/system76_acpi::kbd_backlight"

    MODEL_BACKLIGHT_PATH_MAPPING = {
        'Oryx Pro': {
            'brightness_path': '/sys/class/leds/system76_acpi::kbd_backlight/brightness',
            'brightness_color': '/sys/class/leds/system76_acpi::kbd_backlight/color',
        },
        'Serval WS': {
            'brightness_path': '/sys/class/leds/system76::kbd_backlight/brightness',
            'brightness_color': '/sys/class/leds/system76::kbd_backlight/color_left',
        },
    }

    def __init__(self, context: Dict, battery_handler: Battery):
        laptop_model = get_laptop_model()
        keyboard_backlight_paths = self.MODEL_BACKLIGHT_PATH_MAPPING.get(
            laptop_model,
        )

        if keyboard_backlight_paths is None:
            raise RuntimeError(
                f"{laptop_model} is not supported by this script"
            )

        self.brightness_path = keyboard_backlight_paths['brightness_path']
        self.brightness_color = keyboard_backlight_paths['brightness_color']

        self.brightness_max_value = context.get('brightness_max_value', 255)
        self.brightness_min_value = context.get('brightness_min_value', 15)

        self.red_threshold = context.get('red_threshold', 25)
        self.yellow_threshold = context.get('yellow_threshold', 50)

        self.mode = context.get('mode', 'breath')
        self.mode_functions_mapping = {
            "breath": self.breath,
            "static": self.static,
        }

        self.battery_handler = battery_handler

    def run(self):
        while True:
            self.mode_functions_mapping[self.mode]()
            self.change_color(
                battery_level=self.battery_handler.get_battery_level()
            )

    def breath(self):
        self._ramp_up()
        self._ramp_down()

    def static(self):
        if self._read_brightness() != self.brightness_max_value:
            self._set_full_brightness()
        sleep(0.2)

    def change_color(self, battery_level):
        if battery_level < self.red_threshold:
            self._set_color(RED)
        elif battery_level < self.yellow_threshold:
            self._set_color(YELLOW)
        else:
            self._set_color(GREEN)

    def _ramp_up(self):
        current_brightness = self._read_brightness()
        while current_brightness < self.brightness_max_value:
            self._set_brightness(value=current_brightness)
            current_brightness += 1

    def _ramp_down(self):
        current_brightness = self._read_brightness()
        while current_brightness > self.brightness_min_value:
            self._set_brightness(value=current_brightness)
            current_brightness -= 1

    def _set_color(self, color):
        write_file(path=self.brightness_color, value=color)

    def _set_full_brightness(self):
        write_file(path=self.brightness_path,
                   value=str(self.brightness_max_value))

    def _set_brightness(self, value: int):
        write_file(path=self.brightness_path, value=str(value))

    def _read_brightness(self) -> int:
        return int(read_file(path=self.brightness_path))
