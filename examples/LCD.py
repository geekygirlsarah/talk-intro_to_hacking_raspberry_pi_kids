import RPi_I2C_driver
from time import *

mylcd = RPi_I2C_driver.lcd()

mylcd.backlight(1)
mylcd.lcd_display_string("  Good morning!", 1)
mylcd.lcd_display_string("    Welcome!", 2)

while True:
    sleep(10)
    
mylcd.lcd_clear()
