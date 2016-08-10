import RPi.GPIO as GPIO
import time

GPIO.setwarnings(True)
GPIO.setmode(GPIO.BCM)

GPIO.setup(14, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)

while True:
    GPIO.output(14, False)  # red
    GPIO.output(15, False)  # blue
    GPIO.output(18, True)   # green

GPIO.cleanup()
