#!/usr/bin/env /usr/bin/python

import websocket
import time
import threading
from tkinter import messagebox

from programme_outil_db import*

############################################
def communication_esp_chaudiere():
    global erreur_com
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
        
        #reprise après une erreur de com
        if erreur_com==1:
            print("Erreur communication chaudière résolue")
        #pas d'erreur de com
        erreur_com=1
        #mise en pose de la communication
        time.sleep(10)
        

    except:
        #error com
        maintenant = datetime.now()
        if erreur_com == 0:
            variable_input = "chaudiere_com_error"
            variable_etat = 1
            update_db(variable_input, variable_etat)
            time.sleep(5)
            print(str(maintenant)+" Erreur communication chaudiere\n")
            #initialisation de l'erreur
            erreur_com=1
        time.sleep(5)
        

############################################
def changement_etat():
    while 1:
        communication_esp_chaudiere()
     
############################################
#programme démarrage
        
def com_esp_chaudiere():
    global erreur_com
    erreur_com=0
    #demarrage du thread
    t1= threading.Thread(target=changement_etat)
    t1.start()
    
############################################
