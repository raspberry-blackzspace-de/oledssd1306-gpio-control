# Name: Raspberry Pi - OLED SSD1306 - Display Control by using Python3
# Author: hexzhen3x7
['https://blackzspace.de.de'] (blackzspace.de)
# Github: ['https://github.com/raspberry-blackzspace-de/oledssd1306-gpio-control.git'] (GIT)
# Version: 0.1a


```
Here you'll learn,  how to deal with Banana Pi M2 Berry's gpio-pins , which are the same as raspberry pi 3.

```
#1 - GPIO-PIN Settings for the ssd1306 oled display: Connect your GPIO-PINS like that.

```
 PIN-NUMBER: 1 | CON1-P01 (GPIO Pin Name) |  VCC-3V3 (Default Function)    
 PIN-NUMBER: 3 | CON1-P03 (GPIO Pin Name) |  TWI2-SDA (Default Function)
 PIN-NUMBER: 5 | CON1-P05 (GPIO Pin Name) |  TWI2-SCK	(Default Function)     
 PIN-NUMBER: 9 | CON1-P09 (GPIO Pin Name) |  GND (Default Function)



```
#2 - Install requirements:
```
(Debian/Ubuntu)

sudo apt-get install -y i2c-tools;
sudo apt-get install python3-dev libffi-dev libssl-dev python3-pil libjpeg-dev zlib1g-dev libfreetype6-dev liblcms2-dev libopenjp2-7 libtiff5 -y;
sudo -H pip3 install luma.oled

```
#3 - Turn on i2c -

-  for Raspian OS:```
    sudo raspi-config
    sudo reboot```

-  for Armbian:```
     sudo armbian-config
     select Hardware
     enable i2c2
     enable i2c3
     sudo reboot```


#4 - Now, try to scan for connected i2c-tools:

```
i2cdetect -y 1
```

  4.1 - the ouput should be like this:

```
0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
00:                         -- -- -- -- -- -- -- --
10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
30: -- -- -- -- -- -- -- -- -- -- -- -- 3c -- -- --
40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
70: -- -- -- -- -- -- -- --
```

4.2 - that shows the current i2c-devices matrix,  the i2c-address is = 0x3C, port = 2

4.3 - to control the oled display, run python3 and import the libary luma.oled as shown below:

<code>
<```
from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import ssd1306
```
</code>
<comment>
4.3 -  after including the libarys you need to define the device you wanna use band initializ a serial-communication with followin parameters: (port=2, address=0x3C)

in python code you need to initializ the i2c-device by using the parameters the command i2cdetect, outputed before
</comment>
<code>
<```
serial = i2c(port=2, address=0x3C)
device = ssd1306(serial)
```
</code>
then you can call the modules.draw function by writin:
<code>
<```
with canvas(device) as draw:
    draw.rectangle(device.bounding_box, outline="white", fill="black")
    draw.text((30, 40), "Hello World", fill="white")
```
</code>


