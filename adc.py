from machine import Pin, ADC
import utime


# Indicadores
bombillo= Pin(2, Pin.OUT)


# calibrar.... de acuerdo a las especificaciones del sensor
sensor = ADC(Pin(36))
sensor.atten(ADC.ATTN_11DB)  # para calibrar de 0 a 3.6v
sensor.width(ADC.WIDTH_12BIT) # establecer resolucion de 12 bits hasta 4096

while True:
    
    lectura =  sensor.read()
    print("Luz", lectura)
    utime.sleep_ms(100)
    
    '''if lectura > 1800:
        bombillo.value(1)
        
    else:
        bombillo.value(0)'''
    
    
        
    