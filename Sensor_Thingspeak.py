import network, time, urequests
from machine import Pin,ADC


sensor_a = ADC(Pin(36))
sensor_b = ADC(Pin(39))
led = Pin(15, Pin.OUT)

file = open("lectura.csv", "w")

def conectaWifi (red, password):
      global miRed
      miRed = network.WLAN(network.STA_IF)     
      if not miRed.isconnected():              #Si no está conectado…
          miRed.active(True)                   #activa la interface
          miRed.connect(red, password)         #Intenta conectar con la red
          print('Conectando a la red', red +"…")
          timeout = time.time ()
          while not miRed.isconnected():           #Mientras no se conecte..
              if (time.ticks_diff (time.time (), timeout) > 10):
                  return False
      return True



if conectaWifi ("nombre", "clave"):

    print ("Conexión exitosa!")
    print('Datos de la red (IP/netmask/gw/DNS):', miRed.ifconfig())
      
    url = "https://api.thingspeak.com/update?api_key=UA9Q75WXWMGBZQQB"  
    
    while (True):
       
        lectura_a = sensor_a.read_u16()
        lectura_b = sensor_b.read_u16()
        
        print("Lectura_a = {:02d}, Lectura_b = {:02d}".format (lectura_a,lectura_b))
        
        file.write(str("Lectura ={:02d}, Lectura_b = {:02d}".format (lectura_a,lectura_b) ))
        file.flush()

        respuesta = urequests.get(url+"&field1="+str(lectura_a)+"&field2="+str(lectura_b))
        print(respuesta.text)
        print (respuesta.status_code)
        respuesta.close ()
 
else:
       print ("Imposible conectar")
       miRed.active (False)