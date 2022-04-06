from machine import Pin, PWM
from time import sleep


led = PWM(Pin(15), freq=500)  

while True:
    for duty_cycle in range(0, 65535):
        led.duty(duty_cycle)
        sleep(0.01)