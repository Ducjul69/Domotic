from programme_outil_db import*
import threading
import time

from programme_condition_allumage_planning import*

def conditions():
    while 1:
        #lecture des variables
        
        #mode de marche manu
        variable_input = "mode_manu"
        lecture_db(variable_input)
        mode_manu = lecture_db(variable_input)
        #mode de marche manu tempo
        variable_input = "tempo_manu"
        lecture_db(variable_input)
        tempo_manu = lecture_db(variable_input)
        
        #mode de marche auto
        variable_input = "mode_auto"
        lecture_db(variable_input)
        mode_auto= lecture_db(variable_input)
        
        #mode de marche planning
        variable_input = "mode_planning"
        lecture_db(variable_input)
        mode_planning= lecture_db(variable_input)
        
        #mode de marche global
        variable_input = "mode_de_marche"
        lecture_db(variable_input)
        mode_de_marche= lecture_db(variable_input)

        
        if mode_manu== 0 and mode_auto == 0 and mode_planning == 0:
            #passage de la chaudiere a 0
            variable_input = "etat_chaudiere"
            variable_etat = 0
            update_db(variable_input, variable_etat)
            #ecriture mode de marche
            variable_input = "mode_de_marche"
            variable_etat = 0
            update_db(variable_input, variable_etat)

        if mode_manu==1:
            #passage de la chaudiere a 1
            variable_input = "etat_chaudiere"
            variable_etat = 1
            update_db(variable_input, variable_etat)
            #ecriture mode de marche
            variable_input = "mode_de_marche"
            variable_etat = 1
            update_db(variable_input, variable_etat)

        if mode_manu==2:
            #passage de la chaudiere a 1
            variable_input = "etat_chaudiere"
            variable_etat = 1
            update_db(variable_input, variable_etat)
            #ecriture mode de marche
            variable_input = "mode_de_marche"
            variable_etat = 4
            update_db(variable_input, variable_etat)

        if mode_auto ==1:
            variable_input = "mode_de_marche"
            variable_etat = 2
            update_db(variable_input, variable_etat)
       

        if mode_manu==0 and mode_auto==0 :            
            if mode_planning==1:
                #ecriture mode de marche
                variable_input = "mode_de_marche"
                variable_etat = 3
                update_db(variable_input, variable_etat)
                #condition d allumage en mode planning
                condition_allumage_planning ()
            
        
def changement_etat_chaudiere():
    t1 = threading.Thread(target=conditions)
    t1.start()
    
