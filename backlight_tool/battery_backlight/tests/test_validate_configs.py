import pytest

from battery_backlight.__main__ import validate_configs


@pytest.mark.parametrize("configurations", [
    {
        "mode": "breath",
    },
    {
        "mode": "static",
    },
    {
        "brightness_min_value": 254,
        "brightness_max_value": 255,
    },
    {
        "red_threshold": 98,
        "yellow_threshold": 99,
    },
    {
        "mode": "breath",
        "brightness_min_value": 254,
        "brightness_max_value": 255,
        "red_threshold": 98,
        "yellow_threshold": 99,
    }
])
def test_validate_configs__pass_valid_configurations__should_not_raise_exception(configurations):
    validate_configs(configurations)


@pytest.mark.parametrize("configurations", [
    {
        "mode": 123,
    },
    {
        "mode": "breathee",
    },
    {
        "brightness_max_value": 255,
    },
    {
        "brightness_min_value": 0,
    },
    {
        "yellow_threshold": 20,
    },
    {
        "red_threshold": 10,
    },
    {
        "brightness_max_value": 1,
        "brightness_min_value": 2,
    },
    {
        "yellow_threshold": 2,
        "red_threshold": 3,
    }
])
def test_validate_configs__pass_invalid_configurations__should_raise_exception(configurations):
    with pytest.raises(RuntimeError):
        validate_configs(configurations)
