import mhz19b
import Adafruit_DHT
import RPi.GPIO as GPIO
import datetime
import time
import oled


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

co2_sensor = mhz19b.MHZ19b()
temp_sensor = Adafruit_DHT.DHT22
display = oled.OledDisplay()

while 1:
    try:
        formatted_day_time = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d_%H:%M:%S')
        formatted_time = datetime.datetime.fromtimestamp(time.time()).strftime('%H:%M')
        humidity, temperature = Adafruit_DHT.read_retry(temp_sensor, 18)
        co2 = co2_sensor.get_co2()
        print "%s; t = %.1f; h = %.1f; co2 = %d" % (formatted_day_time, temperature, humidity, co2)
        display.update(formatted_time, co2, temperature, humidity)
    except:
        pass
    time.sleep(5)
