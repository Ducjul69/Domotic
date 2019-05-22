import os
import time
import threading

from programme_outil_db import*

def condition_auto():
    #récupération de l'état sur la base
    variable_input = "mode_auto"
    lecture_db(variable_input)
    mode_auto= lecture_db(variable_input)
    #récuperation des seuils 
    variable_input = "seuil_temp_ext"
    lecture_db(variable_input)
    seuil_temp_ext= lecture_db(variable_input)
    variable_input = "seuil_temp_int"
    lecture_db(variable_input)
    seuil_temp_int= lecture_db(variable_input)

    #condition activer / désactiver
    if mode_auto == 1:        
        #ecriture sur la db auto =0
        variable_input = "mode_auto"
        variable_etat = 0
        update_db(variable_input, variable_etat)


        
    else:
        #ecriture sur la db auto =1
        variable_input = "mode_auto"
        variable_etat = 1
        update_db(variable_input, variable_etat)
        mode_auto = 1
        #ecriture sur la base manu = 0
        variable_input = "mode_manu"
        variable_etat = 0
        update_db(variable_input, variable_etat)
        #ecriture sur la base manu tempo = 0
        variable_input = "tempo_manu"
        variable_etat = 0
        update_db(variable_input, variable_etat)
        
        while mode_auto == 1:
            #mise en pause
            time.sleep(1)

            #condition d'allumage
            #récuperation temp exterieur
            variable_input = "temperature_exterieur"
            lecture_db(variable_input)
            temperature_exterieur= lecture_db(variable_input)
            #recuperation temperature interieur
            variable_input = "temperature_interieur"
            lecture_db(variable_input)
            temperature_interieur= lecture_db(variable_input)

            
            try:    
                if int(temperature_interieur) <= seuil_temp_int and int(temperature_exterieur) <= seuil_temp_int :
                    #mise à ON de la chaudiere
                    variable_input = "etat_chaudiere"
                    variable_etat = 1
                    update_db(variable_input, variable_etat)
                    
                else :
                    #mise à OFF de la chaudiere
                    variable_input = "etat_chaudiere"
                    variable_etat = 0
                    update_db(variable_input, variable_etat)
            except:
                print("Mode auto : Erreur dans les valeurs de température")
                #passage du mode auto à 0
                variable_input = "mode_auto"
                variable_etat = 0
                update_db(variable_input, variable_etat)

            

            #lecture new valeur mode auto
            variable_input = "mode_auto"
            lecture_db(variable_input)
            mode_auto= lecture_db(variable_input)

def programme_auto ():
    t1 = threading.Thread(target=condition_auto)
    t1.start()
