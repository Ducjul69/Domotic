from programme_outil_db import*


def condition_allumage_planning ():
    #lecture de l'heure
    variable_input = "heure"
    lecture_db(variable_input)
    heure= lecture_db(variable_input)
    heure=heure+1

    #lecture du jour
    variable_input = "jour"
    lecture_db(variable_input)
    jour= lecture_db(variable_input)

    #lecture du jour selectionne
    variable_input = "planning_jour"
    lecture_db(variable_input)
    jour_planifie= lecture_db(variable_input)
    
    #lecture selection du jour
    if jour == jour_planifie:
        if jour==1 :
            for i in range (1 , 25):
                if i == heure:
                    with sqlite3.connect('/home/pi/Desktop/Programme_Domotic/domotic.db') as co_db:
                        curseur = co_db.cursor()
                        curseur.execute("""SELECT Lundi FROM Planning WHERE Heure=?""", (i,))
                        variable_output=(curseur.fetchone()[0])
                    co_db.close()
                    if variable_output ==1:
                        variable_input = "etat_chaudiere"
                        variable_etat = 1
                        update_db(variable_input, variable_etat)
                    else:
                        variable_input = "etat_chaudiere"
                        variable_etat = 0
                        update_db(variable_input, variable_etat)
                        
        if jour==2 : 
            for i in range (1 ,25):
                if i == heure:
                    with sqlite3.connect('/home/pi/Desktop/Programme_Domotic/domotic.db') as co_db:
                        curseur = co_db.cursor()
                        curseur.execute("""SELECT Mardi FROM Planning WHERE Heure=?""", (i,))
                        variable_output=(curseur.fetchone()[0])
                    co_db.close()
                    if variable_output ==1:
                        variable_input = "etat_chaudiere"
                        variable_etat = 1
                        update_db(variable_input, variable_etat)
                    else:
                        variable_input = "etat_chaudiere"
                        variable_etat = 0
                        update_db(variable_input, variable_etat)

        if jour==3 :
            for i in range (1 ,25):
                if i == heure:
                    with sqlite3.connect('/home/pi/Desktop/Programme_Domotic/domotic.db') as co_db:
                        curseur = co_db.cursor()
                        curseur.execute("""SELECT Mercredi FROM Planning WHERE Heure=?""", (i,))
                        variable_output=(curseur.fetchone()[0])
                    co_db.close()
                    if variable_output ==1:
                        variable_input = "etat_chaudiere"
                        variable_etat = 1
                        update_db(variable_input, variable_etat)
                    else:
                        variable_input = "etat_chaudiere"
                        variable_etat = 0
                        update_db(variable_input, variable_etat)
                                  
        if jour==4 :
            for i in range (1 ,25):
                if i == heure:
                    with sqlite3.connect('/home/pi/Desktop/Programme_Domotic/domotic.db') as co_db:
                        curseur = co_db.cursor()
                        curseur.execute("""SELECT Jeudi FROM Planning WHERE Heure=?""", (i,))
                        variable_output=(curseur.fetchone()[0])
                    co_db.close()
                    if variable_output ==1:
                        variable_input = "etat_chaudiere"
                        variable_etat = 1
                        update_db(variable_input, variable_etat)
                    else:
                        variable_input = "etat_chaudiere"
                        variable_etat = 0
                        update_db(variable_input, variable_etat)

        if jour==5 :
            for i in range (1 ,25):
                if i == heure:
                    with sqlite3.connect('/home/pi/Desktop/Programme_Domotic/domotic.db') as co_db:
                        curseur = co_db.cursor()
                        curseur.execute("""SELECT Vendredi FROM Planning WHERE Heure=?""", (i,))
                        variable_output=(curseur.fetchone()[0])
                    co_db.close()
                    if variable_output ==1:
                        variable_input = "etat_chaudiere"
                        variable_etat = 1
                        update_db(variable_input, variable_etat)
                    else:
                        variable_input = "etat_chaudiere"
                        variable_etat = 0
                        update_db(variable_input, variable_etat)
                                  
        if jour==6 :
            for i in range (1 ,25):
                if i == heure:
                    with sqlite3.connect('/home/pi/Desktop/Programme_Domotic/domotic.db') as co_db:
                        curseur = co_db.cursor()
                        curseur.execute("""SELECT Samedi FROM Planning WHERE Heure=?""", (i,))
                        variable_output=(curseur.fetchone()[0])
                    co_db.close()
                    if variable_output ==1:
                        variable_input = "etat_chaudiere"
                        variable_etat = 1
                        update_db(variable_input, variable_etat)
                    else:
                        variable_input = "etat_chaudiere"
                        variable_etat = 0
                        update_db(variable_input, variable_etat)


        if jour==7 :
            for i in range (1 ,25):
                if i == heure:
                    with sqlite3.connect('/home/pi/Desktop/Programme_Domotic/domotic.db') as co_db:
                        curseur = co_db.cursor()
                        curseur.execute("""SELECT Dimanche FROM Planning WHERE Heure=?""", (i,))
                        variable_output=(curseur.fetchone()[0])
                    co_db.close()
                    if variable_output ==1:
                        variable_input = "etat_chaudiere"
                        variable_etat = 1
                        update_db(variable_input, variable_etat)
                    else:
                        variable_input = "etat_chaudiere"
                        variable_etat = 0
                        update_db(variable_input, variable_etat)


                                
    if jour_planifie == 8 :
        for i in range (1 ,25): 
            if i == heure:
                with sqlite3.connect('/home/pi/Desktop/Programme_Domotic/domotic.db') as co_db:
                    curseur = co_db.cursor()
                    curseur.execute("""SELECT Semaine FROM Planning WHERE Heure=?""", (i,))
                    variable_output=(curseur.fetchone()[0])
                co_db.close()
                if variable_output ==1:
                    variable_input = "etat_chaudiere"
                    variable_etat = 1
                    update_db(variable_input, variable_etat)
                else:
                    variable_input = "etat_chaudiere"
                    variable_etat = 0
                    update_db(variable_input, variable_etat)
        
