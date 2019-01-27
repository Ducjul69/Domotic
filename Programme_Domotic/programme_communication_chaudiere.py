#!/usr/bin/env /usr/bin/python

import websocket
import time
import threading
from tkinter import messagebox

from programme_outil_db import*

############################################
def communication_esp_chaudiere():
    i=0
    try:
        #lecture etat de la chaudiere
        variable_input = "etat_chaudiere"
        lecture_db(variable_input)
        etat_chaudiere= lecture_db(variable_input)
        #connection a l esp8266 chaudiere
        ws = websocket.WebSocket()
        ws.connect("ws://192.168.1.101/")
        ws.send(str(etat_chaudiere))
        result = ws.recv()
        ws.close()
        if result =="recu":
            if etat_chaudiere ==1:
                #mise à jour etat reel chaudiere
                variable_input = "etat_chaudiere_reel"
                variable_etat = 1
                update_db(variable_input, variable_etat)
            if etat_chaudiere ==0:
                #mise à jour etat reel chaudiere
                variable_input = "etat_chaudiere_reel"
                variable_etat = 0
                update_db(variable_input, variable_etat)
        #mise à jour error_com
        variable_input = "chaudiere_com_error"
        variable_etat = 0
        update_db(variable_input, variable_etat)
        time.sleep(10)

    except:
        #error com
        variable_input = "chaudiere_com_error"
        variable_etat = 1
        update_db(variable_input, variable_etat)
        time.sleep(5)
        print("erreur com chaudiere")

############################################
def changement_etat():
    while 1:
        communication_esp_chaudiere()
     
############################################
#programme démarrage
        
def com_esp_chaudiere():
    #demarrage du thread
    t1= threading.Thread(target=changement_etat)
    t1.start()
    
############################################
