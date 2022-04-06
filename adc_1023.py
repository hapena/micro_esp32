from machine import Pin, ADC
import utime
 
 
sensor = ADC(Pin(36))  // #  mq135 = MQ135(ADC(Pin(36))) 
sensor.width(ADC.WIDTH_12BIT)  # permite regular la precisión de lectura
sensor.atten(ADC.ATTN_11DB) # permite trabajar con 3.3v

while True:
    
    lectura =  int(sensor.read())
    print(lectura)
    utime.sleep(0.5)
    
    