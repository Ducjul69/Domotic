#!/usr/bin/env /usr/bin/python

import os
import time
import threading
from datetime import datetime
from programme_outil_db import*

###########################################
# Gestion de l'heure   
def comptage():
    #global localdate,strtpsh, tpsh
    maintenant = datetime.now()
    tpsh = maintenant.hour
    tpsh=int(tpsh)
    #ecriture de l'heure sur la bd
    variable_input = "heure"
    variable_etat = tpsh
    update_db(variable_input, variable_etat)

    #ecriture du jour dans la base
    jours = [1, 2,3, 4, 5, 6, 7]
    date =int(jours[time.localtime()[6]])
    variable_input = "jour"
    variable_etat = date
    update_db(variable_input, variable_etat)

    
    strtpsh = str(tpsh)
    tpsm = maintenant.minute
    strtpsm = str(tpsm)
    tpss = maintenant.second
    strtpss = str(tpss)
    localdate = strtpsh+":"+strtpsm+":"+strtpss
    
    time.sleep(1)
    
    return localdate
            
############################################


