#!/usr/bin/env /usr/bin/python

from tkinter import *
import os
import websocket
import time
import threading
from datetime import datetime

from programme_outil_db import*


###########################################
# Gestion de l heure   
def heure():
    global localdate, labeltps1,tplanning
    while 1:
            try:
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
            except:
                #arret thread heure
                tplanning.atuer=True
############################################





############################################
#changement des label pendant thread
def changement_label():
    global fin_thread, t10
    
    while fin_thread==0:
        #mise a jour des labels
        etat1.configure(text = ("scrutation du r"+u"\u00E9"+"seau en cours ."))
        etat2.configure(text = ("scrutation du r"+u"\u00E9"+"sseau en cours ."))
        etat3.configure(text = ("scrutation du r"+u"\u00E9"+"sseau en cours ."))
        time.sleep(0.2)
        etat1.configure(text = ("scrutation du r"+u"\u00E9"+"sseau en cours .."))
        etat2.configure(text = ("scrutation du r"+u"\u00E9"+"sseau en cours .."))
        etat3.configure(text = ("scrutation du r"+u"\u00E9"+"sseau en cours .."))
        time.sleep(0.2)
        etat1.configure(text = ("scrutation du r"+u"\u00E9"+"sseau en cours ..."))
        etat2.configure(text = ("scrutation du r"+u"\u00E9"+"sseau en cours ..."))
        etat3.configure(text = ("scrutation du r"+u"\u00E9"+"sseau en cours ..."))
        time.sleep(0.2)
    time.sleep(2)




    # Recuperation des donnees de la db
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
        etat_com_chaudiere = "Communication "+u"\u00E9"+"tablie"
    else:
        etat_com_chaudiere = "Communication perdue"
        
    if etat_com_interieur == 1:
        etat_com_interieur = "Communication "+u"\u00E9"+"tablie"
    else:
        etat_com_interieur = "Communication perdue"
        
    if etat_com_ext == 1:
        etat_com_ext = "Communication "+u"\u00E9"+"tablie"
    else:
        etat_com_ext = "Communication perdue"

    #mise a jour des labels
    etat1.configure(text = (etat_com_chaudiere))
    etat2.configure(text = (etat_com_interieur))
    etat3.configure(text = (etat_com_ext))

    t10.atuer =True
    

############################################
#lancement du thread diagnostic
def start_diagnostic():
    global t10, fin_thread, t1
    
    fin_thread = 0
    t10 = threading.Thread(target=changement_label)
    t10.start()
    t1 = threading.Thread(target=start_diagnostic_thread)
    t1.start()
  
    
     

############################################
#Gestion de la fermeture de la page
def start_diagnostic_thread():

    
    #communication avec chaudiere
    global etat1, etat2, etat3, fin_thread,t1
    try:
        ws = websocket.WebSocket()
        ws.connect("ws://192.168.1.101/")
        ws.close()
        result1=1
        
    except:
        result1=0

    #communication avec temperature interieur
    try:
        ws = websocket.WebSocket()
        ws.connect("ws://192.168.1.103/")
        ws.close()
        result2=1
    except:
        result2=0
    #communication avec temperature exterieur
    try:
        ws = websocket.WebSocket()
        ws.connect("ws://192.168.1.101/")
        ws.close()
        result3=1
    except:
        result3=0

    #sauvegarde des valeurs sur la db
    #com chaudiere
    if result1 ==1:
        variable_input = "etat_com_chaudiere"
        variable_etat = 1
        update_db(variable_input, variable_etat)
    else:
        variable_input = "etat_com_chaudiere"
        variable_etat = 0
        update_db(variable_input, variable_etat)
    #com temperature interieure
    if result2 ==1:
        variable_input = "etat_com_interieur"
        variable_etat = 1
        update_db(variable_input, variable_etat)
    else:
        variable_input = "etat_com_interieur"
        variable_etat = 0
        update_db(variable_input, variable_etat)        
    #com temperature exterieur
    if result3 ==1:
        variable_input = "etat_com_ext"
        variable_etat = 1
        update_db(variable_input, variable_etat)
    else:
        variable_input = "etat_com_ext"
        variable_etat = 0
        update_db(variable_input, variable_etat)


    fin_thread =1
    t1.atuer =True

    
############################################





############################################
#fermeture de la fenetre suite appui bouton
def diagnostic_fermer():
    global fenetre_diag
    #mise a jour de la base
    variable_input = "fermeture"
    variable_etat = 1
    update_db(variable_input, variable_etat)
    fenetre_diag.destroy()

    
    
############################################

    
            
############################################
def fenetre_diagnostic():
    global labeltps1, fenetre_diag, etat1, etat2, etat3, tplanning
    #fenetre principale
    fenetre_diag = Toplevel()
    fenetre_diag.title('Pilotage de la maison')
    fenetre_diag.resizable(width=FALSE, height=FALSE)


    # get screen width and height
    # calculate x and y coordinates for the Tk root window
    x = (800/2) - (800/2)
    y = (410/2) - (440/2)

    fenetre_diag.geometry('%dx%d+%d+%d' % (800, 400, x, y))

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
    # demarrage du thread de l heure
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
    # Recuperation des donnees de la db
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
        etat_com_chaudiere = "Communication "+u"\u00E9"+"tablie"
    else:
        etat_com_chaudiere = "Communication perdue"
        
    if etat_com_interieur == 1:
        etat_com_interieur = "Communication "+u"\u00E9"+"tablie"
    else:
        etat_com_interieur = "Communication perdue"
        
    if etat_com_ext == 1:
        etat_com_ext = "Communication "+u"\u00E9"+"tablie"
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

    label = Label(visu, text="Etat communication capteur ext"+u"\u00E9"+"rieur :", bg = "grey", fg = "white")
    label.config(font=("Courier", 12))
    label.grid(row=1, column=0,columnspan=1)
    etat2 = Label(visu, text=etat_com_ext, bg = "grey", fg = "white")
    etat2.config(font=("Courier", 12))
    etat2.grid(row=1, column=1,columnspan=1)
    
    label = Label(visu, text="Etat communication capteur int"+u"\u00E9"+"rieur :", bg = "grey", fg = "white")
    label.config(font=("Courier", 12))
    label.grid(row=2, column=0,columnspan=1)
    etat3 = Label(visu, text=etat_com_interieur, bg = "grey", fg = "white")
    etat3.config(font=("Courier", 12))
    etat3.grid(row=2, column=1,columnspan=1)

    #bouton de diagnostic
    bouton_fermeture = Button(visu, text="Mise a jour", command=start_diagnostic,width = 14)
    bouton_fermeture.config(font=("Courier", 14))
    bouton_fermeture.grid(row=3, column=1,  rowspan=1,  sticky="ns",pady = 4, padx = 3)
    

    #bouton de fermeture de la page
    bouton_fermeture = Button(bas_page, text="Retour", command=diagnostic_fermer,width = 11)
    bouton_fermeture.config(font=("Courier", 14))
    bouton_fermeture.grid(row=0, column=2,  rowspan=1,  sticky="ns",pady = 4, padx = 3)



#---------------------------------------------------------------------------
def programme_diag():
    fenetre_diagnostic()
