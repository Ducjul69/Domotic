#!/usr/bin/env /usr/bin/python

import asyncio
import websockets
import time
import threading
from tkinter import messagebox
from datetime import datetime


from programme_outil_db import*


        

async def reception_raspberry(websocket, path):
    global maintenant_serveur
    #pour le controle d'activité
    maintenant = datetime.now()
    maintenant_serveur  = maintenant.minute
 
    #reception des infos
    temperature = await websocket.recv()
    temperature =(int(float(temperature)))
    await websocket.send("ok")
    humidite = await websocket.recv()
    humidite = (int(float(humidite)))
    await websocket.send("ok")
    mouvement = await websocket.recv()
    await websocket.send("ok")

    #sauvegarde sur la base
    variable_input = "temperature_interieur"
    variable_etat = temperature
    update_db(variable_input, variable_etat)

    #sauvegarde sur la base
    variable_input = "hygrometrie_interieur"
    variable_etat = humidite
    update_db(variable_input, variable_etat)
    
    #sauvegarde sur la base
    variable_input = "detection_motion"
    variable_etat = mouvement
    update_db(variable_input, variable_etat)

    #etat com
    etat_com=0
    #sauvegarde sur la base
    variable_input = "temperature_int_error"
    variable_etat = etat_com
    update_db(variable_input, variable_etat)
        
############################################
def com_rasp():
    loop=asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    
    start_server = websockets.serve(reception_raspberry, '192.168.1.105', 8765)
    
    loop.run_until_complete(start_server)
    loop.run_forever()


############################################
def controle_activite ():
    global maintenant_serveur
    maintenant_serveur = 0
    while 1:
        maintenant = datetime.now()
        maintenant = datetime.now()
        tpsh = maintenant.minute

        if not maintenant_serveur == tpsh :
            print ("erreur communication avec raspberry")
            #etat com
            etat_com=1
            #sauvegarde sur la base
            variable_input = "temperature_int_error"
            variable_etat = etat_com
            update_db(variable_input, variable_etat)
        else:
            #etat com
            etat_com=0
            #sauvegarde sur la base
            variable_input = "temperature_int_error"
            variable_etat = etat_com
            update_db(variable_input, variable_etat)
            
        time.sleep(30)

############################################
def com_esp_temperature():
    #etat com
    etat_com=1
    #sauvegarde sur la base
    variable_input = "temperature_int_error"
    variable_etat = etat_com
    update_db(variable_input, variable_etat)

    
    t1 = threading.Thread(target=com_rasp)
    t1.start()
    t2 = threading.Thread(target=controle_activite)
    t2.start()
