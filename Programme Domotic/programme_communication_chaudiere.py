#!/usr/bin/env /usr/bin/python

import websocket
import time
import threading
from programme_outil_db import*

############################################
def communication_esp_chaudiere():
    global etat_chaudiere_old
    try:
        #connection à l'esp8266 chaudiere
        ws = websocket.WebSocket()
        ws.connect("ws://192.168.1.101/")
        ws.send(etat_chaudiere_old)
        result = ws.recv()
        ws.close()
     except:
         erreur_chaudiere=1


############################################
def changement_etat():
    global etat_chaudiere_old
    while 1:
        #lecture état de la chaudière
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

    #activation de l esp chaudiere suivant l'état old
    #communication_esp_chaudiere()

    #démarrage du thread
    t1= threading.Thread(target=changement_etat)
    t1.start()

############################################
