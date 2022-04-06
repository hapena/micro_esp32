from dht import DHT11
from machine import Pin
from utime import sleep

sensorDHT = DHT11(Pin(15))

while True:

    sleep(1)
    sensorDHT.measure()
    temp = sensorDHT.temperature()
    hum = sensorDHT.humidity()
    kel = temp + 273
    far = (temp*5)/9 + 32
   

    print("T={:02d}C H={:02d}%  K={:02d}K  F= {:02}F".format(temp, hum, kel, far))


