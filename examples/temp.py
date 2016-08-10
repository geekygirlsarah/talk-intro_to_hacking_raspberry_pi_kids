#Drive 16x2 LCD screen with Raspberry Pi
#Tutorial : http://osoyoo.com/?p=858
import dht11
import RPi.GPIO as GPIO
import time

# Define GPIO to LCD mapping
Temp_sensor=7

# Timing constants
E_PULSE = 0.0005
E_DELAY = 0.0005

# Main program block
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)       # Use BCM GPIO numbers
instance = dht11.DHT11(pin = Temp_sensor)

while True:
  #get DHT11 sensor value
  result = instance.read()
  # Send some test

  if result.is_valid():
    print("temp:"+str(result.temperature)+" C")
    print("humid:"+str(result.humidity)+"%")
  else:
    print("Error: "+str(result.error_code))
          

#  try:
#    main()
#  except KeyboardInterrupt:
#    pass
#  finally:
#    GPIO.cleanup()
