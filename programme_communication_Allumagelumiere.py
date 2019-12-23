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
    activité = await websocket.recv()
    tpsh = maintenant.hour
    tpsh=int(tpsh)
    tpsm = maintenant.minute
    tpsm = int(tpsm)
    print(tpsh)
    if tpsh>= 18 and tpsh<=23 and not tpsm>=15 and not tpsm>=20 or tpsm==15:
        await websocket.send("ok")
        print("ok")
    else:
        await websocket.send("nok")
        print("nok")
    
############################################
def com_esp():
    try:
        loop=asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        
        start_server = websockets.serve(reception_raspberry, '192.168.1.105', 8888)
        print("serveur ok")
        loop.run_until_complete(start_server)
        loop.run_forever()
    except:
        i=1

############################################
#def com_esp_lumiere():
    

print("bonjour")    
t9 = threading.Thread(target=com_esp)
t9.start()
    
