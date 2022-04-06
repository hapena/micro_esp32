from machine import Pin, PWM
from time import sleep

led = PWM(Pin(15), freq=5000)  

while True:
    led.duty(0)
    sleep(0.5)
    led.duty(10000)
    sleep(0.5)
    led.duty(20000)
    sleep(0.5)
    led.duty(30000)
    sleep(0.5)
    led.duty(40000)
    sleep(0.5)
    led.duty(60000)
    sleep(0.5)
    
    
    