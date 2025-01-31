#!/bin/bash
# installer.sh
# Author: BlackLeakz
# Website: https://luxuzleakz.de/
# Github: https://github.com/blackleakz/BPI-M2-Berry_ssd1306-oled-control.git
# Device: Banana-Pi-M2-Berry
# Additional-Hardware: OLED SSD1306 Display
# NFO: This device haves the same GPIO-Pin-selection as Raspberry Pi Pico

echo -n "At first you should enable i2c-devices by using the rasp-config or armbian-config"

echo -e "For armbian-config navigate to System, the select Hardware and enable i2c2 & i2c3. "

echo -n "Installing now dependencys..."

sudo apt-get install git python3-dev i2c-tools libffi-dev libssl-dev python3-pil libjpeg-dev zlib1g-dev libfreetype6-dev liblcms2-dev libopenjp2-7 libtiff5 git make cmake build-essential python3-dev python*pip -y 
python3 -m pip install --upgrade pip wheel setuptools --break-system-packages
python3 -m pip install Adafruit-SSD1306 Adafruit-BBIO psutil --break-system-packages 
python3 -m pip install -r requirements.txt --break-system-packages
sudo python3 -m pip install --upgrade pip wheel setuptools --break-system-packages
sudo python3 -m pip install Adafruit-SSD1306 Adafruit-BBIO psutil --break-system-packages
sudo python3 -m pip install -r requirements.txt --break-system-packages

pip3 install luma-oled --break-system-packages
sudo pip3 install luma-oled --break-system-packages

cd ~
mkdir tmp
cd tmp

git clone https://github.com/rm-hull/luma.oled.git
sudo chmod a+x -R ./*
$me=(whoami)
sudo chown $me -hR /home/$me/tmp/luma*
cd ~/tmp/luma*
sudo python3 setup.py install --break-system-packages
python3 setup.py install --break-system-packages







