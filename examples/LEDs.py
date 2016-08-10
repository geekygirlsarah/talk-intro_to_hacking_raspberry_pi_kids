import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(3, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)

pins = [3, 5, 7]
speed = .5

for i in pins:
    print(i)
    GPIO.output(i, True)
    time.sleep(speed)
    GPIO.output(i, False)

for i in reversed(pins):
    print(i)
    GPIO.output(i, True)
    time.sleep(speed)
    GPIO.output(i, False)
    


GPIO.cleanup()
