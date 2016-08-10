import RPi.GPIO as GPIO
import time

switch_pin = 2
led_pin = 15

GPIO.setmode(GPIO.BCM)

GPIO.setup(switch_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(led_pin, GPIO.OUT)
GPIO.setup(14, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.output(14, False)
GPIO.output(18, False)

while True:
    input_state = GPIO.input(switch_pin)
    if input_state == False:
        print("Button pressed")
        #time.sleep(0.2)
        GPIO.output(led_pin, True)
    else:
        GPIO.output(led_pin, False)
        
        
