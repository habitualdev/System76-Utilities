from common import read_file


class Battery:
    FULL_BATTERY_PATH = '/sys/class/power_supply/BAT0/charge_full'
    CURRENT_BATTERY_PATH = '/sys/class/power_supply/BAT0/charge_now'

    @classmethod
    def _read_current_battery(cls):
        return read_file(cls.CURRENT_BATTERY_PATH)

    @classmethod
    def _read_full_battery(cls):
        return read_file(cls.FULL_BATTERY_PATH)

    @classmethod
    def get_battery_level(cls):
        current = int(cls._read_current_battery())
        full = int(cls._read_full_battery())

        return (current * 100) // full
