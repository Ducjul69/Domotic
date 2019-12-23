#!/usr/bin/env /usr/bin/python

from tkinter import *
import os
import websocket
import time
import threading
from datetime import datetime

from programme_outil_db import*
from programme_communication_chaudiere import*
from programme_communication_temperature import*
from programme_communication_temperature_ext import*


############################################
#fermeture de la fenetre suite appui bouton
    
def diagnostic_fermer():
    global fenetre_manu
    
    fenetre_manu.destroy()
    
############################################

############################################
#Action mode manu illimité
    
def start_manu_limite():
    global fenetre_manu, spin_time

    #recuperation de la valeur du spin
    temps_manu = spin_time.get()
    #ecriture de la valeur sur la base
    variable_input = "tempo_manu"
    variable_etat = temps_manu
    update_db(variable_input, variable_etat)

    #ecriture sur la db manu =1
    variable_input = "mode_manu"
    variable_etat = 2
    update_db(variable_input, variable_etat)
    
    #fermeture de la fenetre
    fenetre_manu.destroy()
    
############################################


############################################
#Action mode manu illimité
    
def start_manu_illimite():
    global fenetre_manu
    
    #lecture de l'ancien etat
    variable_input = "mode_manu"
    lecture_db(variable_input)
    mode_manu = lecture_db(variable_input)

    #mise à 0 de la tempo
    variable_input = "tempo_manu"
    variable_etat = 0
    update_db(variable_input, variable_etat)

    #activation du mode manu
    if mode_manu == 0:
        #ecriture sur la db manu =1
        variable_input = "mode_manu"
        variable_etat = 1
        update_db(variable_input, variable_etat)
        #ecriture sur la base auto = 0
        variable_input = "mode_auto"
        variable_etat = 0
        update_db(variable_input, variable_etat)
            
    elif mode_manu==1 :
        #ecriture sur la db manu =1
        variable_input = "mode_manu"
        variable_etat = 0
        update_db(variable_input, variable_etat)
        
    #fermeture de la fenetre
    fenetre_manu.destroy()
    
############################################
    
            
############################################
def fenetre_selection_manuel():
    global fenetre_manu, spin_time

    #identification du mode de marche manu actif ou non
    variable_input = "mode_manu"
    lecture_db(variable_input)
    mode_manu= lecture_db(variable_input)
    if mode_manu ==0:
        BP_activation_manu = "Activer le \n mode manuel"
    else:
        BP_activation_manu = "Arrêter le \n mode manuel"
    
    #fenetre secondaire
    fenetre_manu = Toplevel()
    fenetre_manu.title('Pilotage de la maison')
    fenetre_manu.resizable(width=FALSE, height=FALSE)

    #récupération position fenetre_principale
    variable_input = "position_fen_x"
    lecture_db(variable_input)
    position_fen_x= lecture_db(variable_input)
    variable_input = "position_fen_y"
    lecture_db(variable_input)
    position_fen_y= lecture_db(variable_input)

    # get screen width and height
    # calculate x and y coordinates for the Tk root window
    x = 225+position_fen_x
    y = 30+position_fen_y

    fenetre_manu.geometry('%dx%d+%d+%d' % (410, 383, x, y))

    #entete
    entete = Frame(fenetre_manu, bg='#ffde57', height=50)
    entete.pack(fill = X, pady = 2)

    #frame visu
    visu = Frame(fenetre_manu, bg='#4584b6', height=300)
    visu.pack(fill = X, pady = 2)

    #bas de page
    bas_page = Frame(fenetre_manu, bg='#ffde57', height=50)
    bas_page.pack(fill = X, pady = 2)

    ############################################
    #mise en place des titres
    ############################################

    ############################################
    #titre principale de la page
    label = Label(entete, text="Paramètrage mode manuel", bg = "#ffde57", fg = "black")
    label.config(font=("Courier", 20))
    label.grid(row=0, column=1, sticky="nsew", padx = 20)

    
    ############################################
    #zone principale
    #illimité
    label = Label(visu, text="Activation du mode manuel \n pour une durée indéfinie :", bg = "#4584b6", fg = "white")
    label.config(font=("Courier", 18))
    label.grid(row=0, column=0,  columnspan=3,  sticky="nsew", padx = 3)
    #bouton 
    bouton_fermeture = Button(visu, text=BP_activation_manu, command=start_manu_illimite)
    bouton_fermeture.config(font=("Courier", 14))
    bouton_fermeture.grid(row=1, column=0,  columnspan=3,  sticky="nsew",pady = 4, padx = 60)
    
    #limité
    label = Label(visu, text="Activation du mode manuel \n pour une durée définie :", bg = "#4584b6", fg = "white")
    label.config(font=("Courier", 18))
    label.grid(row=2, column=0,  columnspan=3,  sticky="nsew", padx = 3)
    #spin box
    label = Label(visu, text="Durée d'activation :", bg = "#4584b6", fg = "white")
    label.config(font=("Courier", 12))
    label.grid(row=3, column=0,  sticky="nsew")   
    spin_time = Spinbox(visu, from_=0, to=5,increment=0.5,width= 3)
    spin_time.config(font=("Courier", 25))
    spin_time.grid(row=3, column=1,  sticky="nsew")
    label = Label(visu, text="Heure(s)", bg = "#4584b6", fg = "white")
    label.config(font=("Courier", 12))
    label.grid(row=3, column=2,  sticky="nsew", padx = 10)
    #bouton 
    bouton_fermeture = Button(visu, text="Activer le mode \n manuel temporisé", command=start_manu_limite)
    bouton_fermeture.config(font=("Courier", 14))
    bouton_fermeture.grid(row=4, column=0,  columnspan=3,  sticky="nsew",pady = 4, padx = 60)
    
    
    ###########################################
    #zone BP bas
    #bouton de fermeture de la page
    bouton_fermeture = Button(bas_page, text="Retour", command=diagnostic_fermer,width = 11)
    bouton_fermeture.config(font=("Courier", 14))
    bouton_fermeture.grid(row=0, column=2,  rowspan=1,  sticky="ns",pady = 4, padx = 140)
