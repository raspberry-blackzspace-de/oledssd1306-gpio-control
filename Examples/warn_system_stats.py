import psutil
import time
import RPi.GPIO as GPIO
from luma.oled.device import ssd1306
from luma.core.interface.serial import i2c
from PIL import Image, ImageDraw, ImageFont

# Setze GPIO-Pin und initialisiere das GPIO-Modul
LED_PIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

# Funktion, um die CPU-Temperatur zu lesen
def get_cpu_temp():
    try:
        with open("/sys/class/thermal/thermal_zone0/temp", "r") as f:
            temp = f.read()
            return float(temp) / 1000  # In Celsius
    except FileNotFoundError:
        return None

# Funktion, um die GPU-Temperatur zu lesen
def get_gpu_temp():
    try:
        result = psutil.sensors_temperatures().get('coretemp', None)
        if result:
            return result[0].current  # GPU-Temperatur
        return None
    except Exception as e:
        print(f"Fehler beim Abrufen der GPU-Temperatur: {e}")
        return None

# Setze das OLED-Display mit i2c
serial = i2c(port=1, address=0x3C)  # Der Standard i2c-Port und die Adresse
device = ssd1306(serial)

# Initialisiere das Bild und das Zeichnen
width, height = device.size
image = Image.new('1', (width, height))
draw = ImageDraw.Draw(image)

# Standard-Schriftart für das Display
font = ImageFont.load_default()

def blink_led():
    """Lässt die LED blinken"""
    GPIO.output(LED_PIN, GPIO.HIGH)  # LED an
    time.sleep(0.1)                  # 100ms warten
    GPIO.output(LED_PIN, GPIO.LOW)   # LED aus
    time.sleep(0.1)                  # 100ms warten

while True:
    # Holen von Systeminformationen
    cpu_percent = psutil.cpu_percent(interval=1)  # CPU-Auslastung in %
    memory = psutil.virtual_memory()
    gpu_temp = get_gpu_temp()
    cpu_temp = get_cpu_temp()

    # Bildschirm leeren
    draw.rectangle((0, 0, width, height), outline=0, fill=0)

    # Text auf dem Display anzeigen
    draw.text((0, 0), f"CPU Auslastung: {cpu_percent}%", font=font, fill=255)
    draw.text((0, 10), f"Speicher: {memory.percent}%", font=font, fill=255)
    draw.text((0, 20), f"CPU Temp: {cpu_temp} C" if cpu_temp else "CPU Temp: N/A", font=font, fill=255)
    draw.text((0, 30), f"GPU Temp: {gpu_temp} C" if gpu_temp else "GPU Temp: N/A", font=font, fill=255)

    # Update des Displays
    device.display(image)

    # Ausgabe im Terminal
    print(f"CPU Auslastung: {cpu_percent}%")
    print(f"Speicher Auslastung: {memory.percent}%")
    print(f"CPU Temperatur: {cpu_temp} °C" if cpu_temp else "CPU Temperatur: N/A")
    print(f"GPU Temperatur: {gpu_temp} °C" if gpu_temp else "GPU Temperatur: N/A")

    # Blinken der LED, wenn die Temperatur über 50°C ist
    if cpu_temp and cpu_temp > 50 or gpu_temp and gpu_temp > 50:
        blink_led()

    # Wartezeit von 2 Sekunden
    time.sleep(2)

# Aufräumen bei Programmende
GPIO.cleanup()
