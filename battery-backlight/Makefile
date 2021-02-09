SHELL := /bin/bash

install: install_conf
	@echo "[-] Installing battery_backlight"
	sudo python3 setup.py install
	@echo "[-] Installing battery-backlight.service Service"
	sudo install -m644 service/battery-backlight.service /etc/systemd/system/
	sudo systemctl daemon-reload

install_conf:
	if [[ ! -f /etc/battery-backlight.conf ]]; \
	then \
		sudo cp configs/battery-backlight.conf /etc/; \
	fi

update_config:
	sudo cp configs/battery-backlight.conf /etc/

