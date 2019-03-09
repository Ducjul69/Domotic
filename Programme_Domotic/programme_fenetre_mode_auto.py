#!/usr/bin/env /usr/bin/python
# coding: utf-8

from tkinter import *
import os
import time
import threading

from programme_outil_db import*
from programme_allumage_auto import*

############################################
#fermeture de la fenetre suite appui bouton  
def activer_mode_auto():
    global fenetre_auto
    programme_auto()
    fenetre_auto.destroy()
    
   



############################################
#fermeture de la fenetre suite appui bouton  
def fenetre_auto_fermer():
    global fenetre_auto
    
    fenetre_auto.destroy()

############################################
def augmentation_ext():
	global seuil_temp_ext, label_seuil_ext 
	seuil_temp_ext=seuil_temp_ext + 1
	#ecriture sur la base de la nouvelle valeur
	variable_input = "seuil_temp_ext"
	variable_etat = seuil_temp_ext
	update_db(variable_input, variable_etat)
	#mise à jour du label
	label_seuil_ext.configure(text = seuil_temp_ext )


############################################
def diminution_ext():
	global seuil_temp_ext, label_seuil_ext 
	seuil_temp_ext= seuil_temp_ext - 1
	#ecriture sur la base de la nouvelle valeur
	variable_input = "seuil_temp_ext"
	variable_etat = seuil_temp_ext
	update_db(variable_input, variable_etat)
	#mise à jour du label
	label_seuil_ext.configure(text = seuil_temp_ext )


############################################
def augmentation_int():
	global seuil_temp_int, label_seuil_int 
	seuil_temp_int=seuil_temp_int + 1
	#ecriture sur la base de la nouvelle valeur
	variable_input = "seuil_temp_int"
	variable_etat = seuil_temp_int
	update_db(variable_input, variable_etat)
	#mise à jour du label
	label_seuil_int.configure(text = seuil_temp_int )


############################################
def diminution_int():
	global seuil_temp_int, label_seuil_int 
	seuil_temp_int= seuil_temp_int - 1
	#ecriture sur la base de la nouvelle valeur
	variable_input = "seuil_temp_int"
	variable_etat = seuil_temp_int
	update_db(variable_input, variable_etat)
	#mise à jour du label
	label_seuil_int.configure(text = seuil_temp_int )


############################################
def ouveture_fen_auto_mode ():
	global fenetre_auto, seuil_temp_ext, seuil_temp_int, label_seuil_ext , label_seuil_int


	#récuperations des seuils de température
	variable_input = "seuil_temp_ext"
	lecture_db(variable_input)
	seuil_temp_ext= lecture_db(variable_input)
	#récuperations des seuils de température
	variable_input = "seuil_temp_int"
	lecture_db(variable_input)
	seuil_temp_int= lecture_db(variable_input)
	#récupération etat du mode auto
	variable_input = "mode_auto"
	lecture_db(variable_input)
	mode_auto= lecture_db(variable_input)
	if mode_auto==1:
		label_bouton = "Arrêter mode \n automatique"
	else:
		label_bouton = "Activer mode \n automatique"

	
	#fenetre secondaire
	fenetre_auto = Toplevel()
	fenetre_auto.title('Pilotage de la maison')
	fenetre_auto.resizable(width=FALSE, height=FALSE)
	# get screen width and height
	# calculate x and y coordinates for the Tk root window

	x = 225
	y = 30

	fenetre_auto.geometry('%dx%d+%d+%d' % (410, 340, x, y))

	#entete
	entete = Frame(fenetre_auto, bg='#ffde57', height=50)
	entete.pack(fill = X, pady = 2)

	#frame visu
	visu = Frame(fenetre_auto, bg='#4584b6', height=300)
	visu.pack(fill = X, pady = 2)

	#bas de page
	bas_page = Frame(fenetre_auto, bg='#ffde57', height=50)
	bas_page.pack(fill = X, pady = 2)

	############################################
	#mise en place des titres
	############################################

	############################################
	#titre principale de la page
	label = Label(entete, text="Paramètrage mode auto", bg = "#ffde57", fg = "black")
	label.config(font=("Courier", 20))
	label.grid(row=0, column=1, sticky="nsew", padx = 20)

    
	############################################
	#zone principale
	#partie temperature exterieure
	label = Label(visu, text="Seuil de température \n extérieure" , bg = "#4584b6", fg = "white")
	label.config(font=("Courier", 12))
	label.grid(row=0,column=0, rowspan=2, sticky="nsew",padx= 10)
	label_seuil_ext = Label(visu, text=seuil_temp_ext , bg = "#4584b6", fg = "white")
	label_seuil_ext .config(font=("Courier", 20))
	label_seuil_ext .grid(row=0,column=1, rowspan=2, sticky="nsew",padx= 10)
	#bouton augmentation 
	bouton_augmentation = Button(visu, text="+", command=augmentation_ext)
	bouton_augmentation.config(font=("Courier", 20))
	bouton_augmentation.grid(row=0, column=2,  sticky="nsew",pady = 0, padx = 10)   
	#bouton diminution
	bouton_diminution = Button(visu, text="-", command=diminution_ext)
	bouton_diminution.config(font=("Courier", 20))
	bouton_diminution.grid(row=1, column=2,   sticky="nsew",pady = 0, padx = 10)
	#partie temperature interieure
	label = Label(visu, text="Seuil de température \n intérieure" , bg = "#4584b6", fg = "white")
	label.config(font=("Courier", 12))
	label.grid(row=2,column=0, rowspan=2, sticky="nsew",padx= 10)
	label_seuil_int = Label(visu, text=seuil_temp_int , bg = "#4584b6", fg = "white")
	label_seuil_int .config(font=("Courier", 20))
	label_seuil_int .grid(row=2,column=1, rowspan=2, sticky="nsew",padx= 10)
	#bouton augmentation 
	bouton_augmentation = Button(visu, text="+", command=augmentation_int)
	bouton_augmentation.config(font=("Courier", 20))
	bouton_augmentation.grid(row=2, column=2,  sticky="nsew",pady = 0, padx = 10)   
	#bouton diminution
	bouton_diminution = Button(visu, text="-", command=diminution_int)
	bouton_diminution.config(font=("Courier", 20))
	bouton_diminution.grid(row=3, column=2,   sticky="nsew",pady = 0, padx = 10)

	###########################################
	#zone BP bas
	#bouton de fermeture de la page
	bouton_fermeture = Button(bas_page, text="Retour", command=fenetre_auto_fermer,width = 11)
	bouton_fermeture.config(font=("Courier", 14))
	bouton_fermeture.grid(row=0, column=2,  rowspan=1,  sticky="ns",pady = 4, padx = 40)
	bouton_activer = Button(bas_page, text=label_bouton, command=activer_mode_auto,width = 13)
	bouton_activer.config(font=("Courier", 14))
	bouton_activer.grid(row=0, column=3,  rowspan=1,  sticky="nsew",pady = 4, padx = 1)
