#!/bin/bash
#Charge the battery to 100%, when you're going to disconnect the battery

echo 0 > /sys/class/power_supply/BAT0/charge_control_start_threshold
echo 100 > /sys/class/power_supply/BAT0/charge_control_end_threshold

