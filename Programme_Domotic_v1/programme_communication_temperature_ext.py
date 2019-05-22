#!/usr/bin/env /usr/bin/python
import socket
import threading
import time
from tkinter import messagebox
from datetime import datetime
from programme_outil_db import*


############################################
def message_batterie():
    messagebox.showinfo("Attention", "Temperature extérieur /n Batterie faible")
      

############################################
def communication_esp_temperature_ext():
    global maintenant_com, erreur_com
    try:
        tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        tcpsock.bind(("192.168.1.100",1111))
    except:
        time.sleep(1)

    i=0
    while True:
        try:
            #ecoute au niveau du serveur
            tcpsock.listen(10)
            (clientsocket, (ip, port)) = tcpsock.accept()
            recu = str(clientsocket.recv(1024))
            print(recu)
            if i<2:
                try:
                    #verification si communication vivante
                    maintenant = datetime.now()
                    maintenant_com = maintenant.minute

                    #reception
                    recu = int(clientsocket.recv(1024))
                    if (recu < 35 and i==0) :
                        #sauvegarde sur la base
                        variable_input = "temperature_exterieur"
                        variable_etat = recu
                        update_db(variable_input, variable_etat)
                    else:
                        #chargement dans la base
                        variable_input = "hygrometrie_exterieur"
                        #ecriture de la variable si conforme
                        if recu>100:
                            recu = 0
                        #envoie de la variable vers la base
                        variable_etat = recu
                        update_db(variable_input, variable_etat)
                    
                    #tempo deco du client
                    time.sleep(1)
                    i=i+1
                except:
                    a=1
            else:
                recu = float(clientsocket.recv(1024))
                tension_pourcent= int((recu *100)/4.2)
                #sauvegrade sur la base
                variable_input = "niveau_batterie_tempext"
                variable_etat = tension_pourcent
                update_db(variable_input, variable_etat)
                
                print("tension",recu)
                if recu < 0.5:
                    t2= threading.Thread(target=message_batterie)
                    t2.start()
                i=0
        except:
            time.sleep(1)

        #Verification communication présente
        tpsh = datetime.now()
        tpsh_com = tpsh.minute
        if not maintenant_com == tpsh_com :
            #check si erreur deja présente
            if erreur_com==0:
                print (str(tpsh)+" Erreur communication capteur exterieur\n")
                #etat com
                etat_com=1
                #sauvegarde sur la base
                variable_input = "temperature_ext_error"
                variable_etat = etat_com
                update_db(variable_input, variable_etat)
                #passage à 1 de l'ereur
                erreur_com=1
            
        else:
            if erreur_com==1:
                print("Erreur communication extérieur résolue")
            #etat com
            etat_com=0
            #sauvegarde sur la base
            variable_input = "temperature_ext_error"
            variable_etat = etat_com
            update_db(variable_input, variable_etat)
            #réinitialisation de l'erreur com
            erreur_com = 0
############################################
        
    
############################################
def com_esp_temperature_ext():
    global t1, maintenant_com, erreur_com
    #initialisation des variables
    #démarrage verification activité communication
    maintenant = datetime.now()
    maintenant_com = maintenant.minute
    erreur_com=0
    
    #demarrage du thread
    t1= threading.Thread(target=communication_esp_temperature_ext)
    t1.start()
############################################
