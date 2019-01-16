#!/usr/bin/env /usr/bin/python

import websocket
import time
import threading
from programme_outil_db import*

############################################
def communication_esp_chaudiere():
    global etat_chaudiere_old
    try:
        #connection a l esp8266 chaudiere
        ws = websocket.WebSocket()
        ws.connect("ws://192.168.1.101/")
        ws.send(etat_chaudiere_old)
        result = ws.recv()
        ws.close()
    except:
        print("erreur")



############################################
def changement_etat():
    global etat_chaudiere_old
    while 1:
        #lecture etat de la chaudiere
        variable_input = "etat_chaudiere"
        lecture_db(variable_input)
        etat_chaudiere_new= str(lecture_db(variable_input))

        if etat_chaudiere_old != etat_chaudiere_new:
            etat_chaudiere_old = etat_chaudiere_new
            communication_esp_chaudiere()
        time.sleep(1)
        
############################################
def com_esp_chaudiere():
    global etat_chaudiere_old

    #etat initial lecture db
    variable_input = "etat_chaudiere"
    lecture_db(variable_input)
    etat_chaudiere_old= str(lecture_db(variable_input))

    #activation de l esp chaudiere suivant l etat old
    #communication_esp_chaudiere()

    #demarrage du thread
    t1= threading.Thread(target=changement_etat)
    t1.start()

############################################
