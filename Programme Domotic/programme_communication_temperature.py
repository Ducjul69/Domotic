#!/usr/bin/env /usr/bin/python

import websocket
import time
import threading
from programme_outil_db import*

############################################
def communication_esp_temperature():
    global etat_chaudiere_old
    #connection à l'esp8266 
    ws = websocket.WebSocket()
    ws.connect("ws://192.168.1.103/")
    ws.send("0")
    humidite = ws.recv()
    humidite=float(humidite)
    #chargement dans la base
    variable_input = "hygrometrie_interieur"
    variable_etat = int(humidite)
    update_db(variable_input, variable_etat)
    time.sleep(1)
    
    ws.send("1")
    temperature = ws.recv()
    temperature=float(temperature)
    #chargement dans la base
    variable_input = "temperature_interieur"
    variable_etat = int(temperature)
    update_db(variable_input, variable_etat)
    time.sleep(1)
    
    ws.send("2")
    resenti = ws.recv()
    resenti=float(resenti)
    time.sleep(1)
    ws.close()
        


############################################
def changement_etat():
    global etat_chaudiere_old
    while 1:
        communication_esp_temperature()
        print("com")
        time.sleep(5)
        
############################################
def com_esp_temperature():
    #démarrage du thread
    t1= threading.Thread(target=changement_etat)
    t1.start()

############################################
