#!/usr/bin/env /usr/bin/python
import socket
import threading
import time
from tkinter import messagebox

from programme_outil_db import*

def message_batterie():
    messagebox.showinfo("Attention", "Temperature extérieur /n Batterie faible")
      

############################################
def communication_esp_temperature_ext():
    tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    tcpsock.bind(("192.168.1.107",1111))

    i=0
    while True:
        print( "En écoute...")
        tcpsock.listen(10)
        (clientsocket, (ip, port)) = tcpsock.accept()
        if i<2:
            try:
                recu = int(clientsocket.recv(1024))
                if (recu < 35 and i==0) :
                    #sauvegarde sur la base
                    variable_input = "temperature_exterieur"
                    variable_etat = recu
                    update_db(variable_input, variable_etat)
                else:
                    #chargement dans la base
                    variable_input = "hygrometrie_exterieur"
                    variable_etat = recu
                    update_db(variable_input, variable_etat)
                
                print("variable recue :", recu)
                print("Client déconnecté...\n")
                time.sleep(1)
                i=i+1
            except:
                print("erreur")
        else:
            recu = float(clientsocket.recv(1024))
            print("tension",recu)
            if recu < 0.5:
                t2= threading.Thread(target=message_batterie)
                t2.start()
            i=0
############################################
        
    
############################################
def com_esp_temperature_ext():
    global t1
    #demarrage du thread
    t1= threading.Thread(target=communication_esp_temperature_ext)
    t1.start()
############################################
