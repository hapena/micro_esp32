from machine import Pin, PWM
import utime

def main():
    
    servo = PWM(Pin(27), freq = 50)        
    
    
    while True:
        angulo = float(input('Ingrese un ángulo: '))
        if angulo >= 0 and angulo <= 180:
            ciclo = ((12.346*angulo**2 + 7777.8*angulo + 700000))
            ciclo /= 1000000
            ciclo = int(ciclo*1023/20)
            servo.duty(ciclo)            
        else:
            print('Digite un ángulo entre 0 y 180')
    
if __name__ == '__main__':
    main()