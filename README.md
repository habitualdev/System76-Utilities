# System76-Utilities

Some utilities for System76 computer owners.

Tested on:

* oryp6


## Tools

![battery_backlight CI status](https://github.com/JeffLabonte/System76-Utilities/workflows/CI/badge.svg)
battery-backlight: 
* Make your keyboard change color depending on the battery level
* install:
  * `make install-battery-backlight`
  * `sudo systemctl start battery-backlight.service`
  * `sudo systemctl enable battery-backlight.service`
* configurations:
  * mode:
	* breath
		* Breathing effect
	* static
		* Solid Light
* (battery-backlight.sh - bash script that does the same as above. However, requires you creating a service, or manually running in the background.)

- Legacy Utility Scripts
  * Scripts that have been superseded by more robust utilities, or now have built in functionality/native binaries

----

***Other Projects***

- [Oryx KB LEDs](https://github.com/davemcphee/oryx-kb-leds): Control your Oryx Pro's Keyboard LEDs
- [sys76-kb](https://github.com/bambash/sys76-kb): RGB keyboard controller for System76 laptops
