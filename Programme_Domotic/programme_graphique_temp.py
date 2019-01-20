#!/usr/bin/env /usr/bin/python
# coding: utf-8

from tkinter import *
from tkinter import messagebox
import os
import time
import threading
import sqlite3
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


from programme_outil_db import*

###########################################
# Gestion de l heure   
def heure():
    global localdate, labeltps2,tplanning
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
                labeltps2.configure(text= localdate)
                time.sleep(1)
            except:
                break
                
############################################

###########################################
#fermeture de la fenetre suite appui bouton
def graph_fermer():
    global fenetre_graph,tplanning
    #mise a jour de la base
    variable_input = "fermeture"
    variable_etat = 1
    update_db(variable_input, variable_etat)
    #arret thread heure
    tplanning.atuer=True
    fenetre_graph.destroy()


############################
#Remplissage de la base de donnees
def remplisage_heure_bd ():
    chemin_base = os.getcwd()+"/domotic.db"
    while 1:
        try:
            #lecture de la temperature
            variable_input = "temperature_interieur"
            lecture_db(variable_input)
            temperature_interieur= lecture_db(variable_input)
            #lecture de la temperature exterieur
            variable_input = "temperature_exterieur"
            lecture_db(variable_input)
            temperature_exterieur =lecture_db(variable_input)
           
            
            #lecture de l'heure
            variable_input = "heure"
            lecture_db(variable_input)
            heure= lecture_db(variable_input)
            #remplissage de la bd
            with sqlite3.connect(chemin_base) as co_db:
                curseur = co_db.cursor()
                curseur.execute("""UPDATE Temperature SET temperature = ? WHERE heure = ?""", (temperature_interieur,heure,))
            co_db.close()
            heure = heure+100
            with sqlite3.connect(chemin_base) as co_db:
                curseur = co_db.cursor()
                curseur.execute("""UPDATE Temperature SET temperature = ? WHERE heure = ?""", (temperature_exterieur,heure,))
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

           
############################################
def fenetre_graphique():
    chemin_base = os.getcwd()+"/domotic.db"
    
    global labeltps2, tplanning, fenetre_graph
    #fenetre principale
    fenetre_graph = Toplevel()
    fenetre_graph.title('Pilotage de la maison')
    fenetre_graph.resizable(width=FALSE, height=FALSE)

    # get screen width and height
    # calculate x and y coordinates for the Tk root window
    x = (800/2) - (800/2)
    y = (430/2) - (440/2)

    fenetre_graph.geometry('%dx%d+%d+%d' % (800, 432, x, y))

    #entete
    entete = Frame(fenetre_graph, bg='grey', height=50)
    entete.pack(fill = X, pady = 2)

    #frame visu
    visu = Frame(fenetre_graph, bg='grey', height=300)
    visu.pack(fill = X, pady = 2)

    #bas de page
    bas_page = Frame(fenetre_graph, bg='grey', height=50)
    bas_page.pack(fill = X, pady = 2)

    ############################################
    #mise en place des titres
    ############################################
    # demarrage du thread de l heure
    localdate=1  
    labeltps2 = Label(entete, text="", bg = "grey",fg ="white")
    labeltps2.config(font=("Courier", 20))
    labeltps2.grid(row=0, column=0, sticky="nsew")
    tplanning = threading.Thread(target=heure)
    tplanning.start()

    ############################################
    #titre principale de la page
    label = Label(entete, text="Graphique de Température", bg = "grey", fg = "white")
    label.config(font=("Courier", 20))
    label.grid(row=0, column=1, sticky="nsew", ipadx = 150)

    ###########################################
    # Creation de la zonne graphique

    #list temperature interieur
    list_temperature = []
    for i in range (1,25):
        with sqlite3.connect(chemin_base) as co_db:
            curseur = co_db.cursor()
            curseur.execute("""SELECT temperature FROM Temperature WHERE heure=?""", (i,))
            variable_output=(curseur.fetchone()[0])
        co_db.close()
        list_temperature.append(variable_output)
    
    #list temperature exterieur
    list_temperature_ext = []
    for i in range (101,125):
        with sqlite3.connect(chemin_base) as co_db:
            curseur = co_db.cursor()
            curseur.execute("""SELECT temperature FROM Temperature WHERE heure=?""", (i,))
            variable_output=(curseur.fetchone()[0])
        co_db.close()
        list_temperature_ext.append(variable_output)

        
        
    fig = Figure(figsize=(10, 4), dpi=85)
    ax = fig.add_subplot(111)
    ax.plot(range(24), list_temperature, marker="*", label="temperature interieur")
    ax.plot(range(24), list_temperature_ext, marker="*", label="temperature extérieur")
    # Place a legend to the right of this smaller subplot.
    ax.legend(bbox_to_anchor=(1.05, 1), loc='center right', borderaxespad=0.)
    graph = FigureCanvasTkAgg(fig, master=visu)
    canvas = graph.get_tk_widget()
    canvas.grid(row=0, column=0)


    #bouton de fermeture de la page
    bouton_fermeture = Button(bas_page, text="Retour", command=graph_fermer,width = 11)
    bouton_fermeture.config(font=("Courier", 14))
    bouton_fermeture.grid(row=0, column=2,  rowspan=1,  sticky="ns",pady = 4, padx = 3)

    
