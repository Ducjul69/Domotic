#!/usr/bin/env /usr/bin/python

import websocket
import time
import threading
from tkinter import messagebox

import asyncio
import websockets

from programme_outil_db import*

############################################
def communication_esp_temperature_ext():
    print ("tesrer")
    #connection a l esp8266 
    ws = websocket.WebSocket()
    ws.connect("ws://192.168.1.102/")
    print("truc")
    ws.send("0")
    humidite = ws.recv()
    humidite=float(humidite)
    #chargement dans la base
    variable_input = "hygrometrie_exterieur"
    variable_etat = int(humidite)
    update_db(variable_input, variable_etat)
    time.sleep(0.5)
        
    ws.send("1")
    temperature = ws.recv()
    temperature=float(temperature)
    #chargement dans la base
    variable_input = "temperature_exterieur"
    variable_etat = int(temperature)
    update_db(variable_input, variable_etat)
    time.sleep(0.5)
        
    ws.send("2")
    resenti = ws.recv()
    resenti=float(resenti)
    time.sleep(0.5)
    ws.close()
        

############################################
def changement_etat():
    """   i=0
    while 1:
        try:
            print("trucd")
            communication_esp_temperature_ext()
            #ecriture bd pas de pb sur la com
            variable_input = "temperature_ext_error"
            variable_etat = 0
            update_db(variable_input, variable_etat)

        except:
            a=1"""


    async def echo(websocket, path):
        async for message in websocket:
            await websocket.send(message)

    asyncio.get_event_loop().run_until_complete(websockets.serve(echo, 'localhost', 8765))
    asyncio.get_event_loop().run_forever()
    print(messsage)
        



def com_esp_temperature_ext():
    global t1
    #demarrage du thread
    t1= threading.Thread(target=changement_etat)
    t1.start()

############################################
