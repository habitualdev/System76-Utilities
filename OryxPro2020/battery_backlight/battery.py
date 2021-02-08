from battery_backlight.common import read_file


class Battery:
    FULL_BATTERY_PATH = '/sys/class/power_supply/BAT0/charge_full'
    CURRENT_BATTERY_PATH = '/sys/class/power_supply/BAT0/charge_now'

    def _read_current_battery(self):
        return read_file(self.CURRENT_BATTERY_PATH)

    def _read_full_battery(self):
        return read_file(self.FULL_BATTERY_PATH)

    def get_battery_level(self):
        current = int(self._read_current_battery())
        full = int(self._read_full_battery())

        return (current * 100) // full
