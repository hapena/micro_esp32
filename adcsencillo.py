from machine import Pin, ADC
import utime
 
 
sensor = ADC(Pin(36))
 
while True:
    
    lectura =  float(sensor.read_u16())
    print(lectura)
    utime.sleep(0.25)
    