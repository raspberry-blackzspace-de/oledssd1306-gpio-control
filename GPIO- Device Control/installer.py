#!/usr/bin/env python3
# installer.py
# Author: BlackLeakz
# Website: https://luxuzleakz.de/
# Github: https://github.com/blackleakz/BPI-M2-Berry_ssd1306-oled-control.git
# Device: Banana-Pi-M2-Berry
# Additional-Hardware: OLED SSD1306 Display
# NFO: This device haves the same GPIO-Pin-selection as Raspberry Pi Pico


import os
import sys
import subprocess
import platform
from os.path import *


p = platform.system()

def install():
    print("Detected: " + p)
    print("\nInstalling now... .. .")
    os.system("sudo apt-get install python3-dev libffi-dev libssl-dev python3-pil libjpeg-dev zlib1g-dev libfreetype6-dev liblcms2-dev libopenjp2-7 libtiff5 git make cmake build-essential python3-dev python*pip -y ")
    os.system("python3 -m pip install --upgrade pip wheel setuptools")
    os.system('python3 -m pip install Adafruit-SSD1306 Adafruit-BBIO psutil')
    os.system("python3 -m pip install -r requirements.txt")

def main():
    if p == "Linux":
	  install()
    else:
        print("Detected: " + p)
        print("\nTryin to install now... .. .")
        os.system("python3 -m pip install --upgrade pip wheel setuptools")
        os.system('python3 -m pip install Adafruit-SSD1306 Adafruit-BBIO psutil')
        os.system("python3 -m pip install -r requirements.txt")


if __name__ == '__main__':
    main()
