
#!/usr/bin/env /usr/bin/python
# coding: utf-8


from tkinter import *
import os
import time
import threading
from datetime import datetime
from PIL import *
import sqlite3
from tkinter import messagebox

from Gestion_heure import*
from programme_planning import*
from programme_communication_chaudiere import*
from programme_communication_temperature import*
from programme_communication_temperature_ext import*
from programme_diagnostic import*
from programme_outil_db import*
from programme_selection_mode_chaudiere import*
from programme_graphique_temp import*
from programme_selection_manu import*
from programme_fenetre_mode_auto import*



###########################################
#liste des pip a installer
#python -m pip install --upgrade pip
#pip install Pillow
#pip install websocket_client
#pip install requests
#pip install matplotlib
###########################################


###########################################
#info db
#variable_input = "etat_chaudiere"
#lecture_db(variable_input)
#etat_chaudiere= lecture_db(variable_input)
#
#variable_input = "etat_chaudiere"
#variable_etat = 0
#update_db(variable_input, variable_etat)
###########################################


###########################################
# mise a jour de la fenetre principale et des
#variables exterieures toute les secondes  
def MaJ_fenetre_main():
    global localdate
    #date et heure pour suivi des erreurs programme
    maintenant = datetime.now()

    #boucle principale du programme
    while 1:
        try:
            #tempo d'actualisation
            time.sleep(0.5)
            
            #mise a jour pour l'heure
            #comptage(localdate)
            heure =[]
            heure= comptage()
            localdate = heure
            #mise a jour label heure
            labeltps.configure(text = localdate)

            #mise a jour affichage des modes de marches
            ecriture_etat_chaudiere()
            
            #mise à jour du niveau de batterie de la temperature exterieur
            #recuperation du niveau sur la base
            variable_input = "niveau_batterie_tempext"
            lecture_db(variable_input)
            niveau_batterie_tempext= lecture_db(variable_input)
            labelbattempext.configure(text = "Batterie : "+str(niveau_batterie_tempext)+"%")
            #changement du logo si plus de batterie
            if niveau_batterie_tempext==0:
                photo2=PhotoImage(file="Hygro_error.png")
                canvas2.itemconfig(item,image = photo2)
                #mise à 0 des valeurs de temp et hygro
                variable_input = "temperature_exterieur"
                variable_etat = 0
                update_db(variable_input, variable_etat)
                variable_input = "hygrometrie_exterieur"
                variable_etat = 0
                update_db(variable_input, variable_etat)

            #changement image suivant etat chaudiere
            #lecture etat chaudiere
            #lecture du mode de marche
            variable_input = "etat_chaudiere_reel"
            lecture_db(variable_input)
            etat= lecture_db(variable_input)
            variable_input = "chaudiere_com_error"
            lecture_db(variable_input)
            chaudiere_com_error= lecture_db(variable_input)
            
            #modification de l'image
            if chaudiere_com_error==0:
                if etat==1:
                    photo5=PhotoImage(file="chaudiere_on.png")
                    canvas5.itemconfig(item,image = photo5)
                if etat==0:   
                    photo5=PhotoImage(file="chaudiere_off.png")
                    canvas5.itemconfig(item,image = photo5)
            else:
                photo5=PhotoImage(file="chaudiere_error.png")
                canvas5.itemconfig(item,image = photo5)               

            #mise a jour des temperatures et hygro
            variable_input = "temperature_exterieur"
            lecture_db(variable_input)
            temperature_exterieur= lecture_db(variable_input)
            #label
            temp_ext_label.configure(text = (str(temperature_exterieur) +u"\u00B0"+"C"))
            
            variable_input = "temperature_interieur"
            lecture_db(variable_input)
            temperature_interieur= lecture_db(variable_input)
            #label
            temp_int_label.configure(text = (str(temperature_interieur) +u"\u00B0"+"C"))

            variable_input = "hygrometrie_exterieur"
            lecture_db(variable_input)
            hygrometrie_exterieur= lecture_db(variable_input)
            #label
            hydro_ext_label.configure(text = (str(hygrometrie_exterieur) +" "+u"\u0025"))
            
            variable_input = "hygrometrie_interieur"
            lecture_db(variable_input)
            hygrometrie_interieur= lecture_db(variable_input)
            #label
            hydro_int_label.configure(text = (str(hygrometrie_interieur) +" "+u"\u0025"))

            #mise à jour du capteur motion
            variable_input = "detection_motion"
            lecture_db(variable_input)
            status_detection= lecture_db(variable_input)
            #mise à jour du label detection
            if status_detection == 1:
                status_motion.configure(text= "Mouvement détecté")
            else :
                status_motion.configure(text= "Mouvement non détecté")
            
            #affichage si erreur com temperature interieur
            variable_input = "temperature_int_error"
            lecture_db(variable_input)
            temperature_int_error= lecture_db(variable_input)
            if temperature_int_error==1:
                photo4=PhotoImage(file="Hygro_error.png")
                canvas4.itemconfig(item,image = photo4)
            if temperature_int_error==0:
                photo4=PhotoImage(file="Hygro.png")
                canvas4.itemconfig(item,image = photo4)           
        except:
            #erreur dans la boucle principale
            print(maintenant, " erreur dans la boucle principale du programme\n")
            time.sleep(0.5)
            #break
            
###########################################
# bouton allumage chaudiere en mode manu
def allumage():
    fenetre_selection_manuel()
    
            
                

###########################################
# bouton allumage chaudiere en mode automatique
def automatique():
    #ouverture de la fenetre de parammetrage
    ouveture_fen_auto_mode ()

###########################################
#Bouton motion
def motion():
        
    #lecture de l'ancien etat
    variable_input = "allumage_motion"
    lecture_db(variable_input)
    allumage_motion = lecture_db(variable_input)

    if allumage_motion==0:
        bouton_motion.config(text = "ON",background ="green")
        variable_input = "allumage_motion"
        variable_etat = 1
        update_db(variable_input, variable_etat)

    if allumage_motion==1:
        bouton_motion.config(text = "OFF",background ="red")
        variable_input = "allumage_motion"
        variable_etat = 0
        update_db(variable_input, variable_etat)



#----------------------------------------------------------
#GESTION DES OUVERTURES FENETRES
###########################################
# affichage du planning
def planning():    
    
    #masquer la fenetre principale
    fenetre.withdraw()
    #thread pour affichage planning
    ouverture_planning()
    t1 = threading.Thread(target=scrutation_fermeture_fenetre)
    t1.start()

###########################################
# affichage fenetre diagnostic
def graph_temp():
    fenetre.withdraw()
    fenetre_graphique()
    t1 = threading.Thread(target=scrutation_fermeture_fenetre)
    t1.start()
    
###########################################
# affichage fenetre diagnostic
def diagnostics():
    fenetre.withdraw()
    programme_diag()
    t1 = threading.Thread(target=scrutation_fermeture_fenetre)
    t1.start()

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

    #mise a jour de la base
    variable_input = "fermeture"
    variable_etat = "0"
    update_db(variable_input, variable_etat)    

#----------------------------------------------------------    


###########################################
# Affichage du mode de marche
def ecriture_etat_chaudiere():
    global etat_mode, tempscompteur
    
    #lecture du mode de marche
    variable_input = "mode_de_marche"
    lecture_db(variable_input)
    mode_de_marche= lecture_db(variable_input)
   
    #recuperation heure
    variable_input = "heure"
    lecture_db(variable_input)
    heure = lecture_db(variable_input)

    if mode_de_marche ==0:
        #mise a jour du label
        etat_mode.configure(text= "Aucun mode \n selectionn"+u"\u00E9")
        #ecriture sur la base
        variable_input = "start_compteur"
        variable_etat = 0
        update_db(variable_input, variable_etat)
        #mise à 1 du debut compteur
        variable_input = "debut_compteur"
        variable_etat = 0
        update_db(variable_input, variable_etat)

    elif mode_de_marche ==4:
        #mise a jour du label
        compteur_manu()
        

    elif mode_de_marche ==1:
        #mise a jour du label
        etat_mode.configure(text= "Mode manuel")
        #ecriture sur la base
        variable_input = "start_compteur"
        variable_etat = 0
        update_db(variable_input, variable_etat)
        #mise à 1 du debut compteur
        variable_input = "debut_compteur"
        variable_etat = 0
        update_db(variable_input, variable_etat)
          
    elif mode_de_marche ==2:
        #mise a jour du label
        etat_mode.configure(text= "Mode \n automatique")
        #ecriture sur la base
        variable_input = "start_compteur"
        variable_etat = 0
        update_db(variable_input, variable_etat)
        #mise à 1 du debut compteur
        variable_input = "debut_compteur"
        variable_etat = 0
        update_db(variable_input, variable_etat)
            
    elif mode_de_marche ==3:
        #lecture de l'etat
        variable_input = "etat_chaudiere"
        lecture_db(variable_input)
        etat_chaudiere= lecture_db(variable_input)
        #ecriture sur la base
        variable_input = "start_compteur"
        variable_etat = 0
        update_db(variable_input, variable_etat)
        #mise à 1 du debut compteur
        variable_input = "debut_compteur"
        variable_etat = 0
        update_db(variable_input, variable_etat)
        if etat_chaudiere == 1:
            #mise a jour du label
            etat_mode.configure(text= "Plannning \n activ"+u"\u00E9")
        else:
            #mise a jour du label
            etat_mode.configure(text= "Plannning \n activ"+u"\u00E9")


###########################################
# Compteur du mode manu temporisée
def compteur_manu ():
    global etat_mode
    #lecture de la tempo sur la base
    variable_input = "tempo_manu"
    lecture_db(variable_input)
    tempo= (lecture_db(variable_input))*3600

    #lecture si demarrage compteur
    variable_input = "debut_compteur"
    lecture_db(variable_input)
    debut = lecture_db(variable_input)
    if debut==0:
        start = int(time.time())
        #ecriture sur la base
        variable_input = "start_compteur"
        variable_etat = start
        update_db(variable_input, variable_etat)
        #mise à 1 du debut compteur
        variable_input = "debut_compteur"
        variable_etat = 1
        update_db(variable_input, variable_etat)
    else:
        #lecture date démarrage
        variable_input = "start_compteur"
        lecture_db(variable_input)
        start_compteur= lecture_db(variable_input)

        actuel= int(time.time())
        #compteur
        tempscompteur = (tempo-(actuel - start_compteur))
        tempscompteurmin = int(tempscompteur/60)
        tempscompteursec = tempscompteur - (tempscompteurmin*60)
        #mise a jour du label
        etat_mode.configure(text= 'Mode manuel: \n '+str(tempscompteurmin)+' : '+str(tempscompteursec))

        if tempscompteur <2:
            #ecriture sur la base
            variable_input = "start_compteur"
            variable_etat = 0
            update_db(variable_input, variable_etat)
            #mise à 1 du debut compteur
            variable_input = "debut_compteur"
            variable_etat = 0
            update_db(variable_input, variable_etat)
            #mode de marche à 0
            variable_input = "mode_de_marche"
            variable_etat = 0
            update_db(variable_input, variable_etat)
            #mode manu à 0
            variable_input = "mode_manu"
            variable_etat = 0
            update_db(variable_input, variable_etat)
            #eteint la chaudiere
            variable_input = "etat_chaudiere"
            variable_etat = 0
            update_db(variable_input, variable_etat)




#---------------------------------------------------------------------
#initialisation des variables

tempint =10
tempext =10
chemin = os.getcwd()+"/"

#mise à 0 de l'etat chaudiere
variable_input = "etat_chaudiere"
variable_etat = 0
update_db(variable_input, variable_etat)
#mise à 0 du mode manu
variable_input = "mode_manu"
variable_etat = 0
update_db(variable_input, variable_etat)
#mise à 0 du mode auto
variable_input = "mode_auto"
variable_etat = 0
update_db(variable_input, variable_etat)
#mise à 0 du mode de marche
variable_input = "mode_de_marche"
variable_etat = 0
update_db(variable_input, variable_etat)
#mise à 1 du mode de marche planning
variable_input = "mode_planning"
variable_etat = 1
update_db(variable_input, variable_etat)
#mise à 0 du mode motion
variable_input = "allumage_motion"
variable_etat = 0
update_db(variable_input, variable_etat)

#fenetre principale
fenetre = Tk()
fenetre.title('Pilotage de la maison')
fenetre.resizable(width=FALSE, height=FALSE)

# get screen width and height
# calculate x and y coordinates for the Tk root window
x = (800/2) - (800/2)
y = (430/2) - (440/2)
fenetre.geometry('%dx%d+%d+%d' % (798, 432, x, y))

#entete
entete = Frame(fenetre, bg='#4584b6', height=50)
entete.pack(fill = X, pady = 2)

#frame visu
visu = Frame(fenetre, bg='#ffde57', height=300)
visu.pack(fill = X, pady = 2)

#frame inferieure
frame_inf = Frame(fenetre, bg='#4584b6', height=50)
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
labeltps = Label(entete, text="00:00:00", bg = "#4584b6",fg ="white")
labeltps.config(font=("Courier", 20))
labeltps.grid(row=0, column=0, sticky="nsew")

#titre principale de la page
label = Label(entete, text="Gestion de la temp"+u"\u00E9"+"rature", bg = "#4584b6", fg = "white")
label.config(font=("Courier", 20))
label.grid(row=0, column=1, sticky="nsew", ipadx = 75)

#remplissage des frames
#1
#titre frame
label = Label(temp_ext,text="Temp"+u"\u00E9"+"rature \n ext"+u"\u00E9"+"rieure",bg = "white",width = 12)
label.config(font=("Courier", 14))
label.grid(row=0, column=1,  columnspan=1, sticky="e")
#image frame
photo1 = PhotoImage(file=chemin+"Thermo1.png")
canvas1 = Canvas(temp_ext,width=photo1.width(), height=photo1.height(),bg = "white",highlightthickness=0)
canvas1.create_image(40, 70, image=photo1)
canvas1.grid(row=0, column=0,rowspan=2, sticky="nsew")
#valeur frame
temp_ext_label = Label(temp_ext,text="10"+u"\u00B0",bg = "white",foreground="blue")
temp_ext_label.config(font=("Courier", 35))
temp_ext_label.grid(row=1, column=1, sticky="nsew")

#2
#titre frame
label = Label(hydro_ext,text="Hygrom"+u"\u00E9"+"trie \n ext"+u"\u00E9"+"rieure",bg = "white",width = 12)
label.config(font=("Courier", 14))
label.grid(row=0, column=1,  columnspan=1, sticky="nsew")
#image frame
photo2 = PhotoImage(file=chemin+"Hygro.png")
canvas2 = Canvas(hydro_ext,width=photo2.width(), height=130,bg = "white",highlightthickness=0)
canvas2.create_image(40,60, image=photo2)
canvas2.grid(row=0, column=0,rowspan=2, sticky="nsew")
#valeur frame
hydro_ext_label = Label(hydro_ext,text="100%",bg = "white",foreground="blue")
hydro_ext_label.config(font=("Courier", 35))
hydro_ext_label.grid(row=1, column=1, sticky="nsew")
#affichage batterie
labelbattempext = Label(hydro_ext,text="Batterie : 0%",bg = "white",width = 12)
labelbattempext.config(font=("Courier", 10))
labelbattempext.grid(row=2, column=1,  columnspan=1, sticky="nsew")

#3
#titre frame
label = Label(temp_int,text="Temp"+u"\u00E9"+"rature \n int"+u"\u00E9"+"rieure",bg = "white",width = 12)
label.config(font=("Courier", 14))
label.grid(row=0, column=1,  columnspan=1, sticky="nsew")
#image frame
photo = PhotoImage(file=chemin+"Thermo1.png")
canvas = Canvas(temp_int,width=photo.width(), height=photo.height(),bg = "white",highlightthickness=0)
canvas.create_image(40, 70, image=photo)
canvas.grid(row=0, column=0,rowspan =2, sticky="nsew")
#valeur frame
temp_int_label = Label(temp_int,text="10"+u"\u00B0",bg = "white",foreground="blue")
temp_int_label.config(font=("Courier", 35))
temp_int_label.grid(row=1, column=1, sticky="nsew")

#4
#titre frame
label = Label(hydro_int,text="Hygrom"+u"\u00E9"+"trie \n  int"+u"\u00E9"+"rieure",bg = "white",width = 12)
label.config(font=("Courier", 14))
label.grid(row=0, column=1,  columnspan=1, sticky="nsew")
#image frame
photo4 = PhotoImage(file=chemin+"Hygro.png")
canvas4 = Canvas(hydro_int,width=photo4.width(), height=130,bg = "white",highlightthickness=0)
canvas4.create_image(40,60, image=photo4)
canvas4.grid(row=0, column=0,rowspan=2, sticky="nsew")
#valeur frame
hydro_int_label = Label(hydro_int,text="100%",bg = "white",foreground="blue")
hydro_int_label.config(font=("Courier", 35))
hydro_int_label.grid(row=1, column=1, sticky="nsew")

#5
mode_marche ="Aucun mode \n selectionn"+u"\u00E9"
#titre frame
label = Label(etat_chaudiere,text="Fonctionnement \n chaudi"+u"\u00E8"+"re",bg = "white",width = 18)
label.config(font=("Courier", 14))
label.grid(row=0, column=0,  columnspan=2, sticky="nsew")
#image d'etat
photo5 = PhotoImage(file=chemin+"chaudiere_off.png")
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
label = Label(etat_chauffage,text="Activation \n détection",bg = "white",width = 18)
label.config(font=("Courier", 14))
label.grid(row=0, column=0,  columnspan=1, sticky="nsew")
#BP allumage de la détection de présence
bouton_motion = Button(etat_chauffage, text="OFF",background ="red", command=motion,height = 1,width = 15)
bouton_motion.config(font=("Courier", 15))
bouton_motion.grid(row=1, column=0,  rowspan=1,  sticky="ns",pady = 4, padx = 3)
#status
status_motion = Label(etat_chauffage,text="Statut : Inactive",bg = "white",foreground = "blue",width = 18)
status_motion.config(font=("Courier", 11))
status_motion.grid(row=3, column=0,  columnspan=1, sticky="nsew")


#frame commandes
#label de la zone commande
label_command = Label(action_bp,text="Chaudi"+u"\u00E8"+"re",bg = "white",width = 12)
label_command.config(font=("Courier", 14))
label_command.grid(row=0, column=0,  columnspan=1, sticky="nsew")
#BP allumage de la chaudiere
bouton_chaudiere = Button(action_bp, text="Forcage \n manuel", command=allumage,height = 3,width = 12)
bouton_chaudiere.config(font=("Courier", 13))
bouton_chaudiere.grid(row=1, column=0,  rowspan=1,  sticky="ns",pady = 4, padx = 3)
#BP planning de la chaudiere
bouton_chaudiere = Button(action_bp, text="Planning \n chaudi"+u"\u00E8"+"re", command=planning,height = 3,width = 12)
bouton_chaudiere.config(font=("Courier", 13))
bouton_chaudiere.grid(row=2, column=0,  rowspan=1, sticky="nsew",pady = 4, padx = 3)
#BP mode automatique de la chaudiere
bouton_chaudiere = Button(action_bp, text="Mode \n automatique", command=automatique,height = 3, width = 12)
bouton_chaudiere.config(font=("Courier", 13))
bouton_chaudiere.grid(row=3, column=0,  rowspan=1, sticky="nsew",pady = 4, padx = 3)

#Frame inferieure
#BP diagnostic
bouton_diagnostic = Button(frame_inf, text="Diagnostics", command=diagnostics,height = 2,width = 11)
bouton_diagnostic.config(font=("Courier", 11))
bouton_diagnostic.grid(row=1, column=0,  rowspan=1,  sticky="ns",pady = 4, padx = 3)


#BP graphique de température
bouton_diagnostic = Button(frame_inf, text="Graphique\n Température", command=graph_temp,height = 2,width = 11)
bouton_diagnostic.config(font=("Courier", 11), width=12)
bouton_diagnostic.grid(row=1, column=3,  rowspan=1,  sticky="ns",pady = 4, padx = 3)






#affichage de l'historique planning
#prise en compte des modification du planning
#lecture de l'activation du mode planning

############################################
# demarrage surveillance mode de marche
changement_etat_chaudiere()
############################################
############################################
# Mise a jour reguliere de la fenetre
t1 = threading.Thread(target=MaJ_fenetre_main)
t1.start()

############################################
############################################
# demarrage communication avec chaudiere
com_esp_chaudiere()
############################################

############################################
# demarrage communication avec temperature int
com_esp_temperature()
############################################

############################################
# demarrage communication avec temperature int
com_esp_temperature_ext()
############################################

############################################
# demarrage enregistrement des temperature
Thread_remplissage_heure()
############################################

fenetre.mainloop()


