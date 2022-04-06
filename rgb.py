from machine import Pin
import utime

rojo = Pin(18, Pin.OUT)
verde = Pin(19, Pin.OUT)
azul = Pin(20, Pin.OUT)


def leds(a,b,c):
    
    rojo.value(a)
    verde.value(b)
    azul.value(c)
          
 
while True:
    leds(0,0,0)
    utime.sleep(2)
    leds(0,0,1)
    utime.sleep(2)
    leds(0,1,0)
    utime.sleep(2)
    leds(0,1,1)
    utime.sleep(2)
    leds(1,0,0)
    utime.sleep(2)
    leds(1,0,1)
    utime.sleep(2)
    leds(1,1,0)
    utime.sleep(2)
    leds(1,1,1)
    utime.sleep(0.5)
    
  

if __name__==("__main__"):
    main()