#!/bin/sh

battery=100
red="FF0000"
green="00FF00"
yellow="FFFF00"
backlight="/sys/class/leds/system76_acpi::kbd_backlight"
brightness=100
while [ 1 -eq 1 ]
do 
	while [ $brightness -lt 155 ] 
	   do
		echo $brightness > $backlight/brightness
		brightness=$(( $brightness+1 ))
	done

	while [ $brightness -gt 15 ]
       	do
		echo $brightness > $backlight/brightness
		brightness=$(( $brightness-1 ))
	done
	full=$(cat /sys/class/power_supply/BAT0/charge_full)
	current=$(cat /sys/class/power_supply/BAT0/charge_now)
	battery=$(( ($current*100)/$full ))

	if [ $battery -lt 20 ]
	then echo $red > $backlight/color
	elif [ $battery -lt 50 ]
	then echo $yellow > $backlight/color
	elif [ $battery -lt 100 ]
	then echo $green > $backlight/color
	fi
done
