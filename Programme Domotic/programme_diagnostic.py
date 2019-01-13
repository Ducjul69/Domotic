#!/usr/bin/env /usr/bin/python

from tkinter import *
import os
import time
import threading
from datetime import datetime

from programme_outil_db import*


###########################################
# Gestion de l'heure   
def heure():
    global localdate, labeltps1
    while 1:
            maintenant = datetime.now()
            tpsh = maintenant.hour
            strtpsh = str(tpsh)
            tpsm = maintenant.minute
            strtpsm = str(tpsm)
            tpss = maintenant.second
            strtpss = str(tpss)
            localdate = strtpsh+":"+strtpsm+":"+strtpss
            labeltps1.configure(text= localdate)
            time.sleep(1)
            
############################################

############################################
#fermeture de la fenetre suite appui bouton
def diagnostic_fermer():
    global fenetre_diag
   #mise à jour de la base
    variable_input = "fermeture"
    variable_etat = 1
    update_db(variable_input, variable_etat)
    fenetre_diag.destroy()
    
############################################
############################################
#Gestion de la fermeture de la page
def diagnostic_ecriture_fichier():
    fichier = open("Echange.txt", "w")
    fichier.write("ferme")
    #fermeture
    fichier.close()
############################################

    
            
############################################
def fenetre_diagnostic():
    global labeltps1, fenetre_diag
    #fenetre principale
    fenetre_diag = Toplevel()
    fenetre_diag.title('Pilotage de la maison')
    fenetre_diag.resizable(width=FALSE, height=FALSE)
    fenetre_diag.geometry('{}x{}'.format(800, 400))

    #entete
    entete = Frame(fenetre_diag, bg='grey', height=50)
    entete.pack(fill = X, pady = 2)

    #frame visu
    visu = Frame(fenetre_diag, bg='grey', height=300)
    visu.pack(fill = X, pady = 2)

    #bas de page
    bas_page = Frame(fenetre_diag, bg='grey', height=50)
    bas_page.pack(fill = X, pady = 2)

    ############################################
    #mise en place des titres
    ############################################
    # démarrage du thread de l'heure
    localdate=1  
    labeltps1 = Label(entete, text="", bg = "grey",fg ="white")
    labeltps1.config(font=("Courier", 20))
    labeltps1.grid(row=0, column=0, sticky="nsew")
    tplanning = threading.Thread(target=heure)
    tplanning.start()


    ############################################
    #titre principale de la page
    label = Label(entete, text="Diagnostics", bg = "grey", fg = "white")
    label.config(font=("Courier", 20))
    label.grid(row=0, column=1, sticky="nsew", ipadx = 150)

    
    ############################################
    # Récuperation des données de la db
    #communication chaudiere
    variable_input = "etat_com_chaudiere"
    lecture_db(variable_input)
    etat_com_chaudiere= lecture_db(variable_input)
    #communication temperature exterieur
    variable_input = "etat_com_interieur"
    lecture_db(variable_input)
    etat_com_interieur= lecture_db(variable_input)
    #communication temperature interieur
    variable_input = "etat_com_ext"
    lecture_db(variable_input)
    etat_com_ext= lecture_db(variable_input)

    if etat_com_chaudiere == 1:
        etat_com_chaudiere = "Communication établie"
    else:
        etat_com_chaudiere = "Communication perdue"
        
    if etat_com_interieur == 1:
        etat_com_interieur = "Communication établie"
    else:
        etat_com_interieur = "Communication perdue"
        
    if etat_com_ext == 1:
        etat_com_ext = "Communication établie"
    else:
        etat_com_ext = "Communication perdue"
    
    ############################################
    #zone principale
    label = Label(visu, text="Etat communication avec la chaudiere :", bg = "grey", fg = "white")
    label.config(font=("Courier", 12))
    label.grid(row=0, column=0,columnspan=1)
    etat1 = Label(visu, text=etat_com_chaudiere, bg = "grey", fg = "white")
    etat1.config(font=("Courier", 12))
    etat1.grid(row=0, column=1,columnspan=1)

    label = Label(visu, text="Etat communication capteur extérieur :", bg = "grey", fg = "white")
    label.config(font=("Courier", 12))
    label.grid(row=1, column=0,columnspan=1)
    etat2 = Label(visu, text=etat_com_ext, bg = "grey", fg = "white")
    etat2.config(font=("Courier", 12))
    etat2.grid(row=1, column=1,columnspan=1)
    
    label = Label(visu, text="Etat communication capteur intérieur :", bg = "grey", fg = "white")
    label.config(font=("Courier", 12))
    label.grid(row=2, column=0,columnspan=1)
    etat3 = Label(visu, text=etat_com_interieur, bg = "grey", fg = "white")
    etat3.config(font=("Courier", 12))
    etat3.grid(row=2, column=1,columnspan=1)


    

    #bouton de fermeture de la page
    bouton_fermeture = Button(bas_page, text="Retour", command=diagnostic_fermer,width = 11)
    bouton_fermeture.config(font=("Courier", 14))
    bouton_fermeture.grid(row=0, column=2,  rowspan=1,  sticky="ns",pady = 4, padx = 3)



#---------------------------------------------------------------------------
def programme_diag():
    with open("Echange.txt", "w") as fichier:
        time.sleep(0.1)
    fichier.close()
    fenetre_diagnostic()
