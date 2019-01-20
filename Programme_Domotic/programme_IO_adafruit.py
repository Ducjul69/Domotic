#! /usr/bin/python

import requests
import os
import time
from time import sleep
from Adafruit_IO import Client
import threading

from programme_outil_db import*


def demarrage_adafruit ():
    global etat_chaudiere_html_old    
    #parametrage de l adafruit         
    aio = Client('ducjul','e076463fcb1446c3aea3184b44285d1a')

    i=1
    if i==1:
        data = aio.receive('chaudiere-action')
        etat_chaudiere_html= format(data.value)
        #Affichage de l etat reel
        variable_input = "etat_chaudiere"
        lecture_db(variable_input)
        etat_chaudiere= lecture_db(variable_input)
        #envoi info adafruit
        if etat_chaudiere==1:
            aio.send('etat-de-la-chaudiere', 'Allumee')
        else:
            aio.send('etat-de-la-chaudiere', 'Eteinte')

        #lecture temperature interieur db
        variable_input = "temperature_interieur"
        lecture_db(variable_input)
        etat_temperature= lecture_db(variable_input)
        etat_temperature = str(etat_temperature)
        aio.send('temperature-exterieur',etat_temperature )   
        print(etat_temperature+" send")        
        
        
        if etat_chaudiere_html == "ON" and etat_chaudiere_html_old !=etat_chaudiere_html:
            #ecriture de la variable sur la base
            variable_input = "mode_manu"
            variable_etat = 1
            update_db(variable_input, variable_etat)
            etat_chaudiere_html_old = etat_chaudiere_html
                    
        if etat_chaudiere_html == "OFF"and etat_chaudiere_html_old !=etat_chaudiere_html: 
            #ecriture de la variable sur la base
            variable_input = "mode_manu"
            variable_etat = 0
            update_db(variable_input, variable_etat)
            etat_chaudiere_html_old = etat_chaudiere_html
              
        time.sleep(5)
    
    

def adafruit():
    global etat_chaudiere_html_old
    # lecture valeur old
    etat_chaudiere_html_old = "OFF"
    t2 = threading.Thread(target=demarrage_adafruit)
    t2.start()
