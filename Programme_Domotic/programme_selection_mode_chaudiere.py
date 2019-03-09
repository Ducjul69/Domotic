from programme_outil_db import*
import threading
import time

from programme_condition_allumage_planning import*

def conditions():
    global mode_manu_old,mode_auto_old, mode_planning_old
    while 1:
        #conditions initiale
        #mode de marche manu
        variable_input = "mode_manu"
        lecture_db(variable_input)
        mode_manu_new = lecture_db(variable_input)
        #mode de marche manu tempo
        variable_input = "tempo_manu"
        lecture_db(variable_input)
        tempo_manu = lecture_db(variable_input)
        
        #mode de marche auto
        variable_input = "mode_auto"
        lecture_db(variable_input)
        mode_auto_new= lecture_db(variable_input)
        #mode de marche planning
        variable_input = "mode_planning"
        lecture_db(variable_input)
        mode_planning_new= lecture_db(variable_input)
        #mode de marche global
        variable_input = "mode_de_marche"
        lecture_db(variable_input)
        mode_de_marche_new= lecture_db(variable_input)

        
        if mode_manu_new == 0 and mode_auto_new == 0 and mode_planning_new == 0:
            #passage de la chaudiere a 0
            variable_input = "etat_chaudiere"
            variable_etat = 0
            update_db(variable_input, variable_etat)
            #ecriture mode de marche
            variable_input = "mode_de_marche"
            variable_etat = 0
            update_db(variable_input, variable_etat)
            
        

        
        elif mode_manu_old != mode_manu_new and tempo_manu==0 and mode_manu_new !=2:
            if mode_manu_new==1:
                #passage des autres modes a 0
                variable_input = "mode_auto"
                variable_etat = 0
                update_db(variable_input, variable_etat)
                mode_auto_new=0
                mode_auto_old=0

                #passage de la chaudiere a 1
                variable_input = "etat_chaudiere"
                variable_etat = 1
                update_db(variable_input, variable_etat)
                #ecriture mode de marche
                variable_input = "mode_de_marche"
                variable_etat = 1
                update_db(variable_input, variable_etat)

                #mise a jour de la variable
                mode_manu_old =1 
            else:
                mode_manu_old =0

        elif mode_manu_new==2:
            if mode_manu_new==2:
                #passage des autres modes a 0
                variable_input = "mode_auto"
                variable_etat = 0
                update_db(variable_input, variable_etat)
                mode_auto_new=0
                mode_auto_old=0

                #passage de la chaudiere a 1
                variable_input = "etat_chaudiere"
                variable_etat = 1
                update_db(variable_input, variable_etat)
                #ecriture mode de marche
                variable_input = "mode_de_marche"
                variable_etat = 4
                update_db(variable_input, variable_etat)

                #mise a jour de la variable
                mode_manu_old =0 
        

        elif mode_auto_new ==1:
            variable_input = "mode_de_marche"
            variable_etat = 2
            update_db(variable_input, variable_etat)
       

        elif mode_planning_old != mode_planning_new:            
            if mode_planning_new==1:
                #passage des autres modes a 0
                variable_input = "mode_auto"
                variable_etat = 0
                update_db(variable_input, variable_etat)
                mode_auto_old=0
                mode_auto_new=0 

                variable_input = "mode_manu"
                variable_etat = 0
                update_db(variable_input, variable_etat)
                mode_manu_old=0
                mode_manu_new=0
                
                #ecriture mode de marche
                variable_input = "mode_de_marche"
                variable_etat = 3
                update_db(variable_input, variable_etat)

                #mise a jour de la variable
                mode_planning_old =1
            else:
                mode_planning_old =0
                
        elif mode_planning_new==mode_planning_old and mode_planning_old ==1  and mode_auto_new==0 and mode_manu_new ==0:
            #ecriture mode de marche
            variable_input = "mode_de_marche"
            variable_etat = 3
            update_db(variable_input, variable_etat)

            #passage des autres modes a 0
            variable_input = "mode_auto"
            variable_etat = 0
            update_db(variable_input, variable_etat)
            mode_auto_old=0
            mode_auto_new=0   

            variable_input = "mode_manu"
            variable_etat = 0
            update_db(variable_input, variable_etat)
            mode_manu_old=0
            mode_manu_new=0

            #condition d allumage en mode planning
            condition_allumage_planning ()
            
            

        
def changement_etat_chaudiere():

    global mode_manu_old,mode_auto_old, mode_planning_old
    
    #conditions initiale
    mode_manu_old= 0
    #mode de marche auto
    mode_auto_old= 0
    #mode de marche planning
    mode_planning_old= 0
    t1 = threading.Thread(target=conditions)
    t1.start()
    
