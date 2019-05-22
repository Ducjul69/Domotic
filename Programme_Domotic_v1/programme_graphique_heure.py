#!/usr/bin/env /usr/bin/python
# coding: utf-8

from tkinter import *
from tkinter import messagebox
import os
import time
import threading
import sqlite3

from programme_outil_db import*


############################
#Remplissage de la base de donnees
def remplisage_heure_bd ():
    while 1:
        try:
            
            #lecture de la temperature
            variable_input = "temperature_interieur"
            lecture_db(variable_input)
            temperature_interieur= lecture_db(variable_input)
            #lecture de l'heure
            variable_input = "heure"
            lecture_db(variable_input)
            heure= lecture_db(variable_input)
            #remplissage de la bd
            with sqlite3.connect('domotic.db') as co_db:
                curseur = co_db.cursor()
                curseur.execute("""UPDATE Temperature SET temperature = ? WHERE heure = ?""", (temperature_interieur,heure,))
            co_db.close()

        except:
            messagebox.showinfo("Erreur", "Erreur enregistrement base de donnee")
            break
        time.sleep(3600)

############################
# demarrage du threat remplissage température base de donnee
def Thread_remplissage_heure ():
    t1 = threading.Thread(target=remplisage_heure_bd)
    t1.start()
