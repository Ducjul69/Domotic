#!/usr/bin/env /usr/bin/python
# coding: utf-8

from tkinter import *
import os
import time
import threading
import sys
from datetime import datetime
from PIL import *

from programme_outil_db import*


###########################################
# Gestion de l'heure   
def planning_comptage():
    global localdate, labeltps1
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
            error=1
###########################################
# recuperation
def recup(jour):
    global list_check
    h=1
    if jour ==1:
        for i in list_check:
            
            with sqlite3.connect('domotic.db') as co_db:
                curseur = co_db.cursor()
                curseur.execute("""SELECT Lundi FROM Planning WHERE Heure=?""", (h,))
                variable_output=(curseur.fetchone()[0])
                if variable_output==1:
                    i.select()
                if variable_output==0:
                    i.deselect()
            co_db.close()
            h=h+1
    if jour ==2:
        h=1
        for i in list_check:
            
            with sqlite3.connect('domotic.db') as co_db:
                curseur = co_db.cursor()
                curseur.execute("""SELECT Mardi FROM Planning WHERE Heure=?""", (h,))
                variable_output=(curseur.fetchone()[0])
                if variable_output==1:
                    i.select()
                if variable_output==0:
                    i.deselect()
            co_db.close()
            h=h+1
    if jour ==3:
        h=1
        for i in list_check:
            
            with sqlite3.connect('domotic.db') as co_db:
                curseur = co_db.cursor()
                curseur.execute("""SELECT Mercredi FROM Planning WHERE Heure=?""", (h,))
                variable_output=(curseur.fetchone()[0])
                if variable_output==1:
                    i.select()
                if variable_output==0:
                    i.deselect()
            co_db.close()
            h=h+1
    if jour ==4:
        h=1
        for i in list_check:
            
            with sqlite3.connect('domotic.db') as co_db:
                curseur = co_db.cursor()
                curseur.execute("""SELECT Jeudi FROM Planning WHERE Heure=?""", (h,))
                variable_output=(curseur.fetchone()[0])
                if variable_output==1:
                    i.select()
                if variable_output==0:
                    i.deselect()
            co_db.close()
            h=h+1
    if jour ==5:
        h=1
        for i in list_check:
            
            with sqlite3.connect('domotic.db') as co_db:
                curseur = co_db.cursor()
                curseur.execute("""SELECT Vendredi FROM Planning WHERE Heure=?""", (h,))
                variable_output=(curseur.fetchone()[0])
                if variable_output==1:
                    i.select()
                if variable_output==0:
                    i.deselect()
            co_db.close()
            h=h+1
    if jour ==6:
        h=1
        for i in list_check:
            
            with sqlite3.connect('domotic.db') as co_db:
                curseur = co_db.cursor()
                curseur.execute("""SELECT Samedi FROM Planning WHERE Heure=?""", (h,))
                variable_output=(curseur.fetchone()[0])
                if variable_output==1:
                    i.select()
                if variable_output==0:
                    i.deselect()
            co_db.close()
            h=h+1
    if jour ==7:
        h=1
        for i in list_check:
            
            with sqlite3.connect('domotic.db') as co_db:
                curseur = co_db.cursor()
                curseur.execute("""SELECT Dimanche FROM Planning WHERE Heure=?""", (h,))
                variable_output=(curseur.fetchone()[0])
                if variable_output==1:
                    i.select()
                if variable_output==0:
                    i.deselect()
            co_db.close()
            h=h+1
    if jour ==8:
        h=1
        for i in list_check:
            
            with sqlite3.connect('domotic.db') as co_db:
                curseur = co_db.cursor()
                curseur.execute("""SELECT Semaine FROM Planning WHERE Heure=?""", (h,))
                variable_output=(curseur.fetchone()[0])
                if variable_output==1:
                    i.select()
                if variable_output==0:
                    i.deselect()
            co_db.close()
            h=h+1

###########################################
# jour1
def lundi():
    global var_check,bouton_lundi,bouton_mardi,bouton_mercredi,bouton_jeudi,bouton_vendredi,bouton_semaine,bouton_samedi,bouton_dimanche
    #ecriture de la variable sur la base
    variable_input = "planning_jour"
    variable_etat = 1
    update_db(variable_input, variable_etat)
    #modifier couleur bouton
    bouton_lundi.configure(bg = 'green')
    bouton_mardi.configure(bg = 'red')
    bouton_mercredi.configure(bg = 'red')
    bouton_jeudi.configure(bg = 'red')
    bouton_vendredi.configure(bg = 'red')
    bouton_samedi.configure(bg = 'red')
    bouton_dimanche.configure(bg = 'red')
    bouton_semaine.configure(bg = 'red')
    jour=1
    recup(jour)

###########################################
# jour1
def mardi():
    global labeltps1,var_check,bouton_lundi,bouton_mardi,bouton_mercredi,bouton_jeudi,bouton_vendredi,bouton_semaine,bouton_samedi,bouton_dimanche
    #ecriture de la variable sur la base
    variable_input = "planning_jour"
    variable_etat = 2
    update_db(variable_input, variable_etat)
    #modifier couleur bouton
    bouton_lundi.configure(bg = 'red')
    bouton_mardi.configure(bg = 'green')
    bouton_mercredi.configure(bg = 'red')
    bouton_jeudi.configure(bg = 'red')
    bouton_vendredi.configure(bg = 'red')
    bouton_samedi.configure(bg = 'red')
    bouton_dimanche.configure(bg = 'red')
    bouton_semaine.configure(bg = 'red')
    jour=2
    recup(jour)

###########################################
# jour1
def mercredi():
    global var_check,bouton_lundi,bouton_mardi,bouton_mercredi,bouton_jeudi,bouton_vendredi,bouton_semaine,bouton_samedi,bouton_dimanche
    #ecriture de la variable sur la base
    variable_input = "planning_jour"
    variable_etat = 3
    update_db(variable_input, variable_etat)
    #modifier couleur bouton
    bouton_lundi.configure(bg = 'red')
    bouton_mardi.configure(bg = 'red')
    bouton_mercredi.configure(bg = 'green')
    bouton_jeudi.configure(bg = 'red')
    bouton_vendredi.configure(bg = 'red')
    bouton_samedi.configure(bg = 'red')
    bouton_dimanche.configure(bg = 'red')
    bouton_semaine.configure(bg = 'red')
    jour=3
    recup(jour)
    

###########################################
# jour1
def jeudi():
    global var_check,bouton_lundi,bouton_mardi,bouton_mercredi,bouton_jeudi,bouton_vendredi,bouton_semaine,bouton_samedi,bouton_dimanche
    #ecriture de la variable sur la base
    variable_input = "planning_jour"
    variable_etat = 4
    update_db(variable_input, variable_etat)
    #modifier couleur bouton
    bouton_lundi.configure(bg = 'red')
    bouton_mardi.configure(bg = 'red')
    bouton_mercredi.configure(bg = 'red')
    bouton_jeudi.configure(bg = 'green')
    bouton_vendredi.configure(bg = 'red')
    bouton_samedi.configure(bg = 'red')
    bouton_dimanche.configure(bg = 'red')
    bouton_semaine.configure(bg = 'red')
    jour=4
    recup(jour)
    
###########################################
# jour1
def vendredi():
    global var_check,bouton_lundi,bouton_mardi,bouton_mercredi,bouton_jeudi,bouton_vendredi,bouton_semaine,bouton_samedi,bouton_dimanche
    #ecriture de la variable sur la base
    variable_input = "planning_jour"
    variable_etat = 5
    update_db(variable_input, variable_etat)
    #modifier couleur bouton
    bouton_lundi.configure(bg = 'red')
    bouton_mardi.configure(bg = 'red')
    bouton_mercredi.configure(bg = 'red')
    bouton_jeudi.configure(bg = 'red')
    bouton_vendredi.configure(bg = 'green')
    bouton_samedi.configure(bg = 'red')
    bouton_dimanche.configure(bg = 'red')
    bouton_semaine.configure(bg = 'red')
    jour=5
    recup(jour)
    
###########################################
# jour1
def samedi():
    global var_check,bouton_lundi,bouton_mardi,bouton_mercredi,bouton_jeudi,bouton_vendredi,bouton_samedi,bouton_dimanche,bouton_semaine
    #ecriture de la variable sur la base
    variable_input = "planning_jour"
    variable_etat = 6
    update_db(variable_input, variable_etat)
    #modifier couleur bouton
    bouton_lundi.configure(bg = 'red')
    bouton_mardi.configure(bg = 'red')
    bouton_mercredi.configure(bg = 'red')
    bouton_jeudi.configure(bg = 'red')
    bouton_vendredi.configure(bg = 'red')
    bouton_samedi.configure(bg = 'green')
    bouton_dimanche.configure(bg = 'red')
    bouton_semaine.configure(bg = 'red')
    jour=6
    recup(jour)

###########################################
# jour1
def dimanche():
    global var_check,bouton_lundi,bouton_mardi,bouton_mercredi,bouton_jeudi,bouton_vendredi,bouton_semaine,bouton_samedi,bouton_dimanche
    #ecriture de la variable sur la base
    variable_input = "planning_jour"
    variable_etat = 7
    update_db(variable_input, variable_etat)
    #modifier couleur bouton
    bouton_lundi.configure(bg = 'red')
    bouton_mardi.configure(bg = 'red')
    bouton_mercredi.configure(bg = 'red')
    bouton_jeudi.configure(bg = 'red')
    bouton_vendredi.configure(bg = 'red')
    bouton_samedi.configure(bg = 'red')
    bouton_dimanche.configure(bg = 'green')
    bouton_semaine.configure(bg = 'red')
    jour=7
    recup(jour)

###########################################
# jour1
def semaine():
    global var_check,bouton_lundi,bouton_mardi,bouton_mercredi,bouton_jeudi,bouton_vendredi,bouton_semaine,bouton_samedi,bouton_dimanche
    #ecriture de la variable sur la base
    variable_input = "planning_jour"
    variable_etat = 8
    update_db(variable_input, variable_etat)
    #modifier couleur bouton
    bouton_lundi.configure(bg = 'red')
    bouton_mardi.configure(bg = 'red')
    bouton_mercredi.configure(bg = 'red')
    bouton_jeudi.configure(bg = 'red')
    bouton_vendredi.configure(bg = 'red')
    bouton_samedi.configure(bg = 'red')
    bouton_dimanche.configure(bg = 'red')
    bouton_semaine.configure(bg = 'green')
    jour=8
    recup(jour)
    
############################################
#fermeture de la fenetre suite appui bouton
def planning_fermer():
    global fenetre_planning,tplanning
    #mise a jour de la base
    tplanning.atuer =True
    variable_input = "fermeture"
    variable_etat = 1
    update_db(variable_input, variable_etat)
    fenetre_planning.destroy()
    
############################################


############################################
#Enregistrement du planning
def planning_enregistrement():
    global var_check

    variable_input = "planning_jour"
    lecture_db(variable_input)
    njour= lecture_db(variable_input)
    
    if njour==1:
        for i in range(0,24):
            etat=var_check[i].get()
            with sqlite3.connect('domotic.db') as co_db:
                curseur = co_db.cursor()
                curseur.execute("""UPDATE Planning SET Lundi = ? WHERE Heure = ?""", (etat,i+1,))
            co_db.close()
    if njour==2:
        for i in range(0,24):
            etat=var_check[i].get()
            with sqlite3.connect('domotic.db') as co_db:
                curseur = co_db.cursor()
                curseur.execute("""UPDATE Planning SET Mardi = ? WHERE Heure = ?""", (etat,i+1,))
            co_db.close()
    if njour==3:
        for i in range(0,24):
            etat=var_check[i].get()
            with sqlite3.connect('domotic.db') as co_db:
                curseur = co_db.cursor()
                curseur.execute("""UPDATE Planning SET Mercredi = ? WHERE Heure = ?""", (etat,i+1,))
            co_db.close()
    if njour==4:
        for i in range(0,24):
            etat=var_check[i].get()
            with sqlite3.connect('domotic.db') as co_db:
                curseur = co_db.cursor()
                curseur.execute("""UPDATE Planning SET Jeudi = ? WHERE Heure = ?""", (etat,i+1,))
            co_db.close()
    if njour==5:
        for i in range(0,25):
            etat=var_check[i].get()
            with sqlite3.connect('domotic.db') as co_db:
                curseur = co_db.cursor()
                curseur.execute("""UPDATE Planning SET Vendredi = ? WHERE Heure = ?""", (etat,i+1,))
            co_db.close()
    if njour==6:
        for i in range(0,24):
            etat=var_check[i].get()
            with sqlite3.connect('domotic.db') as co_db:
                curseur = co_db.cursor()
                curseur.execute("""UPDATE Planning SET Samedi = ? WHERE Heure = ?""", (etat,i+1,))
            co_db.close()
    if njour==7:
        for i in range(0,24):
            etat=var_check[i].get()
            with sqlite3.connect('domotic.db') as co_db:
                curseur = co_db.cursor()
                curseur.execute("""UPDATE Planning SET Dimanche = ? WHERE Heure = ?""", (etat,i+1,))
            co_db.close()
    if njour==8:
        for i in range(0,24):
            etat=var_check[i].get()
            with sqlite3.connect('domotic.db') as co_db:
                curseur = co_db.cursor()
                curseur.execute("""UPDATE Planning SET Semaine = ? WHERE Heure = ?""", (etat,i+1,))
            co_db.close()            
    
############################################

############################################
#Activation du planning
def planning_valider():
    global bouton_activer
    
    #lecture de l'ancienne valeur
    variable_input = "mode_planning"
    lecture_db(variable_input)
    planning_activation = lecture_db(variable_input)

    if (planning_activation ==0):
        variable_input = "mode_planning"
        variable_etat = 1
        update_db(variable_input, variable_etat)
        #modification du bouton
        bouton_activer.configure(text= "Etat : \n activ"+u"\u00E9")
    else:
        variable_input = "mode_planning"
        variable_etat = 0
        update_db(variable_input, variable_etat)
        bouton_activer.configure(text= "Etat : \n d"+u"\u00E9"+"sactiv"+u"\u00E9")

############################################

def ouverture_planning():

    global tplanning,labeltps1,bouton_activer,fenetre_planning,list_check,var_check,bouton_lundi,bouton_mardi,bouton_mercredi,bouton_jeudi,bouton_vendredi,bouton_semaine,bouton_samedi,bouton_dimanche

    #lecture de l'ancienne valeur depuis db
    variable_input = "mode_planning"
    lecture_db(variable_input)
    planning_activation = lecture_db(variable_input)

    if (planning_activation ==0):
        bp_activation="Etat : \n d"+u"\u00E9"+"sactiv"+u"\u00E9"
    else:
        bp_activation="Etat : \n activ"+u"\u00E9"

            
    #fenetre principale
    fenetre_planning = Toplevel()
    fenetre_planning.title('Pilotage de la maison')
    fenetre_planning.resizable(width=FALSE, height=FALSE)

    # get screen width and height
    # calculate x and y coordinates for the Tk root window
    x = (800/2) - (800/2)
    y = (410/2) - (440/2)
    fenetre_planning.geometry('%dx%d+%d+%d' % (800,400, x, y))


    #entete
    entete = Frame(fenetre_planning, bg='grey', height=50)
    entete.pack(fill = X, pady = 2)

    #frame jour
    jour = Frame(fenetre_planning, bg='grey', height=300)
    jour.pack(fill = X, pady = 2)

    #frame visu
    visu = Frame(fenetre_planning, bg='grey', height=300)
    visu.pack(fill = X, pady = 2)

    #bas de page
    bas_page = Frame(fenetre_planning, bg='grey', height=50)
    bas_page.pack(fill = X, pady = 2)

    ############################################
    #mise en place des titres
    ############################################
    # demarrage du thread de l heure
    localdate=1  
    labeltps1 = Label(entete, text="", bg = "grey",fg ="white")
    labeltps1.config(font=("Courier", 20))
    labeltps1.grid(row=0, column=0, sticky="nsew")
    tplanning = threading.Thread(target=planning_comptage)
    tplanning.start()


    ############################################
    #titre principale de la page
    label = Label(entete, text="Planning chaudi"+u"\u00E8"+"re", bg = "grey", fg = "white")
    label.config(font=("Courier", 20))
    label.grid(row=0, column=1, sticky="nsew", ipadx = 150)



    ############################################
    #zone principale

    bouton_lundi = Button(jour, text="Lundi", command=lundi,width = 7)
    bouton_lundi.config(font=("Courier", 12))
    bouton_lundi.grid(row=0, column=0, padx = 1, pady =2)
    bouton_mardi = Button(jour, text="Mardi", command=mardi,width = 7)
    bouton_mardi.config(font=("Courier", 12))
    bouton_mardi.grid(row=0, column=1, padx = 1)
    bouton_mercredi = Button(jour, text="Mercredi", command=mercredi,width = 7)
    bouton_mercredi.config(font=("Courier", 12))
    bouton_mercredi.grid(row=0, column=2, padx = 1)
    bouton_jeudi = Button(jour, text="Jeudi", command=jeudi,width = 7)
    bouton_jeudi.config(font=("Courier", 12))
    bouton_jeudi.grid(row=0, column=3, padx = 1)
    bouton_vendredi = Button(jour, text="Vendredi", command=vendredi,width = 7)
    bouton_vendredi.config(font=("Courier", 12))
    bouton_vendredi.grid(row=0, column=4, padx = 1)
    bouton_samedi = Button(jour, text="Samedi", command=samedi,width = 7)
    bouton_samedi.config(font=("Courier", 12))
    bouton_samedi.grid(row=0, column=5, padx = 1)
    bouton_dimanche = Button(jour, text="Dimanche", command=dimanche,width = 7)
    bouton_dimanche.config(font=("Courier", 12))
    bouton_dimanche.grid(row=0, column=6, padx = 1)
    bouton_semaine = Button(jour, text="Semaine", command=semaine,width = 7)
    bouton_semaine.config(font=("Courier", 12))
    bouton_semaine.grid(row=0, column=7, padx = 1)

    var_check = []
    var0 = IntVar()
    var_check.append(var0)
    var1 = IntVar()
    var_check.append(var1)
    var2 = IntVar()
    var_check.append(var2)
    var3 = IntVar()
    var_check.append(var3)
    var4 = IntVar()
    var_check.append(var4)
    var5 = IntVar()
    var_check.append(var5)
    var6 = IntVar()
    var_check.append(var6)
    var7 = IntVar()
    var_check.append(var7)
    var8 = IntVar()
    var_check.append(var8)
    var9 = IntVar()
    var_check.append(var9)
    var10 = IntVar()
    var_check.append(var10)
    var11 = IntVar()
    var_check.append(var11)
    var12 = IntVar()
    var_check.append(var12)
    var13 = IntVar()
    var_check.append(var13)
    var14 = IntVar()
    var_check.append(var14)
    var15 = IntVar()
    var_check.append(var15)
    var16 = IntVar()
    var_check.append(var16)
    var17 = IntVar()
    var_check.append(var17)
    var18 = IntVar()
    var_check.append(var18)
    var19 = IntVar()
    var_check.append(var19)
    var20 = IntVar()
    var_check.append(var20)
    var21 = IntVar()
    var_check.append(var21)
    var22 = IntVar()
    var_check.append(var22)
    var23 = IntVar()
    var_check.append(var23)

    #liste des boutons
    list_check = []

    #creation des checks box
    var=0
    #premiere ligne

    for i in range (1,5):
        text1= str(var)+"h00 a "+str(var+1)+"h00"
        c = Checkbutton(visu, text=text1, variable=var_check[var])
        c.config(font=("Courier", 14))
        c.grid(row=1, column=i-1,padx=12,pady=4, sticky="nsew")
        var=var+1
        list_check.append(c)
    #ligne2
    for i in range (1,5):
        text1= str(var)+"h00 a "+str(var+1)+"h00"
        c = Checkbutton(visu, text=text1, variable=var_check[var])
        c.config(font=("Courier", 14))
        c.grid(row=2, column=i-1,padx=12,pady=4, sticky="nsew")
        var=var+1
        list_check.append(c)
    #ligne3
    for i in range (1,5):
        text1= str(var)+"h00 a "+str(var+1)+"h00"
        c = Checkbutton(visu, text=text1, variable=var_check[var])
        c.config(font=("Courier", 14))
        c.grid(row=3, column=i-1,padx=12,pady=4, sticky="nsew")
        var=var+1
        list_check.append(c)
    #ligne4
    for i in range (1,5):
        text1= str(var)+"h00 a "+str(var+1)+"h00"
        c = Checkbutton(visu, text=text1, variable=var_check[var])
        c.config(font=("Courier", 14))
        c.grid(row=4, column=i-1,padx=12,pady=4, sticky="nsew")
        var=var+1
        list_check.append(c)
    #ligne5
    for i in range (1,5):
        text1= str(var)+"h00 a "+str(var+1)+"h00"
        c = Checkbutton(visu, text=text1, variable=var_check[var])
        c.config(font=("Courier", 14))
        c.grid(row=5, column=i-1,padx=12,pady=4, sticky="nsew")
        var=var+1
        list_check.append(c)
    #ligne6
    for i in range (1,5):
        text1= str(var)+"h00 a "+str(var+1)+"h00"
        c = Checkbutton(visu, text=text1, variable=var_check[var])
        c.config(font=("Courier", 14))
        c.grid(row=6, column=i-1,padx=12,pady=4, sticky="nsew")
        
        list_check.append(c)
        var=var+1



    #mise a jour des check
    variable_input = "planning_jour"
    lecture_db(variable_input)
    njour= lecture_db(variable_input)
    if njour==1:
        lundi()
    if njour==2:
        mardi()
    if njour==3:
        mercredi()
    if njour==4:
        jeudi()
    if njour==5:
        vendredi()
    if njour==6:
        samedi()
    if njour==7:
        dimanche()
    if njour==8:
        semaine()

      
    ############################################
    #Enregistrer planning
    bouton_enregistrer = Button(bas_page, text="Enregistrer", command=planning_enregistrement,width = 11)
    bouton_enregistrer.config(font=("Courier", 14))
    bouton_enregistrer.grid(row=0, column=0,  rowspan=1,  sticky="ns",pady = 4, padx = 3)

    #Activer planning
    bouton_activer = Button(bas_page, text=bp_activation, command=planning_valider,width = 11)
    bouton_activer.config(font=("Courier", 14))
    bouton_activer.grid(row=0, column=1,  rowspan=1,  sticky="ns",pady = 4, padx = 3)

    #bouton de fermeture de la page
    bouton_fermeture = Button(bas_page, text="Retour", command=planning_fermer,width = 11)
    bouton_fermeture.config(font=("Courier", 14))
    bouton_fermeture.grid(row=0, column=2,  rowspan=1,  sticky="ns",pady = 4, padx = 3)


        
