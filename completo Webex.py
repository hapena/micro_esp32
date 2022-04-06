###importar librerias ###
import traceback
import requests
import json
from machine  import *
from time import *

### ingresar llave de cisco webex team ###
sparkAuthorizationKey = 'Bearer ODRiYmFiOGQtOTg3MS00YThiLWJhMWEtNDdlNDY2NmU3ZjBkMjM2Y2QzMzgtMDc3_PF84_consumer';



### listado de las salas ###
r = requests.get(   "https://api.ciscospark.com/v1/rooms",
                    headers={'Authorization':sparkAuthorizationKey}
                )
if(r.status_code != 200):
    print("Something wrong has happened:")
    print("ERROR CODE: {} \nRESPONSE: {}".format(r.status_code, r.text))
    assert()


###pines de entrada salida###


led_rojo=Pin(18,Pin.OUT)
led_verde=Pin(19,Pin.OUT)




###recorrer las salas e imprimirlas##
rooms = r.json()['items']



# Ingresar en esta variabl el nombre de la sala
roomNameToSearch = 'ejemploiot'



# Define a variable that will hold the roomId
roomIdToMessage = None
rooms = r.json()['items']
for room in rooms:
    if(room['title'].find(roomNameToSearch) != -1):
        print ("Encontrando Salas  " + roomNameToSearch)
        print ("Nombre de sala: '" + room['title'] + "' ID: " + room['id'])
        roomIdToMessage = room['id']
        roomTitleToMessage = room['title']
        break
lastMessageId = None


# ciclo infinito en el que se mantendra el codigo ejecutandose
while True:

    time.sleep(1)
    getMessagesUrlParameters = {
                "roomId": roomIdToMessage,
                "max": 1
    }



    r = requests.get(   "https://api.ciscospark.com/v1/messages",
                        params=getMessagesUrlParameters,
                        headers={'Authorization':sparkAuthorizationKey}
                    )
    if(r.status_code != 200):
        print("Algo malo ha pasado:")
        print("ERROR CODE: {} \nRESPONSE: {}".format(r.status_code, r.text))
        assert()


    jsonData = r.json()
    messages = jsonData['items']
    message  = messages[0]



    if(lastMessageId == message['id']):
        print("No hay mensajes nuevos")
    else:

        print("Nuevo Mensaje: " + message['text'])
        lastMessageId = message['id']


        # se pregunta si el mensaje recibido es un string con valor de 1
        if(message['text'] == '1'):
            messageId = message['id']
            print("Encendiendo led Rojo")
            mensajeEnviar = "Encendiendo led Rojo"
            print("Enviando...")
            postMessagesUrlParameters = {"text": mensajeEnviar,  "roomId": roomIdToMessage}
            p = requests.post("https://api.ciscospark.com/v1/messages",
                    postMessagesUrlParameters,
                    headers={'Authorization':sparkAuthorizationKey}
                    )
            output(led_rojo, True)
            time.sleep(2)


            # se pregunta si el mensaje recibido es un string con valor de 2
        if(message['text'] == '2'):
            messageId = message['id']
            print("Encendiendo led Verde")
            mensajeEnviar = "Encendiendo led Verde"
            print("Enviando...")
            postMessagesUrlParameters = {"text": mensajeEnviar,  "roomId": roomIdToMessage}
            p = requests.post("https://api.ciscospark.com/v1/messages",
                    postMessagesUrlParameters,
                    headers={'Authorization':sparkAuthorizationKey}
                    )
            output(led_verde, True)
            time.sleep(2)


        if(message['text'] == '3'):
            messageId = message['id']
            print("Apagando  led rojo")
            mensajeEnviar = "Apagando  led rojo"
            print("Enviando...")
            postMessagesUrlParameters = {"text": mensajeEnviar,  "roomId": roomIdToMessage}
            p = requests.post("https://api.ciscospark.com/v1/messages",
                    postMessagesUrlParameters,
                    headers={'Authorization':sparkAuthorizationKey}
                    )

            output(led_rojo, False)
            time.sleep(2)



        if(message['text'] == '4'):
            messageId = message['id']
            print("Apagando  led verde")
            mensajeEnviar = "Apagando  led verde"
            print("Enviando...")
            postMessagesUrlParameters = {"text": mensajeEnviar,  "roomId": roomIdToMessage}
            p = requests.post("https://api.ciscospark.com/v1/messages",
                    postMessagesUrlParameters,
                    headers={'Authorization':sparkAuthorizationKey}
                    )

            output(led_verde, False)
            time.sleep(2)




        else:
            output(led_rojo, False)
            output(led_verde, False)
            time.sleep(2)


