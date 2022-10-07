import RPi.GPIO as GPIO
import time
from time import sleep

LED_OUT = 13
GPIO.setwarnings(False)
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_OUT, GPIO.OUT)
GPIO.output(LED_OUT, False)

while True:
    GPIO.output(13, True)
    time.sleep(1);
    GPIO.output(13, False)
    time.sleep(1);