#!/bin/bash
#Limit the battery's max charge to elongate use life

echo 60 > /sys/class/power_supply/BAT0/charge_control_start_threshold
echo 81 > /sys/class/power_supply/BAT0/charge_control_end_threshold

