SHELL := /bin/bash

install:
	@echo "[-] Installing battery_backlight"
	sudo python3 setup.py install
	@echo "[-] Installing battery-backlight.service Service"
	sudo install -m644 service/battery-backlight.service /etc/systemd/system/
	sudo systemctl daemon-reload

