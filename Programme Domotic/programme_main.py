#!/usr/bin/env /usr/bin/python

from tkinter import *
import os
import time
import threading
from datetime import datetime
from PIL import Image,ImageTk
import sqlite3


from Gestion_heure import*
from programme_planning import*
from programme_allumage_auto import*
from programme_communication_chaudiere import*
from programme_communication_temperature import*
from programme_diagnostic import*
from programme_outil_db import*
from programme_selection_mode_chaudiere import*
from programme_IO_adafruit import*


###########################################
# info db
#variable_input = "etat_chaudiere"
#lecture_db(variable_input)
#etat_chaudiere= lecture_db(variable_input)

#variable_input = "etat_chaudiere"
#variable_etat = 0
#update_db(variable_input, variable_etat)



###########################################
# Mise à jour de la fenetre principale et des
#variables exterieures toute les secondes  
def MaJ_fenetre_main():
    global localdate
    while 1:
        #mise à jour pour l'heure
        #comptage(localdate)
        heure =[]
        heure= comptage()
        localdate = heure
        #mise à jour label heure
        labeltps.configure(text = localdate)

        #mise à jour des modes de marches
        ecriture_etat_chaudiere()

        #mise à jour des températures et hygro
        variable_input = "temperature_exterieur"
        lecture_db(variable_input)
        temperature_exterieur= lecture_db(variable_input)
        #label
        temp_ext_label.configure(text = (str(temperature_exterieur) +" °C"))
        
        variable_input = "temperature_interieur"
        lecture_db(variable_input)
        temperature_interieur= lecture_db(variable_input)
        #label
        temp_int_label.configure(text = (str(temperature_interieur) +" °C"))
        
        variable_input = "hygrometrie_exterieur"
        lecture_db(variable_input)
        hygrometrie_exterieur= lecture_db(variable_input)
        #label
        hydro_ext_label.configure(text = (str(hygrometrie_exterieur) +" %"))
        
        variable_input = "hygrometrie_interieur"
        lecture_db(variable_input)
        hygrometrie_interieur= lecture_db(variable_input)
        #label
        hydro_int_label.configure(text = (str(hygrometrie_interieur) +" %"))
           
###########################################
# bouton allumage chaudiere en mode manu
def allumage():
    #lecture de l'ancien etat
    variable_input = "mode_manu"
    lecture_db(variable_input)
    mode_manu = lecture_db(variable_input)
        
    if mode_manu == 1:
        #ecriture sur la db manu =0
        variable_input = "mode_manu"
        variable_etat = 0
        update_db(variable_input, variable_etat)
    else:
        #ecriture sur la db manu =1
        variable_input = "mode_manu"
        variable_etat = 1
        update_db(variable_input, variable_etat)
        
            
                

###########################################
# bouton allumage chaudiere en mode automatique
def automatique():
    #lecture de l'ancien etat
    variable_input = "mode_auto"
    lecture_db(variable_input)
    mode_auto = lecture_db(variable_input)
        
    if mode_auto == 1:
        #ecriture sur la db manu =0
        variable_input = "mode_auto"
        variable_etat = 0
        update_db(variable_input, variable_etat)
    else:
        #ecriture sur la db manu =1
        variable_input = "mode_auto"
        variable_etat = 1
        update_db(variable_input, variable_etat)

            

###########################################
# scrutation fin des autres pages
def scrutation_fermeture_fenetre():
    fermeture = 0
    variable_input = "fermeture"
    while fermeture == 0:
        lecture_db(variable_input)
        fermeture= lecture_db(variable_input)
    fenetre.update()    
    fenetre.deiconify()

    #mise à jour de la base
    variable_input = "fermeture"
    variable_etat = "0"
    update_db(variable_input, variable_etat)    


###########################################
# affichage du planning
def planning():    
    #thread pour affichage planning
    ouverture_planning()
    t1 = threading.Thread(target=scrutation_fermeture_fenetre)
    t1.start()
    #masquer la fenetre principale
    fenetre.withdraw()

###########################################


###########################################
# affichage fenetre diagnostic
def diagnostics():
    programme_diag()
    t1 = threading.Thread(target=scrutation_fermeture_fenetre)
    t1.start()
    fenetre.withdraw()


###########################################
# gestion de l'allumage chaudiere global
def ecriture_etat_chaudiere():
    global photo5, etat_mode
    #lecture du mode de marche
    variable_input = "mode_de_marche"
    lecture_db(variable_input)
    mode_de_marche= lecture_db(variable_input)
   
    #recuperation heure
    variable_input = "heure"
    lecture_db(variable_input)
    heure = lecture_db(variable_input)

    if mode_de_marche ==0:
        #modification de l'image
        photo5=PhotoImage(file="chaudiere_off.png")
        canvas5.itemconfig(item,image = photo5)
        #mise a jour du label
        etat_mode.configure(text= "Aucun mode \n selectionné")
            
    elif mode_de_marche ==1:
        #modification de l'image
        photo5=PhotoImage(file="chaudiere_on.png")
        canvas5.itemconfig(item,image = photo5)
        #mise a jour du label
        etat_mode.configure(text= "Mode manuel")
            
    elif mode_de_marche ==2:
        #modification de l'image
        photo5=PhotoImage(file="chaudiere_on.png")
        canvas5.itemconfig(item,image = photo5)
        #mise a jour du label
        etat_mode.configure(text= "Mode \n automatique")
            
    elif mode_de_marche ==3:
        #lecture de l'état
        variable_input = "etat_chaudiere"
        lecture_db(variable_input)
        etat_chaudiere= lecture_db(variable_input)
        if etat_chaudiere == 1:
            #modification de l'image
            photo5=PhotoImage(file="chaudiere_on.png")
            canvas5.itemconfig(item,image = photo5)
            #mise a jour du label
            etat_mode.configure(text= "Plannning \n activé")
        else:
            #modification de l'image
            photo5=PhotoImage(file="chaudiere_off.png")
            canvas5.itemconfig(item,image = photo5)
            #mise a jour du label
            etat_mode.configure(text= "Plannning \n activé")

        

#---------------------------------------------------------------------
#initialisation des variables

tempint =10
tempext =10

#fenetre principale
fenetre = Tk()
fenetre.title('Pilotage de la maison')
fenetre.resizable(width=FALSE, height=FALSE)
fenetre.geometry('{}x{}'.format(800, 400))

#entete
entete = Frame(fenetre, bg='grey', height=50)
entete.pack(fill = X, pady = 2)

#frame visu
visu = Frame(fenetre, bg='grey', height=300)
visu.pack(fill = X, pady = 2)

#frame inferieure
frame_inf = Frame(fenetre, bg='grey', height=50)
frame_inf.pack(fill = X, pady = 2)

#organisation de la frame visu
temp_ext = Frame(visu, bg='white', width=200,height = 150)
hydro_ext = Frame(visu, bg='white', width=200,height = 150)
temp_int = Frame(visu, bg='white', width=200,height = 150)
hydro_int = Frame(visu, bg='white', width=200,height = 150)
etat_chaudiere = Frame(visu, bg='white', width=200,height = 150)
etat_chauffage =Frame(visu, bg='white', width=200,height = 150)
action_bp = Frame(visu, bg='white', width=200,height = 150)

temp_ext.grid(row=0, column=0, sticky="nsew", pady = 5, padx = 5)
hydro_ext.grid(row=0, column=1, sticky="nsew", pady = 5, padx = 5)
temp_int.grid(row=1, column=0, sticky="nsew", pady = 5, padx = 5)
hydro_int.grid(row=1, column=1, sticky="nsew", pady = 5, padx = 5)
etat_chaudiere.grid(row=0, column=2, sticky="nsew", pady = 5, padx = 5)
etat_chauffage.grid(row=1, column=2, sticky="nsew", pady = 5, padx = 5)
action_bp.grid(row = 0, rowspan=2, column=3, sticky="nsew", pady = 5, padx = 5)

############################################
#mise en place des titres
############################################

# Affichage de l'heure
localdate=0  
labeltps = Label(entete, text="00:00:00", bg = "grey",fg ="white")
labeltps.config(font=("Courier", 20))
labeltps.grid(row=0, column=0, sticky="nsew")

#titre principale de la page
label = Label(entete, text="Gestion de la température", bg = "grey", fg = "white")
label.config(font=("Courier", 20))
label.grid(row=0, column=1, sticky="nsew", ipadx = 75)

#remplissage des frames
#1
#titre frame
label = Label(temp_ext,text="Température \n extérieure",bg = "white",width = 12)
label.config(font=("Courier", 14))
label.grid(row=0, column=1,  columnspan=1, sticky="e")
#image frame
photo1 = PhotoImage(file="Thermo1.png")
canvas1 = Canvas(temp_ext,width=photo1.width(), height=photo1.height(),bg = "white",highlightthickness=0)
canvas1.create_image(40, 70, image=photo1)
canvas1.grid(row=0, column=0,rowspan=2, sticky="nsew")
#valeur frame
temp_ext_label = Label(temp_ext,text="10°",bg = "white")
temp_ext_label.config(font=("Courier", 30))
temp_ext_label.grid(row=1, column=1, sticky="nsew")

#2
#titre frame
label = Label(hydro_ext,text="Hygrométrie \n extérieure",bg = "white",width = 12)
label.config(font=("Courier", 14))
label.grid(row=0, column=1,  columnspan=1, sticky="nsew")
#image frame
photo2 = PhotoImage(file="Hygro.png")
canvas2 = Canvas(hydro_ext,width=photo2.width(), height=130,bg = "white",highlightthickness=0)
canvas2.create_image(40,60, image=photo2)
canvas2.grid(row=0, column=0,rowspan=2, sticky="nsew")
#valeur frame
hydro_ext_label = Label(hydro_ext,text="100%",bg = "white")
hydro_ext_label.config(font=("Courier", 30))
hydro_ext_label.grid(row=1, column=1, sticky="nsew")

#3
#titre frame
label = Label(temp_int,text="Température \n intérieure",bg = "white",width = 12)
label.config(font=("Courier", 14))
label.grid(row=0, column=1,  columnspan=1, sticky="nsew")
#image frame
photo = PhotoImage(file="Thermo1.png")
canvas = Canvas(temp_int,width=photo.width(), height=photo.height(),bg = "white",highlightthickness=0)
canvas.create_image(40, 70, image=photo)
canvas.grid(row=0, column=0,rowspan =2, sticky="nsew")
#valeur frame
temp_int_label = Label(temp_int,text="10°",bg = "white")
temp_int_label.config(font=("Courier", 30))
temp_int_label.grid(row=1, column=1, sticky="nsew")

#4
#titre frame
label = Label(hydro_int,text="Hygrométrie \n  intérieure",bg = "white",width = 12)
label.config(font=("Courier", 14))
label.grid(row=0, column=1,  columnspan=1, sticky="nsew")
#image frame
photo4 = PhotoImage(file="Hygro.png")
canvas4 = Canvas(hydro_int,width=photo4.width(), height=130,bg = "white",highlightthickness=0)
canvas4.create_image(40,60, image=photo4)
canvas4.grid(row=0, column=0,rowspan=2, sticky="nsew")
#valeur frame
hydro_int_label = Label(hydro_int,text="100%",bg = "white")
hydro_int_label.config(font=("Courier", 30))
hydro_int_label.grid(row=1, column=1, sticky="nsew")

#5
mode_marche ="Aucun mode \n selectionné"
#titre frame
label = Label(etat_chaudiere,text="Fonctionnement \n chaudière",bg = "white",width = 18)
label.config(font=("Courier", 14))
label.grid(row=0, column=0,  columnspan=2, sticky="nsew")
#image d'état
photo5 = PhotoImage(file="chaudiere_off.png")
canvas5 = Canvas(etat_chaudiere,width=photo5.width(), height=85,bg = "white",highlightthickness=0)
item=canvas5.create_image(45,42, image=photo5)
canvas5.grid(row=1, column=0,rowspan=2, sticky="nsew")
#mode de marche
label = Label(etat_chaudiere,text="Mode \n de marche",bg = "white",width = 11)
label.config(font=("Courier", 11))
label.grid(row=1, column=1,  columnspan=1, sticky="nsew")
#etat du mode de marche
etat_mode = Label(etat_chaudiere,text=mode_marche, bg = "white", fg = "blue",width = 11)
etat_mode.config(font=("Courier", 11))
etat_mode.grid(row=2, column=1,  columnspan=1, sticky="nsew")

#6
#titre frame
label = Label(etat_chauffage,text="Fonctionnement \n chauffage",bg = "white",width = 18)
label.config(font=("Courier", 14))
label.grid(row=0, column=0,  columnspan=1, sticky="nsew")

#frame commandes
#label de la zone commande
label_command = Label(action_bp,text="Chaudière",bg = "white",width = 10)
label_command.config(font=("Courier", 13))
label_command.grid(row=0, column=0,  columnspan=1, sticky="nsew")
#BP allumage de la chaudiere
bouton_chaudiere = Button(action_bp, text="Forcage \n manuel", command=allumage,height = 3,width = 11)
bouton_chaudiere.config(font=("Courier", 13))
bouton_chaudiere.grid(row=1, column=0,  rowspan=1,  sticky="ns",pady = 4, padx = 3)
#BP planning de la chaudiere
bouton_chaudiere = Button(action_bp, text="Planning \n chaudiere", command=planning,height = 3,width = 11)
bouton_chaudiere.config(font=("Courier", 13))
bouton_chaudiere.grid(row=2, column=0,  rowspan=1, sticky="nsew",pady = 4, padx = 3)
#BP mode automatique de la chaudiere
bouton_chaudiere = Button(action_bp, text="Mode \n automatique", command=automatique,height = 3, width = 11)
bouton_chaudiere.config(font=("Courier", 13))
bouton_chaudiere.grid(row=3, column=0,  rowspan=1, sticky="nsew",pady = 4, padx = 3)

#Frame inférieure
#BP diagnostic
bouton_diagnostic = Button(frame_inf, text="Diagnostics", command=diagnostics,height = 2,width = 11)
bouton_diagnostic.config(font=("Courier", 11))
bouton_diagnostic.grid(row=1, column=0,  rowspan=1,  sticky="ns",pady = 4, padx = 3)







#affichage de l'historique planning
#prise en compte des modification du planning
#lecture de l'activation du mode planning


############################################
# démarrage surveillance mode de marche
changement_etat_chaudiere()
############################################
############################################
# Mise à jour régulière de la fenetre
t1 = threading.Thread(target=MaJ_fenetre_main)
t1.start()
############################################
############################################
# démarrage communication avec serveur
adafruit()

############################################
############################################
# démarrage communication avec chaudière
com_esp_chaudiere()
############################################

############################################
# démarrage communication avec temperature
com_esp_temperature()
############################################

fenetre.mainloop()


