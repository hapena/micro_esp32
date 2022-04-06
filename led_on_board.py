from machine import Pin, ADC, PWM
from utime import  sleep, sleep_ms

led_interno = Pin(2, Pin.OUT)

while True:

    led_interno.value(1)
    sleep_ms(100)
    led_interno.value(0)
    sleep_ms(100)


