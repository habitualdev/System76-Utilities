from time import sleep

from battery import Battery
from colors import GREEN, YELLOW, GREEN
from common import read_file, write_file


class KeyboardBacklight:
    BACKLIGHT_DEVICE_PATH = "/sys/class/leds/system76_acpi::kbd_backlight"

    _MAX_VALUE = 155
    _MIN_VALUE = 15

    def __init__(self, mode: str, battery_handler: Battery):
        self.brightness_path = f"{self.BACKLIGHT_DEVICE_PATH}/brightness"
        self.brightness_color = f"{self.BACKLIGHT_DEVICE_PATH}/color"
        self.mode = mode
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
        if self._read_brightness() != self._MAX_VALUE:
            self._set_full_brightness()
        sleep(0.2)

    def change_color(self, battery_level):
        if battery_level <= 25:
            self._set_color(RED)
        elif battery_level <= 50:
            self._set_color(YELLOW)
        else:
            self._set_color(GREEN)

    def _ramp_up(self):
        current_brightness = self._read_brightness()
        while current_brightness < self._MAX_VALUE:
            self._set_brightness(value=current_brightness)
            current_brightness += 1

    def _ramp_down(self):
        current_brightness = self._read_brightness()
        while current_brightness > self._MIN_VALUE:
            self._set_brightness(value=current_brightness)
            current_brightness -= 1

    def _set_color(self, color):
        write_file(path=self.brightness_color, value=color)

    def _set_full_brightness(self):
        write_file(path=self.brightness_path, value=self._MAX_VALUE)

    def _set_brightness(self, value: int):
        write_file(path=self.brightness_path, value=str(value))

    def _read_brightness(self) -> int:
        return int(read_file(path=self.brightness_path))
