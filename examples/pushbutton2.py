import RPi.GPIO as GPIO
import time

switch_pin = 18

GPIO.setmode(GPIO.BCM)

GPIO.setup(switch_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    input_state = GPIO.input(switch_pin)
    if input_state == False:
        print("Button pressed")
        time.sleep(0.2)
        
