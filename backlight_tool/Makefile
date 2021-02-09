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


install_dev: venv
	.venv/bin/pip install -r requirements.test.txt

venv:
	if [[ ! -d .venv/ ]]; \
	then \
		python3 -m venv .venv; \
	fi

tests:
	py.test battery_backlight/tests/
