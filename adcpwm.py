from machine import Pin, PWM, ADC
import utime

def main():
    
    sensor = ADC(Pin(36))
    sensor.width(ADC.WIDTH_10BIT) # permite regular la precisión de lectura
    sensor.atten(ADC.ATTN_11DB)
    
    servo = PWM(Pin(27), freq = 50)        
    
    def map(x):
        return int((x - 0) * (130- 34) / (180 - 0) + 34)
    
    def mapadc(x):
        return int((x - 0) * (1023- 0) / (130 - 34) + 0)
    
    while True:
                   
        lectura =  float(sensor.read())/10
        print(lectura)
        angulo = mapadc(lectura)              
        m = map(angulo)
        servo.duty(m)
        utime.sleep(0.2)  
        print(m)
   
    
if __name__ == '__main__':
    main()