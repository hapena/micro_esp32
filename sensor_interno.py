import esp32
from machine import Pin
import utime


while True:
    
    temp = esp32.raw_temperature()
    #cent= (((temp-32)*5)/9)
    print(temp)
    utime.sleep_ms(100)
